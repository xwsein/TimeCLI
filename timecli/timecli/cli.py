
### cli.py
import click
from .task_manager import add_task, edit_task, delete_task, list_tasks, schedule_day
from .reminder import set_reminder
from .timer import start_pomodoro

@click.group()
def cli():
    """🕒 timecli: Time Management CLI Tool"""
    pass

@cli.group()
def task():
    """Manage your tasks"""
    pass

@task.command()
@click.argument('title')
@click.option('--due', help='Due date/time for the task (e.g. "2025-07-30 14:00")')
def add(title, due):
    add_task(title, due)

@task.command()
@click.argument('task_id', type=int)
@click.option('--title', help='New title')
@click.option('--due', help='New due date/time')
def edit(task_id, title, due):
    edit_task(task_id, title, due)

@task.command()
@click.argument('task_id', type=int)
def delete(task_id):
    delete_task(task_id)

@task.command(name="list")
def list_():
    list_tasks()

@cli.command()
@click.argument('start_time')
@click.argument('date')
@click.argument('title_duration', nargs=-1)
def plan(start_time, date, title_duration):
    schedule_day(start_time, date, list(title_duration))

@cli.command()
@click.argument('message')
@click.option('--at', help='Time to remind (e.g. "15:30" or "now")')
def remind(message, at):
    set_reminder(message, at)

@cli.command()
@click.argument('title')
@click.option('--work', default=25)
@click.option('--break_', 'break_time', default=5)
@click.option('--rounds', default=4)
def pomodoro(title, work, break_time, rounds):
    start_pomodoro(title, work, break_time, rounds)