from constraint import Constraint

class ExactProductConstraint(Constraint):

    def __init__(self, exactprod):
        self._exactprod = exactprod

    def preProcess(self, variables, domains, constraints, vconstraints):
        Constraint.preProcess(self, variables, domains, constraints, vconstraints)
        exactprod = self._exactprod
        for variable in variables:
            domain = domains[variable]
            for value in domain[:]:
                if value > exactprod:
                    if value > exactprod:
                        domain.remove(value)

    def __call__(self, variables, domains, assignments, forwardcheck=False):
        exactprod = self._exactprod
        prod = 1
        missing = False

        for variable in variables:
            if variable in assignments:
                prod *= assignments[variable]
            else: 
                missing = True
        if prod > exactprod:
            return False
        if forwardcheck and missing:
            for variable in variables:
                if variable not in assignments:
                    domain = domains[variable]
                    for value in domain[:]:
                        if prod * value > exactprod:
                            domain.hideValue(value)
                    if not domain:
                        return False
        if missing:
            return prod <= exactprod
        else:
            return prod == exactprod
        
        pass