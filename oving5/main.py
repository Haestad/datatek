from fsm import Rule, FSM
from kpc import KPC

agent = KPC()
fsm = FSM(agent)

rules_list = [
    Rule('S-init', 'S-Read', Rule.signal_is_any, agent.reset_passcode_entry),
    Rule('S-Read', 'S-Read', Rule.signal_is_digit, agent.append_next_password_digit),
    Rule('S-Read', 'S-Verify', '*', agent.verify_login),
    Rule('S-Read', 'S-init', Rule.signal_is_any, agent.reset_agent),
    Rule('S-Verify', 'S-Active', 'Y', agent.fully_activate_agent),
    Rule('S-Verify', 'S-init', 'N', agent.reset_agent),
    Rule('S-Active', 'S-Read-2', '*', agent.reset_agent),
    Rule('S-Active', 'S-led', Rule.signal_is_pin, agent.select_pin),
    Rule('S-led', 'S-dur', '*', agent.reset_agent),
    Rule('S-led', 'S-led', Rule.signal_is_pin, agent.select_pin),
    Rule('S-led', 'S-Active', Rule.signal_is_any, agent.reset_agent),
    Rule('S-dur', 'S-dur', Rule.signal_is_digit, agent.append_dur),
    Rule('S-dur', 'S-Active', '*', agent.light_one_led),
    Rule('S-dur', 'S-Active', Rule.signal_is_any, agent.reset_agent()),
    Rule('S-Read-2', 'S-Read-2', Rule.signal_is_digit, agent.append_next_password_digit),
    Rule('S-Read-2', 'S-Validate', '*', agent.validate_password_change),
    Rule('S-Read-2', 'S-Active', Rule.signal_is_any, agent.reset_agent),
    Rule('S-Validate', 'S-Active', Rule.signal_is_any, agent.reset_agent),
    Rule('S-Active', 'S-end', '#', agent.exit_action)
]
for rule in rules_list:
    fsm.add_rule(rule)

fsm.run()
