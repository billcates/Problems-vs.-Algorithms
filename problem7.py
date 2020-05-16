class RouteTrie:
    def __init__(self, handler=None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root=RouteTrieNode(handler)
    def insert(self,path_pieces ,handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current=self.root
        for path in path_pieces:
            if path not in current.children:
                current.children[path]=RouteTrieNode(None)
            current=current.children[path]
        current.handler=handler

    def find(self, path_pieces):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current=self.root
        for path in path_pieces:
            if path not in current.children:
                return None
            current=current.children[path]
        return current.handler
# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self,handler=None):
        # Initialize the node with children as before, plus a handler
        self.children={}
        self.handler=handler
    def insert(self,path_piece,handler):
        self.children[path_piece]=handler
    def __repr__(self):
        return str(self.children)

class Router:
    def __init__(self, handler):
        self.route_trie = RouteTrie(handler)
        self.route_trie.root.handler = handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        path_pieces = self.split_path(path)
        self.route_trie.insert(path_pieces , handler)


    def lookup(self,path):
        if path == "":
            return "empty"
        # lookup path (by parts) and return the associated handler
        path_pieces = self.split_path(path)
        return  self.route_trie.find(path_pieces)
    #helper method to return a list of path pieces from a url
    # "/" return []
    #“/foo/bar/hello/world” return [“foo", "bar". "hello", "world”]
    def split_path(self, path):
        if path == "/":
            return []
        path_pieces = path.split('/')
        #remove the initial empty string from path_pieces
        path_pieces.remove('')
        return path_pieces

#Udacity test cases
router = Router("root handler")
router.add_handler("/home/about", "about handler")  # add a route
print("Udacity test case")
# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print  None
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print   None
print(router.lookup("/home/about/me")) # should print  None
print("\n")
print('''"/" is  passed  ''')
#test testcases
router1=Router("root")
print(router1.lookup("/")) #returns root
#when null string is passed
print("\nempty string is passed")
print(router1.lookup("/"))
#general cases
print(router1.lookup("/user"))#return NONE
router1.add_handler("/user","user handler")
print(router1.lookup("/user"))#returns user handler
print(router1.lookup("/user/login/dashboard"))#returns None
router1.add_handler("/user/login/dashboard","dashboard handler")
print(router1.lookup("/user/login/dashboard"))#returns dashboard handler
# when wrong address is passed
print("\nWhen wrong address is passed")
print(router1.lookup("/user/dashboard"))
# termination /
print("\ntermination / is passed")
print(router1.lookup("/user/login/dashboard/"))
#add some route handlers
print("\nsome more handlers")
router1.add_handler("/user/login","login handler")
router1.add_handler("/user/signup","signup handler")
print(router1.lookup("/user/login"))
print(router1.lookup("/user/signup"))
