print("Program starting.")
print("This program can copy a file.")
src = input("Insert source filename: ")
dst = input("Insert destination filename: ")
with open(src) as rf:
	with open(dst, "w") as wf:
		wf.write(rf.read())
print(f"Reading file '{src}' content.")
print("File content ready in memory.")
print(f"Writing content into file '{dst}'.")
print("Copying operation complete.")
print("Program ending.")

