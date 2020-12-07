# --- Day 7: Handy Haversacks ---

import re
#https://regex101.com/r/XdkbCj/1
rule_regex=re.compile(r'([a-z\s]+)\s(?:bags)\s(?:contain)((no other bags)|[a-z\s\d,]+)')

def parse_rules(rules:str)->dict:
    """Parse list of rules in dictionary of each bag and what they can carry

    Args:
        rules (str): The string containing all the rules, newline delimited

    Returns:
        dict: Dictionary of each bag and what they can carry
    """
    bags={}
    for rule in rules.split('\n'):
        matches=[s.strip() for s in rule_regex.findall(rule)[0] if s]
        outer_bag=matches[0]
        can_carry=(None if 'no other bags' in matches[1] else 
                    list(b.strip() for b in matches[1].split(',')))
        if can_carry is not None:
            can_carry={' '.join(b[1].split()[:2]):int(b[0]) for b in (c.split(None,1) for c in can_carry)}
        bags[outer_bag]=can_carry
        
    return bags

def valid_carrying_bags(rules:dict,bag_to_carry:str):
    direct_carriers=[]
    for bag,carriable in rules.items():
        if carriable and bag_to_carry in carriable:
            direct_carriers.append(bag)
    total_carriers=[]
    for carrier in direct_carriers:
        if carrier not in total_carriers:
            total_carriers+=valid_carrying_bags(rules,carrier)
    total_carriers+=direct_carriers
    return list(set(total_carriers))
    
def count_total_bags_inside(rules:dict,outer_bag:str):
    outer_bag_rule=rules[outer_bag]
    if outer_bag_rule is None:
        return 0
    bags_inside_current=sum([c for c in outer_bag_rule.values()])
    for bag,count in outer_bag_rule.items():
        bags_inside_current+=count_total_bags_inside(rules,bag)*count
    return bags_inside_current


# test="""light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags."""
# rules=parse_rules(test)

#Part 1
rules_text=''
with open('./day7_bagrules.txt','r') as f:
    rules_text=f.read()

rules=parse_rules(rules_text)
carried_eventually_by=valid_carrying_bags(rules,'shiny gold')
print(len(carried_eventually_by))

#Part 2
total_bags_inside=count_total_bags_inside(rules,'shiny gold')
print(total_bags_inside)