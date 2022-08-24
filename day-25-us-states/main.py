import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
score = 0
correct_answers = []


while True:
    answer_state = screen.textinput(title=f"{score}/50", prompt="Next state:").title()
    if answer_state == "Exit":
        need_to_learn = [state for state in states if state not in correct_answers]
        new_data = pandas.DataFrame(need_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in states:
        score += 1
        correct_answers.append(answer_state)
        # states.remove(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()

        state_row = data[data.state == answer_state]
        x_cor = int(state_row.x)
        y_cor = int(state_row.y)
        t.goto(x_cor, y_cor)
        t.write(answer_state)

    # df = pandas.DataFrame(states)
    # df.to_csv("need_to_learn.csv")




screen.exitonclick()