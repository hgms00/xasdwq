import sys

from expert_system import Prompt, Tree, Print
from expert_system.parser.Parser import ESParser
from expert_system.config.Env import Env
from expert_system.config.Cmd import Cmd
from expert_system.util.Color import Color


def resolve_lines(parser):
    tree = Tree.NPITree(parser.structured_rules, parser.facts, parser.queries)
    results = {}
    for query in parser.queries:
        results[query] = tree.resolve_query(query)
        color = Color.GREEN if results[query] is True else Color.FAIL
        print(f"{ query } resolved as { color }{ results[query] }{ Color.END }")
    return results


questions = {
    'A': 'Você quer um computador para atividades pesadas(para trabalho e jogos)?',
    'B': 'JUREMA',
    'G': 'Tabata'
}

A = ['a', 'b', 'c']

def chatbot(parser):
    while(True):
        answer = input(questions[parser.atual_fact])

        if(answer=='SIM'):
            Prompt.ESPrompt(lines).do_add_fact('a')
            next = parser.atual_fact + parser.atual_fact.lower() + '+'
        else:
            next = parser.atual_fact + parser.atual_fact.lower() + '!+'

        for w in parser.structured_rules:
            if (next == w.npi_left):
                parser.atual_fact = w.npi_right

        if(answer == 'leave'):
            break


if __name__ == "__main__":
    args = Cmd.args

    try:
        with open(args.input) as f:
            lines = f.readlines()

            parser = ESParser(lines)
            chatbot(parser)

            res = resolve_lines(parser)


    except (Exception, BaseException) as e:
        print(e)
        sys.exit(1)
