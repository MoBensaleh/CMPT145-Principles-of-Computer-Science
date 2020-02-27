import a7q6 as a7q6
import node as node

#several nodes for to_sring()
print(a7q6.to_string(node.create(1, node.create(2, node.create(3)))))
#one node for to_string()
print(a7q6.to_string(node.create(1)))


#several nodes for copy_chain()
print(a7q6.copy_chain(node.create(1, node.create(2, node.create(3)))))

# one node for copy_chain()
print(a7q6.copy_chain(node.create(1)))



# node chain with no replacement for replace()
print(a7q6.replace(node.create(1, node.create(2, node.create(3))), 2, 2))
# node chain with several replacements for replace()
print(a7q6.replace(node.create(1, node.create(1, node.create(3, node.create(1, node.create(4))))), 1, 5))

