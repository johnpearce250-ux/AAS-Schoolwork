
def push(s,x):
    s.append(x)

def pop_safe(s):
    if len(s)==0:
        print('Stack is empty.')
        return None
    else:
        popped=s.pop()
        return popped

def peek_safe(s):
    if not s:
        print('Stack is empty.')
        return None
    else:
        print(s[-1])
undo_history=[]
push(undo_history, 1)
push(undo_history, 2)
push(undo_history, 3)
print(undo_history)
popped1=pop_safe(undo_history)
print(popped1)
popped2=pop_safe(undo_history)
print(popped2)
popped3=pop_safe(undo_history)
print(popped3)
popped4=pop_safe(undo_history)
