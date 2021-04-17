import json
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


def add_new_films():
    file_f = open(f'{list_of_users[u_choice].username}_film_list.json', 'a')
    choice = int(input("How many films do you want to add? "))
    for obj in range(choice):
        obj = Film(title=input("Input title: "), year=input("Input year: "), genre=input("Input genre: "))
        file_f.write(str(obj.json()) + '\n')
    file_f.close()


def load_films():
    file_f = open(f'{list_of_users[u_choice].username}_film_list.json', 'r')
    j = 0
    for lines in file_f:
        smt = dict(json.loads(lines))
        obj = Film(title=smt.get("title"), year=smt.get("year"), genre=smt.get("genre"))
        list_of_users[u_choice].movie_list.append(obj)
        print(list_of_users[u_choice].movie_list[j].title,
              list_of_users[u_choice].movie_list[j].year,
              list_of_users[u_choice].movie_list[j].genre)
        j += 1
    file_f.close()


def select_film():
    choice = int(input("What film do you want to select? "))
    print(list_of_users[u_choice].movie_list[choice].title,
          list_of_users[u_choice].movie_list[choice].viewed)
    print("Did you watch this movie? ")
    list_of_users[u_choice].movie_list[choice].viewed = input()
    file_f = open(f'{list_of_users[u_choice].username}_film_list.json', 'w')
    for obj in list_of_users[u_choice].movie_list:
        file_f.write(str(obj.json())+'\n')
    file_f.close()


def add_new_users():
    file = open('users.json', 'a')
    choice = int(input("How many users do you want to add? "))
    for obj in range(choice):
        obj = Users(movie_list=[], username=input())
        file.write(str(obj.json()) + '\n')
    file.close()


def load_users():
    file = open('users.json', 'r')
    i = 0
    for lines in file:
        smt = dict(json.loads(lines))
        obj = Users(movie_list=smt.get("movie_list"), username=smt.get("username"))
        list_of_users.append(obj)
        print(list_of_users[i].username)
        i += 1


def select_user():
    user_choice = int(input("What user do you want to select? "))
    return user_choice


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


def choice_user_input():
    choice = -1
    while choice != 0:
        choice = int(input("What do you want to do?\n"
                           " 1 -- to add new users,\n"
                           " 2 -- to load the list of users\n"
                           " 3 -- to select the user\n"
                           " 0 -- to exit\n"))
        if choice == 1:
            add_new_users()
        elif choice == 2:
            load_users()
        elif choice == 3:
            global u_choice
            u_choice = select_user()
            choice_movies_input()


choice_user_input()