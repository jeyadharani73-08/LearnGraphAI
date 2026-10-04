import re

from data import LEARNING_MATERIALS
from graph import generate_learning_path


class GraphRAG:

    def __init__(self):
        self.documents = []
        self.load_documents()

    def load_documents(self):

        for skill, resources in LEARNING_MATERIALS.items():

            for resource in resources:

                if isinstance(resource, dict):

                    title = resource.get(
                        "title",
                        skill
                    )

                    url = resource.get(
                        "url",
                        ""
                    )

                else:

                    title = skill
                    url = resource

                self.documents.append(
                    {
                        "skill": skill,
                        "title": title,
                        "url": url
                    }
                )

    def tokenize(self, text):

        return set(
            re.findall(
                r"[a-zA-Z0-9]+",
                text.lower()
            )
        )

    def retrieve(self, question):

        question_words = self.tokenize(
            question
        )

        results = []

        for document in self.documents:

            skill_words = self.tokenize(
                document["skill"]
            )

            score = len(
                question_words & skill_words
            )

            if score > 0:

                results.append(
                    (
                        score,
                        document
                    )
                )

        results.sort(
            key=lambda x: x[0],
            reverse=True
        )

        return [
            document
            for score, document in results[:5]
        ]

    def answer(
        self,
        question,
        target_skill
    ):

        roadmap = generate_learning_path(
            target_skill
        )

        retrieved = self.retrieve(
            question
        )

        if roadmap:

            roadmap_text = " → ".join(
                roadmap
            )

            answer = (
                f"Your roadmap to {target_skill} is: "
                f"{roadmap_text}"
            )

        else:

            answer = (
                "No roadmap was found."
            )

        return {
            "answer": answer,
            "roadmap": roadmap,
            "sources": retrieved
        }