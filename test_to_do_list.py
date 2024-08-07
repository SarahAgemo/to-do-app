import pytest
from to_do_list import add_task, tasks, list_tasks


def test_add_task(monkeypatch):
    task = "Go shopping"
    monkeypatch.setattr("builtins.input", lambda _: task)
    add_task()
    assert task in tasks
    assert tasks[-1] == task


def test_list_tasks_no_tasks(capfd):
    # Arrange
    tasks.clear()  # Ensure tasks list is empty

    # Act
    list_tasks()

    # Assert
    captured = capfd.readouterr()
    assert captured.out == "There are no tasks currently.\n"


def test_list_tasks_with_tasks(capfd, monkeypatch):
    # Arrange
    tasks.clear()  # Ensure tasks list is empty
    task = "Go shopping"
    monkeypatch.setattr("builtins.input", lambda _: task)
    add_task()

    # Act
    list_tasks()

    # Assert
    captured = capfd.readouterr()
    # Split the captured output to separate add_task() print from list_tasks() print
    captured_output = captured.out.split("\n", 1)[
        1
    ]  # Remove the first line from add_task

    expected_output = "Current Tasks:\n" "Task #0. Go shopping\n"
    assert captured_output == expected_output
