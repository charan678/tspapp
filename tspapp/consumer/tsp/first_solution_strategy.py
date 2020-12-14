from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

from tspapp.consumer.tsp.tsp import TSP
from tspapp import logger
from tspapp.consumer.tsp.vehical import Vehical

class FirstSolutionStrategy(TSP):
    def __init__(self, vehical: Vehical):
        self.vehical = vehical
        self.data['locations'] = vehical.locations
        self.data['num_vehicles'] = 1
        self.data['depot'] = 0

    def _print_solution(self, manager, routing, solution):
        logger.info('Objective: {}'.format(solution.ObjectiveValue()))
        index = routing.Start(0)
        plan_output = 'Route:\n'
        route_distance = 0
        while not routing.IsEnd(index):
            plan_output += ' {} ->'.format(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
        plan_output += ' {}\n'.format(manager.IndexToNode(index))
        logger.info(plan_output)
        plan_output += 'Objective: {}m\n'.format(route_distance)

    def find_shortest_path(self):
        manager = pywrapcp.RoutingIndexManager(len(self.data['locations']),
                                               self.data['num_vehicles'], self.data['depot'])
        routing = pywrapcp.RoutingModel(manager)
        distance_matrix = self.vehical.eular_distance_locations()

        def distance_callback(from_index, to_index):
            from_node = manager.IndexToNode(from_index)
            to_node = manager.IndexToNode(to_index)
            return distance_matrix[from_node][to_node]

        transit_callback_index = routing.RegisterTransitCallback(distance_callback)
        routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)
        search_parameters = pywrapcp.DefaultRoutingSearchParameters()
        search_parameters.first_solution_strategy = (
            routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
        solution = routing.SolveWithParameters(search_parameters)

        if solution:
            self._print_solution(manager, routing, solution)
        return solution