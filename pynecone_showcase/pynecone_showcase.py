"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config
from functools import partial

import pynecone as pc

title = "Pynecone Showcase"


class State(pc.State):
    """The app state."""

    show: bool = False
    alertdialog_show: bool = False
    drawer_show: bool = False
    modal_show: bool = False
    popover_show: bool = False


def case(label_, item):
    return pc.hstack(
        label(label_), pc.spacer(), pc.center(item, width="12vw"), width="22vw"
    )


def label(text):
    return pc.center(pc.text(text), width="8vw")


def typography():
    return pc.vstack(
        case("pc.Text", pc.text("Some text")),
        case("pc.Heading", pc.heading("A big title", size="lg")),
        case(
            "pc.Span",
            pc.box(pc.span("Some", color="red"), pc.span("span", color="blue")),
        ),
        case("pc.Markdown", pc.markdown("##Some markdown")),
    )


def forms():
    options = ["Option1", "Option2"]
    return pc.vstack(
        case("Button", pc.button("A button")),
        case("Checkbox", pc.checkbox("Check me!")),
        case(
            "Input + Form Control",
            pc.form_control(
                label="FormControl label",
                input=pc.input(),
                help_text="A very helpful note",
                error_message="A very angry ERROR message",
                is_required=True,
            ),
        ),
        case("NumberInput", pc.number_input()),
        case("Pin Input", pc.pin_input(length=3)),
        case("Select", pc.select(options)),
        case("RadioGroup", pc.radio_group(options)),
        case("Slider", pc.slider()),
        case("RangeSlider", pc.range_slider()),
        case("Switch", pc.switch()),
        case(
            "Editable",
            pc.editable(
                pc.editable_preview(),
                pc.editable_input(),
                placeholder="Editable example...",
                width="100%",
            ),
        ),
        case("TextArea", pc.text_area()),
    )


def layout():
    list_ = ["1", "2", "3", "4"]
    return pc.vstack(
        case("Box", pc.box(width="250px", height="40px", bg="black")),
        case(
            "Center",
            pc.center(pc.text("."), width="250px", height="40px", border="black solid"),
        ),
        case(
            "Cond",
            pc.box(
                pc.switch(on_change=State.set_show),
                pc.cond(~State.show, pc.text("Item1"), pc.text("Item2")),
            ),
        ),
        case(
            "Container",
            pc.container(
                pc.box(width="100px", height="40px", bg="gray"),
                width="250px",
                center_content=True,
                bg="black",
            ),
        ),
        case(
            "Flex",
            pc.flex(
                pc.square("Component", bg="red"),
                pc.box("box", width="50px", bg="green"),
                width="250px",
                border="green solid",
                height="40px",
            ),
        ),
        case(
            "Foreach",
            pc.center(
                pc.foreach(
                    list_,
                    lambda id: pc.box(
                        id, width="40px", height="40px", bg="gray", border="black solid"
                    ),
                ),
            ),
        ),
        case(
            "Grid",
            pc.grid(
                pc.grid_item(row_span=1, col_span=2, bg="lightblue"),
                pc.grid_item(row_span=1, col_span=2, bg="yellow"),
                pc.grid_item(row_span=1, col_span=1, bg="lightgreen"),
                pc.grid_item(row_span=2, col_span=1, bg="orange"),
                pc.grid_item(row_span=1, col_span=1, bg="purple"),
                template_rows="repeat(2, 1fr)",
                template_columns="repeat(5, 1fr)",
                height="40px",
                width="250px",
            ),
        ),
        case(
            "ResponsiveGrid",
            pc.responsive_grid(
                pc.box(height="40px", width="40px", bg="lightgreen"),
                pc.box(height="40px", width="40px", bg="lightblue"),
                pc.box(height="40px", width="40px", bg="purple"),
                pc.box(height="40px", width="40px", bg="tomato"),
                pc.box(height="40px", width="40px", bg="orange"),
                pc.box(height="40px", width="40px", bg="yellow"),
                columns=[3],
                spacing="2",
            ),
        ),
        # case("Wrap", pc.wrap(items=[pc.box("."), pc.box(".")])),
    )


def navigation():
    return pc.vstack(
        case(
            "Breadcrumb",
            pc.breadcrumb(items=[("Home", "/"), ("Page", "/")]),
        ),
        case(
            "Link",
            pc.link("Awesome link to ... here", href="/"),
        ),
    )


def data_display():
    list_ = ["Example 1", "Example 2"]
    return pc.vstack(
        case("Badge", pc.badge("Some badge")),
        case(
            "CodeBlock",
            pc.code_block(
                """def fib(n):
    if n <= 1:
        return n
    else:
        return(fib(n-1) + fib(n-2))""",
                language="python",
                show_line_numbers=True,
            ),
        ),
        case(
            "Divider",
            pc.center(
                pc.text("Before"),
                pc.divider(),
                pc.text("After"),
                width="250px",
                heigh="40px",
            ),
        ),
        case(
            "DataTable",
            pc.data_table(data=[[1, 2], ["A", "B"]], sort=True),
        ),
        case(
            "List",
            pc.list(
                items=list_,
            ),
        ),
        case(
            "Unordered List",
            pc.unordered_list(
                items=list_,
            ),
        ),
        case(
            "Ordered List",
            pc.ordered_list(
                items=list_,
            ),
        ),
        case(
            "Stat",
            pc.center(
                pc.stat(
                    label="A stat", number=50, help_text="25%", arrow_type="increase"
                )
            ),
        ),
        case(
            "Table",
            pc.table(
                caption="BIG CAPTION",
                headers=["Name", "Age"],
                rows=[("John", 30), ("Jeanne", "50")],
                # footers=["F1", "F2"],
            ),
        ),
    )


