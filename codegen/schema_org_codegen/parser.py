from __future__ import annotations

from pathlib import Path

from rdflib import Graph

from .vocabulary import Vocabulary


class Parser:
    def __init__(self, schema_file: str | Path = "codegen/data/schema.ttl") -> None:
        self.schema_file = Path(schema_file)
        self._graph: Graph | None = None
        self._vocabulary: Vocabulary | None = None

    @property
    def graph(self) -> Graph:
        if self._graph is None:
            self._graph = Graph()
            self._graph.parse(str(self.schema_file), format="turtle")
        return self._graph

    @property
    def subjects(self):
        if self._vocabulary is None:
            self._vocabulary = Vocabulary.from_graph(self.graph)
        return self._vocabulary.subjects

    def vocabulary(self) -> Vocabulary:
        if self._vocabulary is None:
            self._vocabulary = Vocabulary.from_graph(self.graph)
        return self._vocabulary


def parse(schema_file: str | Path) -> Vocabulary:
    return Parser(schema_file).vocabulary()
