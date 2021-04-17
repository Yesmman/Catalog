import json
import os
import pathlib
from dataclasses import dataclass
from typing import Callable

from pydantic import BaseModel

list_of_users = []
list_of_users_as_dict = []
list_of_movies = []


class Users(BaseModel):
    username: str
    movie_list: list


class Film(BaseModel):
    title: str
    year: int
    genre: str
    viewed: str = "No"

    def __str__(self):
        return f'{self.title} {self.year} {self.genre}'

    def __repr__(self):
        return str(self)


def add_new_films():
    with open(f'{list_of_users[u_choice].username}_film_list.json', 'a') as file_f:
        choice = int(input("How many films do you want to add? "))
        for obj in range(choice):
            obj = Film(
                title=input("Input title: "),
                year=input("Input year: "),
                genre=input("Input genre: "),
            )
            file_f.write(obj.json() + '\n')


def load_films():
    user = list_of_users[u_choice]

    with open(f'{user.username}_film_list.json', 'r') as file_f:
        for j, lines in enumerate(file_f):
            film_raw = json.loads(lines)

            film = Film.parse_raw(film_raw)

            user.movie_list.append(film)

            print(film)


def select_film():
    choice = int(input("What film do you want to select? "))
    print(list_of_users[u_choice].movie_list[choice].title,
          list_of_users[u_choice].movie_list[choice].viewed)
    print("Did you watch this movie? ")
    list_of_users[u_choice].movie_list[choice].viewed = input()
    with open(f'{list_of_users[u_choice].username}_film_list.json', 'w') as file_f:
        for obj in list_of_users[u_choice].movie_list:
            file_f.write(str(obj.json()) + '\n')


def add_new_users():
    path = pathlib.Path(__file__).parent.joinpath('storage', 'users.json')
    with open(path, 'a') as file:
        choice = int(input("How many users do you want to add? "))
        for obj in range(choice):
            obj = Users(movie_list=[], username=input())
            file.write(str(obj.json()) + '\n')


def load_users():
    with open(os.path.join('storage', 'users.json'), 'r') as file:
        for index, lines in enumerate(file):
            smt = dict(json.loads(lines))
            user = Users(movie_list=smt.get("movie_list"), username=smt.get("username"))
            list_of_users.append(user)

            print(f'{index} - {user.username}')


def select_user():
    return int(input("What user do you want to select? "))


def choice_movies_input():
    choice = -1
    while choice != 0:
        choice = int(input("What do you want to do?\n"
                           " 1 -- to add new films in the list\n"
                           " 2 -- to load the list of films\n"
                           " 3 -- to select film\n"
                           " 0 -- to exit\n"))
        if choice == 1:
            add_new_films()
        elif choice == 2:
            load_films()
        elif choice == 3:
            select_film()


@dataclass
class MenuItem:
    text: str
    action: Callable


def choice_user_input():
    choice = -1

    menu = [
        MenuItem(
            text='add new users',
            action=add_new_users,
        ),
        MenuItem(
            text='load the list of users',
            action=load_users,
        )
    ]

    while choice != 0:
        print("What do you want to do?")

        # choice = int(input("What do you want to do?\n"
        #                    " 1 -- to add new users,\n"
        #                    " 2 -- to load the list of users\n"
        #                    " 3 -- to select the user\n"
        #                    " 0 -- to exit\n"))
        for index, menu_item in enumerate(menu):
            print(f'{index} -- {menu_item.text}')

        choice = int(input())

        menu[choice].action()

        global u_choice

        # if choice == 1:
        #     add_new_users()
        # elif choice == 2:
        #     load_users()
        # elif choice == 3:
        #
        #     u_choice = select_user()
        #     choice_movies_input()


choice_user_input()