def graphing():
    return pc.vstack()


def disclosure():
    _items = [("Label1", pc.center("Panel1")), ("Label2", pc.center("Panel2"))]
    return pc.vstack(
        case("Accordion", pc.accordion(items=_items)),
        case("Tabs", pc.tabs(items=_items)),
    )


def feedback():
    return pc.vstack(
        case("Alert", pc.alert(status="error", title="Some title")),
        case("Circular progress", pc.circular_progress(is_indeterminate=True)),
        case("Progress Bar", pc.progress(is_indeterminate=True, width="100%")),
        case(
            "Skeleton",
            pc.vstack(
                pc.hstack(
                    pc.skeleton_circle(),
                    pc.skeleton(height="10px", width="100px", is_loaded=False),
                ),
                pc.skeleton_text(no_of_lines=3, is_loaded=False, width="150px"),
            ),
        ),
        case("Spinner", pc.center(pc.spinner())),
    )


def media():
    return pc.vstack(
        case(
            "Avatar",
            pc.tooltip(pc.avatar(name=title), label=title),
        ),
        case("Image", pc.image(src="/black.png")),
        case(
            "Icon",
            pc.hstack(
                pc.icon(tag="MoonIcon"),
                pc.icon(tag="AddIcon"),
                pc.icon(tag="SunIcon"),
                pc.icon(tag="ArrowForwardIcon"),
                pc.icon(tag="StarIcon"),
            ),
        ),
    )


def overlay():
    return pc.vstack(
        case(
            "AlertDialog",
            pc.center(
                pc.button(
                    "Open AlertDialog",
                    on_click=partial(State.set_alertdialog_show, True),
                ),
                pc.alert_dialog(
                    header="Confirm?",
                    body="Are you suuure you want to confirm? No take back!",
                    footer=pc.button(
                        "Confirm", on_click=partial(State.set_alertdialog_show, False)
                    ),
                    on_close=partial(State.set_alertdialog_show, False),
                    is_open=State.alertdialog_show,
                ),
            ),
        ),
        case(
            "Drawer",
            pc.center(
                pc.button("Open Drawer", on_click=partial(State.set_drawer_show, True)),
                pc.drawer(
                    header="Big Drawer",
                    body="Yes it's a drawer, what else did you expect?",
                    footer=pc.button(
                        "I wasted my time",
                        on_click=partial(State.set_drawer_show, False),
                    ),
                    on_close=partial(State.set_drawer_show, False),
                    is_open=State.drawer_show,
                ),
            ),
        ),
        case(
            "Menu",
            pc.menu(
                button=pc.icon(tag="HamburgerIcon"),
                items=[
                    pc.menu_item("Menu Item 1"),
                    pc.menu_item("Menu Item 2"),
                    pc.menu_divider(),
                    pc.menu_item("Menu Item 3"),
                ],
            ),
        ),
        case(
            "Modal",
            pc.center(
                pc.button("Open Modal", on_click=partial(State.set_modal_show, True)),
                pc.modal(
                    header="A Modal",
                    body="Body of the Modal",
                    footer=pc.button(
                        "Confirm Modal", on_click=partial(State.set_modal_show, False)
                    ),
                    on_close=partial(State.set_modal_show, False),
                    is_open=State.modal_show,
                ),
            ),
        ),
        case(
            "Popover",
            pc.center(
                pc.popover(
                    trigger=pc.button(
                        "Open Popover", on_click=partial(State.set_popover_show, True)
                    ),
                    header="Popover header",
                    body="It's a popover, nothing to see.",
                    footer="Popover footer",
                    use_close_button=True,
                    on_close=partial(State.set_popover_show, False),
                    is_open=State.popover_show,
                ),
            ),
        ),
        case(
            "Tooltip",
            pc.tooltip(pc.text("Some text"), label="with a tooltip"),
        ),
    )


def other():
    return pc.vstack(case("HTML", pc.html("<div>Some basic HTML</div>")))


def basic_showcase():
    return pc.accordion(
        items=[
            ("Typography", typography()),
            ("Forms", forms()),
            ("Layout", layout()),
            ("Navigation", navigation()),
            ("DataDisplay", data_display()),
            ("Graphing", graphing()),
            ("Disclosure", disclosure()),
            ("Feedback", feedback()),
            ("Media", media()),
            ("Overlay", overlay()),
            ("Other", other()),
        ],
        width="30vw",
    )


def index():
    return pc.center(
        pc.vstack(
            pc.hstack(
                pc.heading(title, margin="15px"),
                pc.icon(tag="SunIcon", on_click=pc.toggle_color_mode),
            ),
            pc.tabs(
                items=[
                    ("Basic Components", basic_showcase()),
                    (
                        "Complex Components",
                        pc.box(
                            "TODO: add 'complex components', ",
                            "meaning components built from ",
                            "assembling basic components together",
                        ),
                    ),
                ],
                width="30vw",
                height="70vh",
            ),
        ),
        height="100vh",
    )


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index, image="/bl.png")
app.compile()
