# ==========================================================
# LEARNGRAPH AI - GRAPH ENGINE
# ==========================================================

import networkx as nx

from data import SKILLS, PREREQUISITES


# ----------------------------------------------------------
# CREATE KNOWLEDGE GRAPH
# ----------------------------------------------------------

def create_graph():

    graph = nx.Graph()

    # Add all skills as nodes
    graph.add_nodes_from(SKILLS)

    # Add relationships as edges
    for item in PREREQUISITES:

        if not isinstance(item, (tuple, list)) or len(item) != 2:

            raise ValueError(
                f"Invalid prerequisite entry: {item!r}"
            )

        prerequisite, skill = item

        if prerequisite not in SKILLS:

            raise ValueError(
                f"Unknown prerequisite skill: {prerequisite}"
            )

        if skill not in SKILLS:

            raise ValueError(
                f"Unknown target skill: {skill}"
            )

        graph.add_edge(
            prerequisite,
            skill
        )

    return graph


# ----------------------------------------------------------
# GENERATE LEARNING PATH
# ----------------------------------------------------------

def generate_learning_path(current_skill, target_skill):

    graph = create_graph()

    # Check starting skill
    if current_skill not in graph:
        return []

    # Check target skill
    if target_skill not in graph:
        return []

    # Same skill
    if current_skill == target_skill:
        return [current_skill]

    try:

        path = nx.shortest_path(
            graph,
            source=current_skill,
            target=target_skill
        )

        return path

    except nx.NetworkXNoPath:

        return []

    except nx.NodeNotFound:

        return []