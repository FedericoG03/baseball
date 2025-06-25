import itertools
from itertools import combinations

import networkx as nx
from networkx.classes import neighbors

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._idMap = {}

    def getAnni(self):
        return DAO.getAnni()

    def getSquadre(self,anno):
        return DAO.getSquadre(anno)

    def buildGraph(self, anno):
        self._graph.clear()
        for s in self.getSquadre(anno):
            self._idMap[s.ID] = s
        self._graph.add_nodes_from(self.getSquadre(anno))
        squadre = DAO.getEdges(anno, self._idMap)
        edges = list(itertools.combinations(self._graph.nodes(), 2))
        self._graph.add_edges_from(edges)

        for e in self._graph.edges:
            self._graph[e[0]][e[1]]["weight"] = squadre[e[0]] + squadre[e[1]]

    def _calcolaPeso(self, a, b, squadre):
        peso = 0
        for s in squadre:
            if s[0] == a or s[0] == b:
                peso += s[1]
        return peso

    def getDetailsGraph(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()

    def getDettagli(self,squadra):
        s = None
        for chiave, valore in self._idMap.items():
            if valore.name == squadra:
                s = self._idMap[chiave]
        vicini = self._graph.neighbors(s)

        viciniTuple = []

        for v in vicini:
            viciniTuple.append((v, self._graph[s][v]["weight"]))  # [(v0, p0) (v1, p1) ()]

        viciniTuple.sort(key=lambda x: x[1], reverse=True)

        return viciniTuple