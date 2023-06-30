"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config
from functools import partial
from collections import namedtuple
import json
import reflex as rx

title = "Reflex Showcase"

Route = namedtuple("Route", ["route", "link"])
routes = [
    Route("page/[arg]", "page/1"),
    Route("page/[arg]/[...slug]", "page/1/2/3"),
    Route("page2/[my_arg]", "page2/1"),
]

WIDTH="80vw"
SUBWIDTH="50vw"
HEIGHT="70vh"
FULL_HEIGHT="100vh"

class State(rx.State):
    """The app state."""

    show: bool = False
    alertdialog_show: bool = False
    drawer_show: bool = False
    modal_show: bool = False
    popover_show: bool = False


class RouteState(State):
    @rx.var
    def show_args(self):
        return json.dumps(self.get_query_params())


def case(label_, item):
    return rx.hstack(
        label(label_), rx.spacer(), rx.center(item, width="20vw"), width=SUBWIDTH
    )


def label(text):
    return rx.center(rx.text(text), width="8vw")

md_example = """##Some markdown
        
some text
"""

def typography():
    return rx.vstack(
        case("rx.Text", rx.text("Some text")),
        case("rx.Heading", rx.heading("A big title", size="lg")),
        case(
            "rx.Span",
            rx.box(rx.span("Some", color="red"), rx.span("span", color="blue")),
        ),
        case("rx.Markdown", rx.markdown(md_example)),
    )


def forms():
    options = ["Option1", "Option2"]
    return rx.vstack(
        case("Button", rx.button("A button")),
        case("Checkbox", rx.checkbox("Check me!")),
        case(
            "Input + Form Control",
            rx.form_control(
                label="FormControl label",
                input=rx.input(),
                help_text="A very helpful note",
                error_message="A very angry ERROR message",
                is_required=True,
            ),
        ),
        case("NumberInput", rx.number_input()),
        case("Pin Input", rx.pin_input(length=3)),
        case("Select", rx.select(options)),
        case("RadioGroup", rx.radio_group(options)),
        case("Slider", rx.slider()),
        case("RangeSlider", rx.range_slider()),
        case("Switch", rx.switch()),
        case(
            "Editable",
            rx.editable(
                rx.editable_preview(),
                rx.editable_input(),
                placeholder="Editable example...",
                width="100%",
            ),
        ),
        case("TextArea", rx.text_area()),
    )


def layout():
    list_ = ["1", "2", "3", "4"]
    return rx.vstack(
        case("Box", rx.box(width="250px", height="40px", bg="black")),
        case(
            "Center",
            rx.center(rx.text("."), width="250px", height="40px", border="black solid"),
        ),
        case(
            "Cond",
            rx.box(
                rx.switch(on_change=State.set_show),
                rx.cond(~State.show, rx.text("Item1"), rx.text("Item2")),
            ),
        ),
        case(
            "Container",
            rx.container(
                rx.box(width="100px", height="40px", bg="gray"),
                width="250px",
                center_content=True,
                bg="black",
            ),
        ),
        case(
            "Flex",
            rx.flex(
                rx.square("Component", bg="red"),
                rx.box("box", width="50px", bg="green"),
                width="250px",
                border="green solid",
                height="40px",
            ),
        ),
        case(
            "Foreach",
            rx.center(
                rx.foreach(
                    list_,
                    lambda id: rx.box(
                        id, width="40px", height="40px", bg="gray", border="black solid"
                    ),
                ),
            ),
        ),
        case(
            "Grid",
            rx.grid(
                rx.grid_item(row_span=1, col_span=2, bg="lightblue"),
                rx.grid_item(row_span=1, col_span=2, bg="yellow"),
                rx.grid_item(row_span=1, col_span=1, bg="lightgreen"),
                rx.grid_item(row_span=2, col_span=1, bg="orange"),
                rx.grid_item(row_span=1, col_span=1, bg="purple"),
                template_rows="repeat(2, 1fr)",
                template_columns="repeat(5, 1fr)",
                height="40px",
                width="250px",
            ),
        ),
        case(
            "ResponsiveGrid",
            rx.responsive_grid(
                rx.box(height="40px", width="40px", bg="lightgreen"),
                rx.box(height="40px", width="40px", bg="lightblue"),
                rx.box(height="40px", width="40px", bg="purple"),
                rx.box(height="40px", width="40px", bg="tomato"),
                rx.box(height="40px", width="40px", bg="orange"),
                rx.box(height="40px", width="40px", bg="yellow"),
                columns=[3],
                spacing="2",
            ),
        ),
        # case("Wrap", rx.wrap(items=[rx.box("."), rx.box(".")])),
    )


def navigation():
    return rx.vstack(
        case(
            "Breadcrumb",
            rx.breadcrumb(items=[("Home", "/"), ("Page", "/")]),
        ),
        case(
            "Link",
            rx.link("Awesome link to ... here", href="/"),
        ),
    )

code_fib = """def fib(n):
    if n <= 1:
        return n
    else:
        return(fib(n-1) + fib(n-2))
"""

