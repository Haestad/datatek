""" This module contains the classes necessary for the Finite State Machine (FSM).
    That includes the FSM itself, as well as the Rule class, because the FSM is
    a Rule Based System (RBS) """
from inspect import isfunction


class FSM:
    """ This class contains the Finite State Machine (FSM). """

    def __init__(self, agent):
        self.rule_list = []
        self.agent = agent
        self.state = None

    def add_rule(self, rule):
        """ Adds a rule to the end of the rule list. """
        if isinstance(rule, Rule):
            self.rule_list.append(rule)

    def get_next_signal(self):
        """ Queries the agent for the next signal. """
        return self.agent.get_next_signal()

    def run(self):
        """ Starts the FSM in default state, and then
            repeatedly calls get_next_signal until the FSM reaches its final state. """
        self.state = 'S-init'
        while self.state != 'S-end':
            self.match_rule(self.get_next_signal())

    def match_rule(self, signal):
        """ Checks for the first fulfilled rule with the given signal.
            If a rule is found, that rule is fired. """
        for rule in self.rule_list:
            if rule.match(self.state, signal):
                rule.fire(self, self.agent)
                return


class Rule:
    """ This class contains a rule used by the Rule Based System (RBS). """

    def __init__(self, state1, state2, signal, action):
        self.state1 = state1
        self.state2 = state2
        self.signal = signal
        self.action = action

    def match(self, state, signal):
        """ Checks whether the rule condition is fulfilled. """
        if state == self.state1:
            if signal == self.signal:
                return True
            if isfunction(self.signal):
                return self.signal(signal)
        return False

    def fire(self, fsm, agent):
        """ Uses the consequent of a rule to set the next state of the FSM,
            and calls the appropriate agent action method. """
        fsm.state = self.state2
        agent.do_action(self.action)

    @staticmethod
    def signal_is_any(signal):
        """ Returns True, used when rule is accepting any signal. """
        return True

    @staticmethod
    def signal_is_digit(signal):
        """ Returns True if the signal is a digit between 0-9. """
        return 48 <= ord(str(signal)) <= 57

    @staticmethod
    def signal_is_pin(signal):
        """ Returns True if the signal is a digit between 0-5. """
        return 48 <= ord(str(signal)) <= 53
