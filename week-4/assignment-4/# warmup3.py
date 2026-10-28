# warmup3
# lists of programming languages
A = [ "Python", "HTML", "C#", "Swift", "Java", "Kotlin"]
B = [ "PHP", "Java", "Go", "Swift", "Scala", "Perl", "Rust", "Assembly"]

print(A)
print(B)
print("_________________")

set_A = set(A)
set_B = set(B)

print(set(A))
print(set(B))
print("=================")

print(set(A).union(set(B)))          # Output: {Python, HTML, C#, Swift, Java, Kotlin, PHP, Go, Scala, Perl, Rust, Assembly}
print(set(A).intersection(set(B)))   # Output: {Java, Swift}
print(set(A).difference(set(B)))     # Output: {Python, HTML, C#, Kotlin}
