# How to Create and Write to a File in Python video

# it will over write.

file_builder = open("logger.txt", "w+")

for i in range(1000):
    file_builder.write(f"I'm on line {i + 1}\n") # carriage return


# file_builder.write("Hey, I'm in a file!")

file_builder.close()
