import heapq


# Class to represent the Symbol Table
class SymbolTable:

    def __init__(self):
        # Priority queue (min-heap) for storing symbol names
        self.symbol_heap = []
        # Dictionary to store symbol information (type, value)
        self.symbol_dict = {}

    # Method to add a new symbol
    def add_symbol(self, name, var_type, value):
        heapq.heappush(self.symbol_heap, name)
        self.symbol_dict[name] = {'type': var_type, 'value': value}

    # Method to update an existing symbol's value
    def update_symbol(self, name, value):
        if name in self.symbol_dict:
            self.symbol_dict[name]['value'] = value
        else:
            raise KeyError(f"Symbol '{name}' not found.")

    # Method to retrieve symbol information
    def get_symbol(self, name):
        return self.symbol_dict.get(name, None)

    # Method to print all symbols in the symbol table
    def print_symbols(self):
        # Sort heap to maintain order
        temp_heap = self.symbol_heap[:]
        heapq.heapify(temp_heap)
        while temp_heap:
            symbol_name = heapq.heappop(temp_heap)
            print(
                f"Symbol: {symbol_name}, Type: {self.symbol_dict[symbol_name]['type']}, "
                f"Value: {self.symbol_dict[symbol_name]['value']}")


# Simulating a Zara program
def example_sub_program(symbol_table):
    # Adding symbols (variable declarations)
    symbol_table.add_symbol("a", "integer", "10")
    symbol_table.add_symbol("b", "float", "3.14")
    symbol_table.add_symbol("arr", "array", "[1, 2, 3]")
    symbol_table.add_symbol("str", "string", "Hello")
    symbol_table.add_symbol("stk", "stack", "[]")

    # Updating a symbol
    symbol_table.update_symbol("b", "6.28")

    # Printing a specific symbol's details
    symbol_b = symbol_table.get_symbol("b")
    print(
        f"\nUpdated Symbol 'b': Type: {symbol_b['type']}, Value: {symbol_b['value']}"
    )

    # Print all symbols in the symbol table
    print("\nAll Symbols in the Symbol Table:")
    symbol_table.print_symbols()


# Main program to run the symbol table operations
if __name__ == "__main__":
    # Create a symbol table
    symbol_table = SymbolTable()

    # Simulate Zara program's variable declarations and operations
    example_sub_program(symbol_table)

    print("""
    Mwai Irungu C026-01-0907/2022
    Urbanus Kioko C026-01-0937/2022
    Charles Kahuho C026-01-0941/2022
    Brian Chepyegon C026-01-0970/2022
    """)
