from hal2cff import hal2cff
import ipywidgets as widgets

# # hal2cff example

adresse = "https://hal.archives-ouvertes.fr/hal-01361430v1"

text_widget = widgets.Text(
    value='https://hal.archives-ouvertes.fr/',
    placeholder='Type something',
    description='String:',
    disabled=False
)

text_widget

button = widgets.Button(
    description='Click me',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Click me',
    icon='check' # (FontAwesome names without the `fa-` prefix)
)

out = widgets.Output(layout={'border': '1px solid black'})


def display_html(button):
    txt = text_widget.get_state()["value"]
    prefix = "https://hal.archives-ouvertes.fr/"
    if txt[:len(prefix)] == prefix:
        with out:
            print(hal2cff(txt))


button.on_click(display_html)

button

out


