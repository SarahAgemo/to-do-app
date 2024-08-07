import pytest
from to_do_list import add_task, delete_task, tasks, list_tasks


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


def test_delete_task_success(monkeypatch, capfd):
    # Arrange
    tasks.clear()  # Ensure tasks list is empty
    tasks.append("Go shopping")
    tasks.append("Clean the house")

    # Mock input to delete the first task
    monkeypatch.setattr("builtins.input", lambda _: "0")

    # Act
    delete_task()

    # Assert
    captured = capfd.readouterr()
    assert "Task 0 has been removed." in captured.out
    assert len(tasks) == 1
    assert tasks[0] == "Clean the house"


def test_delete_task_invalid_index(monkeypatch, capfd):
    # Arrange
    tasks.clear()  # Ensure tasks list is empty
    tasks.append("Go shopping")

    # Mock input to delete a non-existent task
    monkeypatch.setattr("builtins.input", lambda _: "5")

    # Act
    delete_task()

    # Assert
    captured = capfd.readouterr()
    assert "Task No. 5 not found." in captured.out
    assert len(tasks) == 1
    assert tasks[0] == "Go shopping"


def test_delete_task_empty_list(monkeypatch, capfd):
    # Arrange
    tasks.clear()  # Ensure tasks list is empty

    # Mock input to delete from an empty list
    monkeypatch.setattr("builtins.input", lambda _: "0")

    # Act
    delete_task()

    # Assert
    captured = capfd.readouterr()
    assert "There are no tasks currently." in captured.out


def test_delete_task_invalid_input(monkeypatch, capfd):
    # Arrange
    tasks.clear()  # Ensure tasks list is empty
    tasks.append("Go shopping")

    # Mock input to delete with invalid input (non-integer)
    monkeypatch.setattr("builtins.input", lambda _: "invalid")

    # Act
    delete_task()

    # Assert
    captured = capfd.readouterr()
    assert "Invalid input." in captured.out
    assert len(tasks) == 1
    assert tasks[0] == "Go shopping"
