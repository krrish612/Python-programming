# Advanced To-Do List with Categories, Priority, Due Dates, and Persistence

import json
from datetime import datetime, timedelta
from enum import Enum
from dataclasses import dataclass, field, asdict
from typing import List, Optional
from pathlib import Path
import os

# ================== ENUMS AND DATACLASSES ==================
class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    URGENT = 4

class Status(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

@dataclass
class Task:
    """Task with full metadata"""
    id: int
    title: str
    description: str = ""
    priority: Priority = Priority.MEDIUM
    category: str = "General"
    status: Status = Status.PENDING
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    due_at: Optional[str] = None
    completed_at: Optional[str] = None
    tags: List[str] = field(default_factory=list)
    
    def is_overdue(self) -> bool:
        """Check if task is overdue"""
        if self.due_at and self.status != Status.COMPLETED:
            return datetime.fromisoformat(self.due_at) < datetime.now()
        return False
    
    def is_due_today(self) -> bool:
        """Check if due today"""
        if self.due_at:
            due = datetime.fromisoformat(self.due_at)
            today = datetime.now().date()
            return due.date() == today
        return False
    
    def complete(self) -> None:
        """Mark task as completed"""
        self.status = Status.COMPLETED
        self.completed_at = datetime.now().isoformat()
    
    def to_dict(self) -> dict:
        """Convert to dictionary for JSON"""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority.name,
            "category": self.category,
            "status": self.status.value,
            "created_at": self.created_at,
            "due_at": self.due_at,
            "completed_at": self.completed_at,
            "tags": self.tags
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Task':
        """Create from dictionary"""
        return cls(
            id=data["id"],
            title=data["title"],
            description=data.get("description", ""),
            priority=Priority[data.get("priority", "MEDIUM")],
            category=data.get("category", "General"),
            status=Status(data.get("status", "pending")),
            created_at=data.get("created_at", datetime.now().isoformat()),
            due_at=data.get("due_at"),
            completed_at=data.get("completed_at"),
            tags=data.get("tags", [])
        )

# ================== CATEGORY MANAGER ==================
class CategoryManager:
    """Manage task categories"""
    
    DEFAULT_CATEGORIES = {
        "General": "📋",
        "Work": "💼",
        "Personal": "👤",
        "Study": "📚",
        "Health": "💪",
        "Shopping": "🛒",
        "Home": "🏠",
    }
    
    def __init__(self):
        self.categories = dict(self.DEFAULT_CATEGORIES)
    
    def add_category(self, name: str, emoji: str = "📌") -> None:
        """Add new category"""
        self.categories[name] = emoji
    
    def get_emoji(self, category: str) -> str:
        """Get emoji for category"""
        return self.categories.get(category, "📌")
    
    def list_categories(self) -> List[str]:
        """List all categories"""
        return list(self.categories.keys())

# ================== TODO LIST ==================
class TodoList:
    """Advanced to-do list manager"""
    
    def __init__(self, filename: str = "todo_data.json"):
        self.tasks: List[Task] = []
        self.next_id = 1
        self.categories = CategoryManager()
        self.filename = filename
        self.load()
    
    def add_task(self, title: str, **kwargs) -> Task:
        """Add new task"""
        task = Task(id=self.next_id, title=title, **kwargs)
        self.tasks.append(task)
        self.next_id += 1
        self.save()
        return task
    
    def get_task(self, task_id: int) -> Optional[Task]:
        """Get task by ID"""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    
    def update_task(self, task_id: int, **updates) -> bool:
        """Update task"""
        task = self.get_task(task_id)
        if not task:
            return False
        
        for key, value in updates.items():
            if hasattr(task, key):
                setattr(task, key, value)
        
        self.save()
        return True
    
    def delete_task(self, task_id: int) -> bool:
        """Delete task"""
        task = self.get_task(task_id)
        if task:
            self.tasks.remove(task)
            self.save()
            return True
        return False
    
    def complete_task(self, task_id: int) -> bool:
        """Mark task as completed"""
        task = self.get_task(task_id)
        if task:
            task.complete()
            self.save()
            return True
        return False
    
    def filter_tasks(self, **filters) -> List[Task]:
        """Filter tasks by criteria"""
        results = self.tasks
        
        if "status" in filters:
            results = [t for t in results if t.status == filters["status"]]
        
        if "priority" in filters:
            results = [t for t in results if t.priority == filters["priority"]]
        
        if "category" in filters:
            results = [t for t in results if t.category == filters["category"]]
        
        if "overdue" in filters and filters["overdue"]:
            results = [t for t in results if t.is_overdue()]
        
        if "due_today" in filters and filters["due_today"]:
            results = [t for t in results if t.is_due_today()]
        
        if "search" in filters:
            query = filters["search"].lower()
            results = [t for t in results if query in t.title.lower()]
        
        return results
    
    def sort_tasks(self, by: str = "priority", reverse: bool = True) -> List[Task]:
        """Sort tasks"""
        if by == "priority":
            return sorted(self.tasks, key=lambda t: t.priority.value, reverse=reverse)
        elif by == "due_date":
            return sorted(self.tasks, key=lambda t: t.due_at or "", reverse=reverse)
        elif by == "created":
            return sorted(self.tasks, key=lambda t: t.created_at, reverse=reverse)
        elif by == "title":
            return sorted(self.tasks, key=lambda t: t.title.lower())
        return self.tasks
    
    def get_stats(self) -> dict:
        """Get statistics"""
        return {
            "total": len(self.tasks),
            "pending": len([t for t in self.tasks if t.status == Status.PENDING]),
            "in_progress": len([t for t in self.tasks if t.status == Status.IN_PROGRESS]),
            "completed": len([t for t in self.tasks if t.status == Status.COMPLETED]),
            "overdue": len([t for t in self.tasks if t.is_overdue()]),
        }
    
    def save(self) -> None:
        """Save to file"""
        data = {
            "next_id": self.next_id,
            "tasks": [t.to_dict() for t in self.tasks]
        }
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load(self) -> None:
        """Load from file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    data = json.load(f)
                    self.next_id = data.get("next_id", 1)
                    self.tasks = [Task.from_dict(t) for t in data.get("tasks", [])]
            except (json.JSONDecodeError, IOError):
                self.tasks = []
                self.next_id = 1

# ================== MENU FUNCTIONS ==================
def get_priority() -> Priority:
    """Get priority from user"""
    print("Priority: (1) Low (2) Medium (3) High (4) Urgent")
    choice = input("Choice: ")
    priorities = [Priority.LOW, Priority.MEDIUM, Priority.HIGH, Priority.URGENT]
    try:
        return priorities[int(choice) - 1]
    except (ValueError, IndexError):
        return Priority.MEDIUM

def get_due_date() -> Optional[str]:
    """Get due date from user"""
    print("Due date? (y/n): ", end="")
    if input().lower() != 'y':
        return None
    
    print("Days from now (or specific date YYYY-MM-DD): ", end="")
    date_input = input().strip()
    
    try:
        # Try parsing as days
        days = int(date_input)
        due = datetime.now() + timedelta(days=days)
        return due.isoformat()
    except ValueError:
        try:
            # Try parsing as date
            due = datetime.strptime(date_input, "%Y-%m-%d")
            return due.isoformat()
        except ValueError:
            return None

def display_task(task: Task, show_emoji: bool = True) -> None:
    """Display a single task"""
    emoji = ""
    if show_emoji:
        categories = CategoryManager()
        emoji = categories.get_emoji(task.category)
    
    status_icon = {
        Status.PENDING: "⏳",
        Status.IN_PROGRESS: "🔄",
        Status.COMPLETED: "✅",
        Status.CANCELLED: "❌"
    }[task.status]
    
    priority_icon = {
        Priority.LOW: "🟢",
        Priority.MEDIUM: "🟡",
        Priority.HIGH: "🟠",
        Priority.URGENT: "🔴"
    }[task.priority]
    
    overdue_marker = " ⚠️ OVERDUE" if task.is_overdue() else ""
    
    print(f"{task.id}. {emoji} {task.title} {status_icon} {priority_icon}{overdue_marker}")
    if task.description:
        print(f"   📝 {task.description}")
    if task.due_at:
        due_str = datetime.fromisoformat(task.due_at).strftime("%Y-%m-%d %H:%M")
        print(f"   📅 Due: {due_str}")

def display_tasks(tasks: List[Task], title: str = "Tasks") -> None:
    """Display task list"""
    if not tasks:
        print(f"\nNo {title}")
        return
    
    print(f"\n=== {title} ({len(tasks)}) ===")
    for task in tasks:
        display_task(task)

# ================== MAIN MENU ==================
def main():
    todo = TodoList()
    
    while True:
        print("\n=== TO-DO LIST ===")
        print("1. View all tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Edit task")
        print("6. Filter tasks")
        print("7. Statistics")
        print("8. View by category")
        print("9. Add category")
        print("10. Exit")
        
        choice = input("\nChoice: ")
        
        if choice == "1":
            # View all
            print("\nSort by: (1) Priority (2) Due date (3) Created (4) Title")
            sort_choice = input("Choice: ")
            
            if sort_choice == "1":
                tasks = todo.sort_tasks("priority")
            elif sort_choice == "2":
                tasks = todo.sort_tasks("due_date")
            elif sort_choice == "3":
                tasks = todo.sort_tasks("created")
            elif sort_choice == "4":
                tasks = todo.sort_tasks("title")
            else:
                tasks = todo.tasks
            
            display_tasks(tasks, "All Tasks")
        
        elif choice == "2":
            # Add task
            title = input("Task title: ")
            if not title:
                continue
            
            description = input("Description (optional): ")
            priority = get_priority()
            category = input("Category (default: General): ") or "General"
            due = get_due_date()
            
            todo.add_task(
                title=title,
                description=description,
                priority=priority,
                category=category,
                due_at=due
            )
            print("Task added!")
        
        elif choice == "3":
            # Complete task
            try:
                task_id = int(input("Task ID to complete: "))
                if todo.complete_task(task_id):
                    print("Task completed!")
                else:
                    print("Task not found!")
            except ValueError:
                print("Invalid ID!")
        
        elif choice == "4":
            # Delete task
            try:
                task_id = int(input("Task ID to delete: "))
                if todo.delete_task(task_id):
                    print("Task deleted!")
                else:
                    print("Task not found!")
            except ValueError:
                print("Invalid ID!")
        
        elif choice == "5":
            # Edit task
            try:
                task_id = int(input("Task ID to edit: "))
                task = todo.get_task(task_id)
                if not task:
                    print("Task not found!")
                    continue
                
                print(f"Editing: {task.title}")
                print("Leave blank to keep current value")
                
                title = input(f"Title [{task.title}]: ")
                description = input(f"Description [{task.description}]: ")
                priority = get_priority()
                due = get_due_date()
                
                todo.update_task(
                    task_id,
                    title=title or None,
                    description=description or None,
                    priority=priority,
                    due_at=due
                )
                print("Task updated!")
            except ValueError:
                print("Invalid ID!")
        
        elif choice == "6":
            # Filter
            print("\nFilter by: (1) Status (2) Priority (3) Overdue (4) Due today (5) Search")
            filter_choice = input("Choice: ")
            
            if filter_choice == "1":
                print("Status: (1) Pending (2) In Progress (3) Completed")
                try:
                    status_choice = int(input("Choice: "))
                    statuses = [Status.PENDING, Status.IN_PROGRESS, Status.COMPLETED]
                    tasks = todo.filter_tasks(status=statuses[status_choice - 1])
                    display_tasks(tasks, "Filtered Tasks")
                except (ValueError, IndexError):
                    pass
            
            elif filter_choice == "2":
                priority = get_priority()
                tasks = todo.filter_tasks(priority=priority)
                display_tasks(tasks, "Filtered Tasks")
            
            elif filter_choice == "3":
                tasks = todo.filter_tasks(overdue=True)
                display_tasks(tasks, "Overdue Tasks")
            
            elif filter_choice == "4":
                tasks = todo.filter_tasks(due_today=True)
                display_tasks(tasks, "Due Today")
            
            elif filter_choice == "5":
                search = input("Search: ")
                tasks = todo.filter_tasks(search=search)
                display_tasks(tasks, f"Search: {search}")
        
        elif choice == "7":
            # Stats
            stats = todo.get_stats()
            print("\n=== STATISTICS ===")
            print(f"Total tasks: {stats['total']}")
            print(f"Pending: {stats['pending']}")
            print(f"In Progress: {stats['in_progress']}")
            print(f"Completed: {stats['completed']}")
            print(f"Overdue: {stats['overdue']}")
        
        elif choice == "8":
            # By category
            category = input("Category: ")
            tasks = todo.filter_tasks(category=category)
            display_tasks(tasks, category)
        
        elif choice == "9":
            # Add category
            name = input("Category name: ")
            emoji = input("Emoji: ")
            todo.categories.add_category(name, emoji)
            print("Category added!")
        
        elif choice == "10":
            print("Goodbye!")
            break
    
    todo.save()

if __name__ == "__main__":
    main()