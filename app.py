import streamlit as st

from graph import generate_learning_path
from data import SKILLS, LEARNING_MATERIALS


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="LearnGraph AI",
    page_icon="🎓",
    layout="wide"
)


# ==========================================================
# SESSION STATE
# ==========================================================

if "learning_path" not in st.session_state:
    st.session_state.learning_path = []

if "completed_topics" not in st.session_state:
    st.session_state.completed_topics = set()


# ==========================================================
# PROGRESS FUNCTION
# ==========================================================

def update_topic_progress(topic_id):

    if st.session_state.get(topic_id, False):
        st.session_state.completed_topics.add(topic_id)
    else:
        st.session_state.completed_topics.discard(topic_id)


# ==========================================================
# TITLE
# ==========================================================

st.title("🎓 LearnGraph AI")

st.subheader(
    "Personalized Learning Roadmap using Knowledge Graphs"
)

st.write(
    "Choose what you already know and what you want to learn. "
    "The knowledge graph will find a learning path between them."
)


# ==========================================================
# INPUT SECTION
# ==========================================================

st.header("🎯 Build Your Learning Path")

col1, col2 = st.columns(2)

with col1:

    current_skill = st.selectbox(
        "What do you already know?",
        SKILLS,
        index=0
    )

with col2:

    target_skill = st.selectbox(
        "What do you want to learn?",
        SKILLS,
        index=1
    )


# ==========================================================
# GENERATE ROADMAP
# ==========================================================

if st.button(
    "🚀 Generate My Roadmap",
    use_container_width=True
):

    if current_skill == target_skill:

        st.warning(
            "Please choose different current and target skills."
        )

    else:

        try:

            learning_path = generate_learning_path(
                current_skill,
                target_skill
            )

            st.session_state.learning_path = learning_path

            # Reset progress
            st.session_state.completed_topics = set()

            # Remove old checkbox states
            for key in list(st.session_state.keys()):

                if key.startswith("topic_"):
                    del st.session_state[key]

        except (ValueError, KeyError) as error:

            st.error(
                f"Please check your learning data: {error}"
            )

            st.session_state.learning_path = []


# ==========================================================
# GET CURRENT LEARNING PATH
# ==========================================================

learning_path = st.session_state.learning_path


# ==========================================================
# NO ROADMAP YET
# ==========================================================

if not learning_path:

    st.info(
        "👆 Select your current skill and target skill, "
        "then click **Generate My Roadmap**."
    )


# ==========================================================
# DISPLAY ROADMAP
# ==========================================================

