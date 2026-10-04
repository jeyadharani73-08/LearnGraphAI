# ==========================================================
# LEARNGRAPH AI - DATA
# ==========================================================

# ----------------------------------------------------------
# SKILLS / GRAPH NODES
# ----------------------------------------------------------

SKILLS = [
    "Python",
    "Data Structures",
    "Algorithms",
    "Mathematics",
    "Statistics",
    "Machine Learning",
    "Deep Learning",
    "Generative AI"
]


# ----------------------------------------------------------
# GRAPH RELATIONSHIPS
# ----------------------------------------------------------

PREREQUISITES = [
    ("Python", "Data Structures"),
    ("Data Structures", "Algorithms"),
    ("Algorithms", "Machine Learning"),
    ("Statistics", "Machine Learning"),
    ("Machine Learning", "Deep Learning"),
    ("Deep Learning", "Generative AI")
]


# ----------------------------------------------------------
# LEARNING MATERIALS
# ----------------------------------------------------------

LEARNING_MATERIALS = {

    # ======================================================
    # PYTHON
    # ======================================================

    "Python": {
        "description": "Learn the fundamentals of Python programming.",

        "topics": [
            "Variables and Data Types",
            "Conditions and Loops",
            "Functions",
            "Lists, Tuples and Dictionaries",
            "Object-Oriented Programming"
        ],

        "resources": [
            ("Python Official Tutorial",
             "https://docs.python.org/3/tutorial/"),

            ("W3Schools Python",
             "https://www.w3schools.com/python/"),

            ("GeeksforGeeks Python",
             "https://www.geeksforgeeks.org/python-programming-language/"),

            ("freeCodeCamp Python",
             "https://www.freecodecamp.org/learn/scientific-computing-with-python/")
        ],

        "projects": [
            ("Calculator Project",
             "https://github.com/topics/python-calculator"),

            ("To-Do List Project",
             "https://github.com/topics/python-todo"),

            ("Number Guessing Game",
             "https://github.com/topics/python-number-guessing-game")
        ],

        "hours": 10
    },


    # ======================================================
    # DATA STRUCTURES
    # ======================================================

    "Data Structures": {
        "description": "Learn how data can be organized and efficiently accessed.",

        "topics": [
            "Arrays and Lists",
            "Stacks",
            "Queues",
            "Hash Tables",
            "Trees",
            "Graphs"
        ],

        "resources": [
            ("GeeksforGeeks Data Structures",
             "https://www.geeksforgeeks.org/data-structures/"),

            ("Programiz Data Structures",
             "https://www.programiz.com/dsa"),

            ("W3Schools Data Structures",
             "https://www.w3schools.com/dsa/"),

            ("freeCodeCamp Data Structures",
             "https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures-v8/")
        ],

        "projects": [
            ("Stack Implementation",
             "https://github.com/topics/stack-data-structure"),

            ("Queue Implementation",
             "https://github.com/topics/queue-data-structure"),

            ("Binary Search Tree",
             "https://github.com/topics/binary-search-tree")
        ],

        "hours": 12
    },


    # ======================================================
    # ALGORITHMS
    # ======================================================

    "Algorithms": {
        "description": "Learn fundamental algorithms and problem-solving techniques.",

        "topics": [
            "Searching Algorithms",
            "Sorting Algorithms",
            "Recursion",
            "Breadth First Search",
            "Depth First Search",
            "Shortest Path Algorithms"
        ],

        "resources": [
            ("GeeksforGeeks Algorithms",
             "https://www.geeksforgeeks.org/fundamentals-of-algorithms/"),

            ("Programiz Algorithms",
             "https://www.programiz.com/dsa/algorithm"),

            ("Khan Academy Algorithms",
             "https://www.khanacademy.org/computing/computer-science/algorithms"),

            ("freeCodeCamp Algorithms",
             "https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures-v8/")
        ],

        "projects": [
            ("Sorting Visualizer",
             "https://github.com/topics/sorting-visualizer"),

            ("Maze Solver",
             "https://github.com/topics/maze-solver"),

            ("Pathfinding Visualizer",
             "https://github.com/topics/pathfinding-visualizer")
        ],

        "hours": 15
    },


    # ======================================================
    # MATHEMATICS
    # ======================================================

    "Mathematics": {
        "description": "Learn mathematical foundations useful for AI and machine learning.",

        "topics": [
            "Linear Algebra",
            "Vectors",
            "Matrices",
            "Functions",
            "Probability Basics"
        ],

        "resources": [
            ("Khan Academy Mathematics",
             "https://www.khanacademy.org/math"),

            ("3Blue1Brown Linear Algebra",
             "https://www.3blue1brown.com/topics/linear-algebra"),

            ("MIT OpenCourseWare Mathematics",
             "https://ocw.mit.edu/search/?d=Mathematics"),

            ("Paul's Online Math Notes",
             "https://tutorial.math.lamar.edu/")
        ],

        "projects": [
            ("Matrix Calculator",
             "https://github.com/topics/matrix-calculator"),

            ("Linear Algebra Projects",
             "https://github.com/topics/linear-algebra"),

            ("Probability Projects",
             "https://github.com/topics/probability")
        ],

        "hours": 15
    },


    # ======================================================
    # STATISTICS
    # ======================================================

    "Statistics": {
        "description": "Learn statistics required for understanding machine learning.",

        "topics": [
            "Mean and Median",
            "Variance and Standard Deviation",
            "Probability",
            "Distributions",
            "Correlation",
            "Hypothesis Testing"
        ],

        "resources": [
            ("Khan Academy Statistics",
             "https://www.khanacademy.org/math/statistics-probability"),

            ("StatQuest",
             "https://statquest.org/"),

            ("NIST Statistics Handbook",
             "https://www.itl.nist.gov/div898/handbook/"),

            ("OpenIntro Statistics",
             "https://www.openintro.org/book/os/")
        ],

        "projects": [
            ("Statistics Projects",
             "https://github.com/topics/statistics-project"),

            ("Data Analysis Projects",
             "https://github.com/topics/data-analysis"),

            ("Exploratory Data Analysis",
             "https://github.com/topics/exploratory-data-analysis")
        ],

        "hours": 15
    },


    # ======================================================
    # MACHINE LEARNING
    # ======================================================

    "Machine Learning": {
        "description": "Learn how machines learn patterns from data.",

        "topics": [
            "Supervised Learning",
            "Unsupervised Learning",
            "Linear Regression",
            "Classification",
            "Decision Trees",
            "Model Evaluation"
        ],

        "resources": [
            ("Scikit-learn Documentation",
             "https://scikit-learn.org/stable/"),

            ("Google Machine Learning Crash Course",
             "https://developers.google.com/machine-learning/crash-course"),

            ("Kaggle Learn - Machine Learning",
             "https://www.kaggle.com/learn/intro-to-machine-learning"),

            ("Microsoft Machine Learning",
             "https://learn.microsoft.com/en-us/training/paths/create-machine-learn-models/")
        ],

        "projects": [
            ("House Price Prediction",
             "https://github.com/topics/house-price-prediction"),

            ("Titanic Machine Learning",
             "https://www.kaggle.com/competitions/titanic"),

            ("Spam Classifier",
             "https://github.com/topics/spam-classifier")
        ],

        "hours": 20
    },


    # ======================================================
    # DEEP LEARNING
    # ======================================================

    "Deep Learning": {
        "description": "Learn neural networks and deep learning concepts.",

        "topics": [
            "Neural Networks",
            "Activation Functions",
            "Backpropagation",
            "CNNs",
            "RNNs",
            "Model Training"
        ],

        "resources": [
            ("PyTorch Tutorials",
             "https://pytorch.org/tutorials/"),

            ("TensorFlow Tutorials",
             "https://www.tensorflow.org/tutorials"),

            ("DeepLearning.AI",
             "https://www.deeplearning.ai/"),

            ("Kaggle Deep Learning",
             "https://www.kaggle.com/learn/intro-to-deep-learning")
        ],

        "projects": [
            ("MNIST Digit Classification",
             "https://github.com/topics/mnist-classification"),

            ("Image Classification",
             "https://github.com/topics/image-classification"),

            ("CNN Projects",
             "https://github.com/topics/convolutional-neural-network")
        ],

        "hours": 25
    },


    # ======================================================
    # GENERATIVE AI
    # ======================================================

    "Generative AI": {
        "description": "Learn how modern AI systems generate text, images and other content.",

        "topics": [
            "Large Language Models",
            "Transformers",
            "Attention Mechanism",
            "Prompt Engineering",
            "Retrieval Augmented Generation",
            "AI Agents"
        ],

        "resources": [
            ("Hugging Face Learn",
             "https://huggingface.co/learn"),

            ("OpenAI Documentation",
             "https://platform.openai.com/docs/"),

            ("Google Generative AI",
             "https://ai.google.dev/"),

            ("DeepLearning.AI Generative AI",
             "https://www.deeplearning.ai/courses/generative-ai-with-llms/")
        ],

        "projects": [
            ("AI Chatbot Projects",
             "https://github.com/topics/ai-chatbot"),

            ("RAG Projects",
             "https://github.com/topics/retrieval-augmented-generation"),

            ("AI Agent Projects",
             "https://github.com/topics/ai-agents")
        ],

        "hours": 30
    }
}