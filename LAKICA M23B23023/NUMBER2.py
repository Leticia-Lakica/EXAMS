class StudentQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, student):
        self.queue.append(student)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty."

    def is_empty(self):
        return len(self.queue) == 0

    def queue_size(self):
        return len(self.queue)

student_queue = StudentQueue()

student_queue.enqueue("Student1")
student_queue.enqueue("Student2")
student_queue.enqueue("Student3")

print(student_queue.queue)

served_student = student_queue.dequeue()
print("Served Student:", served_student)

print("Is the queue empty?", student_queue.is_empty())

print("Current queue size:", student_queue.queue_size())