def data_display():
    list_ = ["Example 1", "Example 2"]
    return rx.vstack(
        case("Badge", rx.badge("Some badge")),
        case(
            "CodeBlock",
            rx.code_block(
                code_fib,
                language="python",
                can_copy=True,
                show_line_numbers=True,
            ),
        ),
        case(
            "Divider",
            rx.center(
                rx.text("Before"),
                rx.divider(),
                rx.text("After"),
                width="250px",
                heigh="40px",
            ),
        ),
        case(
            "DataTable",
            rx.data_table(data=[[1, 2], ["A", "B"]], columns=["a", "b"]),
        ),
        case(
            "List",
            rx.list(
                items=list_,
            ),
        ),
        case(
            "Unordered List",
            rx.unordered_list(
                items=list_,
            ),
        ),
        case(
            "Ordered List",
            rx.ordered_list(
                items=list_,
            ),
        ),
        case(
            "Stat",
            rx.center(
                rx.stat(
                    label="A stat", number=50, help_text="25%", arrow_type="increase"
                )
            ),
        ),
        case(
            "Table",
            rx.table(
                caption="BIG CAPTION",
                headers=["Name", "Age"],
                rows=[("John", 30), ("Jeanne", "50")],
                footers=["F1", "F2"],
            ),
        ),
    )


def graphing():
    return rx.vstack()


def disclosure():
    _items = [("Label1", rx.center("Panel1")), ("Label2", rx.center("Panel2"))]
    return rx.vstack(
        case("Accordion", rx.accordion(items=_items)),
        case("Tabs", rx.tabs(items=_items)),
    )


def feedback():
    return rx.vstack(
        case("Alert", rx.alert(status="error", title="Some title")),
        case("Circular progress", rx.circular_progress(is_indeterminate=True)),
        case("Progress Bar", rx.progress(is_indeterminate=True, width="100%")),
        case(
            "Skeleton",
            rx.vstack(
                rx.hstack(
                    rx.skeleton_circle(),
                    rx.skeleton(height="10px", width="100px", is_loaded=False),
                ),
                rx.skeleton_text(no_of_lines=3, is_loaded=False, width="150px"),
            ),
        ),
        case("Spinner", rx.center(rx.spinner())),
    )


def media():
    return rx.vstack(
        case(
            "Avatar",
            rx.tooltip(rx.avatar(name=title), label=title),
        ),
        case(
            "Image",
            rx.image(
                src="/black.png",
                # fallback="add black.png in your assets folder if image doesn't show up",
            ),
        ),
        case(
            "Icon",
            rx.hstack(
                rx.icon(tag="moon"),
                rx.icon(tag="add"),
                rx.icon(tag="sun"),
                rx.icon(tag="arrow_forward"),
                rx.icon(tag="star"),
            ),
        ),
    )


def overlay():
    return rx.vstack(
        case(
            "AlertDialog",
            rx.center(
                rx.button(
                    "Open AlertDialog",
                    on_click=partial(State.set_alertdialog_show, True),
                ),
                rx.alert_dialog(
                    header="Confirm?",
                    body="Are you suuure you want to confirm? No take back!",
                    footer=rx.button(
                        "Confirm", on_click=partial(State.set_alertdialog_show, False)
                    ),
                    on_close=partial(State.set_alertdialog_show, False),
                    is_open=State.alertdialog_show,
                ),
            ),
        ),
        case(
            "Drawer",
            rx.center(
                rx.button("Open Drawer", on_click=partial(State.set_drawer_show, True)),
                rx.drawer(
                    header="Big Drawer",
                    body="Yes it's a drawer, what else did you expect?",
                    footer=rx.button(
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
            rx.menu(
                button=rx.icon(tag="hamburger"),
                items=[
                    rx.menu_item("Menu Item 1"),
                    rx.menu_item("Menu Item 2"),
                    rx.menu_divider(),
                    rx.menu_item("Menu Item 3"),
                ],
            ),
        ),
        case(
            "Modal",
            rx.center(
                rx.button("Open Modal", on_click=partial(State.set_modal_show, True)),
                rx.modal(
                    header="A Modal",
                    body="Body of the Modal",
                    footer=rx.button(
                        "Confirm Modal", on_click=partial(State.set_modal_show, False)
                    ),
                    on_close=partial(State.set_modal_show, False),
                    is_open=State.modal_show,
                ),
            ),
        ),
        case(
            "Popover",
            rx.center(
                rx.popover(
                    trigger=rx.button(
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
            rx.tooltip(rx.text("Some text"), label="with a tooltip"),
        ),
    )


def other():
    return rx.vstack(case("HTML", rx.html("<div>Some basic HTML</div>")))


def basic_showcase():
    return rx.tabs(
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
        allow_toggle=True,
        width=WIDTH,
    )


def full_showcase():
    return rx.tabs(
        items=[
            ("Basic Components", basic_showcase()),
            (
                "Complex Components",
                rx.box(
                    "TODO: add 'complex components', ",
                    "meaning components built from ",
                    "assembling basic components together",
                ),
            ),
            (
                "Routes",
                rx.hstack(
                    # foreach doesn't work
                    # rx.foreach(routes, lambda route: rx.link(route.route, href=route.link))
                    # unpacking the list comprehension work
                    *[rx.link(route.route, href=route.link) for route in routes]
                ),
            ),
        ],
        width=WIDTH,
        height=HEIGHT,
    )


def frame(body):
    return rx.center(
        rx.vstack(
            rx.hstack(
                rx.heading(title, margin="15px"),
                rx.icon(tag="sun", on_click=rx.toggle_color_mode),
            ),
            body,
        ),
        height=FULL_HEIGHT,
    )


def index():
    return frame(full_showcase())


def index2():
    return frame(
        rx.vstack(
            rx.hstack(rx.link(rx.icon(tag="arrow_left"), "Return", href="/")),
            rx.text(
                "You can change the parameters in the url, they will show up on the page"
            ),
            rx.text(RouteState.show_args),
        )
    )


# Add state and page to the app.
app = rx.App(state=State)
app.add_page(index, title="Reflex Showcase")
for route in routes:
    app.add_page(index2, route=route.route)
app.compile()
