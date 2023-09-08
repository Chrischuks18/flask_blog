from dotenv import dotenv_values

ENV = dotenv_values()

SECRET_KEY = ENV["SECRET_KEY"]
