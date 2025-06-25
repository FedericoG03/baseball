import flet as ft
from networkx.classes import neighbors


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
    def fillDD(self):
        for y in self._model.getAnni():
            self._view._ddAnno.options.append(ft.dropdown.Option(y))
        self._view.update_page()

    def handleDDYearSelection(self, e):
        anno = int(self._view._ddAnno.value)
        self._view._txtOutSquadre.controls.clear()
        for s in self._model.getSquadre(anno):
            self._view._txtOutSquadre.controls.append(ft.Text(f"{s.teamCode} ({s.name}"))
            self._view._ddSquadra.options.append(ft.dropdown.Option(s.name))
        self._view.update_page()

    def handleCreaGrafo(self, e):
        anno = int(self._view._ddAnno.value)
        self._model.buildGraph(anno)
        nodi,archi  = self._model.getDetailsGraph()
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(
            ft.Text(f"Grafo correttamente creato\nSono presenti {nodi} nodi e {archi} archi"))
        self._view.update_page()

    def handleDettagli(self, e):
        squadra = self._view._ddSquadra.value
        neighbors= self._model.getDettagli(squadra)
        self._view._txt_result.controls.clear()
        for n in neighbors:
            self._view._txt_result.controls.append(
                ft.Text(f"{n[0].name}   {n[1]}"))
        self._view.update_page()




    def handlePercorso(self, e):
        pass