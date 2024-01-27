from taipy.gui import Gui, navigate
# sidebar = '''
# <|Settings|button|>
# '''

home_pg = '''
<|menu|label=Menu|lov={page_names}|on_action=on_menu|>
#Home
<|layout|columns = 1 1|
    <|
<|Placeholder|button|>
    |>
    <|
<|Settings|button|>

<br />

<|Create a new group|button|>

<br />

<|Friends|button|>
    |>
|> 
'''