else:

    # ------------------------------------------------------
    # COLLECT ALL TOPICS
    # ------------------------------------------------------

    all_topics = []

    for skill in learning_path:

        material = LEARNING_MATERIALS.get(
            skill,
            {}
        )

        topics = material.get(
            "topics",
            []
        )

        if isinstance(topics, list):

            for index, topic in enumerate(topics):

                topic_id = f"topic_{skill}_{index}"

                all_topics.append(
                    (
                        skill,
                        topic,
                        topic_id
                    )
                )


    # ------------------------------------------------------
    # CALCULATE OVERALL PROGRESS
    # ------------------------------------------------------

    total_topics = len(all_topics)

    completed_topics = sum(
        1
        for _, _, topic_id in all_topics
        if topic_id in st.session_state.completed_topics
    )

    remaining_topics = (
        total_topics - completed_topics
    )

    if total_topics > 0:

        progress_percentage = (
            completed_topics / total_topics
        )

    else:

        progress_percentage = 0


    # ======================================================
    # PROGRESS DASHBOARD
    # ======================================================

    st.header("📊 Your Learning Progress")

    progress_col1, progress_col2, progress_col3 = st.columns(3)

    with progress_col1:

        st.metric(
            "📚 Total Topics",
            total_topics
        )

    with progress_col2:

        st.metric(
            "✅ Completed",
            completed_topics
        )

    with progress_col3:

        st.metric(
            "⏳ Remaining",
            remaining_topics
        )

    st.progress(progress_percentage)

    st.write(
        f"### 🎯 Overall Progress: "
        f"{progress_percentage * 100:.0f}%"
    )


    # ------------------------------------------------------
    # COMPLETION MESSAGE
    # ------------------------------------------------------

    if (
        total_topics > 0
        and completed_topics == total_topics
    ):

        st.success(
            "🎉 Congratulations! "
            "You completed your entire learning roadmap!"
        )


    # ======================================================
    # ROADMAP
    # ======================================================

    st.header("🗺️ Your Personalized Roadmap")

    st.write(
        f"**{current_skill}** → **{target_skill}**"
    )


    total_hours = 0


    # ======================================================
    # DISPLAY EACH SKILL
    # ======================================================

    for index, skill in enumerate(learning_path):

        material = LEARNING_MATERIALS.get(
            skill,
            {}
        )

        if not isinstance(material, dict):
            material = {}


        # --------------------------------------------------
        # GET LEARNING INFORMATION
        # --------------------------------------------------

        description = material.get(
            "description",
            f"Learn the fundamentals of {skill}."
        )

        topics = material.get(
            "topics",
            []
        )

        resources = material.get(
            "resources",
            []
        )

        projects = material.get(
            "projects",
            []
        )

        hours = material.get(
            "hours",
            0
        )


        # --------------------------------------------------
        # SAFETY CHECKS
        # --------------------------------------------------

        if not isinstance(topics, list):
            topics = []

        if not isinstance(resources, list):
            resources = []

        if not isinstance(projects, list):
            projects = []

        if not isinstance(hours, (int, float)):
            hours = 0


        total_hours += hours


        # --------------------------------------------------
        # CALCULATE SKILL PROGRESS
        # --------------------------------------------------

        skill_completed = 0

        for topic_index, topic in enumerate(topics):

            topic_id = (
                f"topic_{skill}_{topic_index}"
            )

            if (
                topic_id
                in st.session_state.completed_topics
            ):

                skill_completed += 1


        skill_total = len(topics)

        if skill_total > 0:

            skill_progress = (
                skill_completed / skill_total
            )

        else:

            skill_progress = 0


        # ==================================================
        # SKILL SECTION
        # ==================================================

        st.divider()

        st.subheader(
            f"Step {index + 1}: {skill}"
        )

        st.write(description)


        # --------------------------------------------------
        # SKILL PROGRESS
        # --------------------------------------------------

        st.write(
            f"**Skill Progress: "
            f"{skill_completed}/{skill_total} "
            f"topics completed**"
        )

        st.progress(skill_progress)


        # --------------------------------------------------
        # LEARNING DETAILS
        # --------------------------------------------------

        with st.expander(
            f"📚 Learn {skill}"
        ):

            topic_col, resource_col = st.columns(2)


            # ==============================================
            # TOPICS
            # ==============================================

            with topic_col:

                st.markdown("### 📖 Topics")

                if topics:

                    for topic_index, topic in enumerate(topics):

                        topic_id = (
                            f"topic_{skill}_{topic_index}"
                        )

                        st.checkbox(
                            topic,
                            key=topic_id,
                            on_change=update_topic_progress,
                            args=(topic_id,)
                        )

                else:

                    st.write(
                        "No topics available yet."
                    )


            # ==============================================
            # RESOURCES
            # ==============================================

            with resource_col:

                st.markdown("### 🔗 Learning Resources")

                if resources:

                    for resource in resources:

                        # Resource stored as:
                        # ("Resource Name", "URL")

                        if (
                            isinstance(
                                resource,
                                (tuple, list)
                            )
                            and len(resource) == 2
                        ):

                            resource_name, resource_url = resource

                            st.markdown(
                                f"🔗 [{resource_name}]"
                                f"({resource_url})"
                            )

                        # Resource stored only as URL

                        elif isinstance(
                            resource,
                            str
                        ):

                            st.markdown(
                                f"🔗 [Open Resource]"
                                f"({resource})"
                            )

                        else:

                            st.write(
                                str(resource)
                            )

                else:

                    st.write(
                        "No resources available yet."
                    )


            # ==============================================
            # PROJECTS
            # ==============================================

            st.markdown("### 🛠️ Practice Projects")

            if projects:

                for project in projects:

                    # Project stored as:
                    # ("Project Name", "URL")

                    if (
                        isinstance(
                            project,
                            (tuple, list)
                        )
                        and len(project) == 2
                    ):

                        project_name, project_url = project

                        st.markdown(
                            f"🔹 **{project_name}**"
                        )

                        st.link_button(
                            "View Project",
                            project_url
                        )

                    # Project stored only as text

                    else:

                        st.write(
                            f"• {project}"
                        )

            else:

                st.write(
                    "No projects available yet."
                )


            # ==============================================
            # LEARNING TIME
            # ==============================================

            st.info(
                f"⏱️ Estimated learning time: "
                f"**{hours} hours**"
            )


    # ======================================================
    # FINAL GOAL
    # ======================================================

    st.divider()

    st.header("🎯 Final Goal")

    st.info(
        f"Your learning route starts with "
        f"**{current_skill}** and ends with "
        f"**{target_skill}**."
    )


    # ======================================================
    # FINAL STATISTICS
    # ======================================================

    goal_col1, goal_col2, goal_col3 = st.columns(3)

    with goal_col1:

        st.metric(
            "⏱️ Total Learning Time",
            f"{total_hours} hours"
        )

    with goal_col2:

        st.metric(
            "✅ Topics Completed",
            completed_topics
        )

    with goal_col3:

        st.metric(
            "⏳ Topics Remaining",
            remaining_topics
        )


    # ======================================================
    # RESET PROGRESS
    # ======================================================

    st.divider()

    if st.button(
        "🔄 Reset All Progress"
    ):

        # Remove topic checkbox states
        for key in list(st.session_state.keys()):

            if key.startswith("topic_"):

                del st.session_state[key]

        st.session_state.completed_topics = set()

        st.rerun()


# ==========================================================
# FOOTER
# ==========================================================

st.divider()

st.caption(
    "LearnGraph AI • Personalized Learning with Knowledge Graphs"
)