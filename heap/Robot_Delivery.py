import heapq  
import random  
import time 


class DeliveryCenter:
    def __init__(self):
        self.tasks = []
        self.counter = 1  
    
    def add_delivery(self, priority, description):
        """
        Add a delivery task to the heap queue with a given priority.
        Lower priority value = higher urgency.
        """
        heapq.heappush(self.tasks, (priority, self.counter, description))
        print(f"📦 New delivery added (Priority {priority}): {description}")
        self.counter += 1  # Increment counter for next task

    def dispatch_delivery(self):
        """
        Dispatch the highest-priority delivery task (lowest priority number).
        Simulate a random outcome for the dispatched delivery.
        """
        if self.tasks:
            # Pop the task with the smallest priority value
            priority, _, description = heapq.heappop(self.tasks)
            print(f"\n🤖 Robot dispatched for: {description} (Priority {priority})")

            # Randomly select a delivery outcome to simulate real-world events
            event = random.choice([
                "✅ Delivery successful! Customer is happy.",
                "⚡ Robot ran out of battery mid-route!",
                "🚧 Traffic jam delayed delivery.",
                "🎉 Bonus points! Customer tipped extra credits."
            ])
            print(f"🗞️ Status: {event}\n")
        else:
            # When no deliveries remain
            print("😴 No deliveries left! All robots are recharging.\n")


def game():
    """
    Main function to simulate the Robot Delivery Rush game.
    It initializes delivery tasks, prioritizes them, and dispatches robots.
    """
    print("🚀 Welcome to *Robot Delivery Rush*!")
    print("Manage your robots wisely — urgent tasks first!\n")

    # Create a delivery center instance
    center = DeliveryCenter()

    # List of delivery tasks with their priorities
    deliveries = [
        ("Deliver medicine to Sector 9", 1),
        ("Send pizza to Tech Hub", 3),
        ("Deliver spare parts to Factory 22", 2),
        ("Ship memes to Galactic Forum", 5),
        ("Recharge station batteries", 4)
    ]

    # Add all deliveries to the system with a short delay between each
    for desc, prio in deliveries:
        center.add_delivery(prio, desc)
        time.sleep(0.5)

    print("\n--- Dispatching Begins ---\n")
    time.sleep(1)

    # Keep dispatching until all tasks are done
    while center.tasks:
        center.dispatch_delivery()
        time.sleep(1)

    print("🏁 All deliveries completed! The city runs smoothly again.\n")


# Run the game
game()
