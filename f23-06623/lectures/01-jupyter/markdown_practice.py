import os
import json
import ipywidgets as widgets
import functools


def load_state():
    if os.path.exists("state.json"):
        return json.load(open("state.json"))
    else:
        return {}


def save_state(state):
    with open("state.json", "w") as f:
        f.write(json.dumps(state))


state = load_state()

questions = [
    {

        "question":  "What is the correct way to make text bold in markdown?",
        "answer": ["*text*", "**text**", '<text style="bold">text</text>']
    },
    {
           "question": "What is the correct way to make italics text in markdown?",
        "answer": ["*text*", "**text**", '<text style="italic">text</text>']
    },
    {
        "question": "Which is a level 3 heading in Markdown?",
        "answer": ['#3 heading title', '### headingtitle', '*** heading title']
    },
    {
        'question': 'How do you represent this equation $\int_0^x e^x$? in Markdown',
        'answer': ['int 0 x e(x)',
                  '¯\_(ツ)_/¯',
                  '$\int_0^x e^x$']
    },
    {
     'question': 'What is the syntax for a link in Markdown?',
        'answer': ['[text](url)',
                   '(text)[url]',
                   '[[url]]']              
    }
]


out = widgets.Output()

def on_value_change(change, qid):
    state[qid] = change["new"]
    save_state(state)
    with out:
        print(state)

for i, q in enumerate(questions):
       
    pieces = [ widgets.HTMLMath(q['question']),
                widgets.RadioButtons(options=q['answer'],
                                    layout={"width": "max-content"},  
                                    description="Answer:",
                                    value=state.get(str(i), None))
              ]
    
    pieces[1].observe(functools.partial(on_value_change, qid=i), names="value")
               
    display(widgets.VBox(pieces))
    
        

