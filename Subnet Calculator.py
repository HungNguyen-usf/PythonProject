import ipaddress


class SubnetCalculator:
    def __init__(self, network_address, subnet_mask):
        self.network_address = network_address
        self.subnet_mask = subnet_mask

    def calculate_subnets(self, num_subnets):
        try:
            num_subnets = int(num_subnets)
        except ValueError:
            print("Number of subnets must be a valid integer.")
            return []

        network = ipaddress.IPv4Network(self.network_address + '/' + self.subnet_mask, strict=False)
        subnets = list(network.subnets(new_prefix=network.prefixlen + int(num_subnets).bit_length() - 1))
        return subnets

    def display_subnets(self, subnets):
        if not subnets:
            print("No subnets to display")
            return

    def display_subnets(self, subnets):
        print("Subnets:")
        for subnet in subnets:
            print("Network Address: ", subnet.with_prefixlen)
            print("First Usable Address: ", subnet.network_address + 1)
            print("Last Usable Address: ", subnet.network_address + subnet.num_addresses - 2)
            print("Broadcast Address: ", subnet.broadcast_address)
            print("Subnet Mask: ", subnet.netmask)
            print("----------------------")


# Input of network info to subnet
def main():
    # Asks for network address and subnet mask to start from
    network_address = input("Enter the network address: ")
    subnet_mask = input("Enter the subnet mask: ")

    calculator = SubnetCalculator(network_address, subnet_mask)

    # Asks for number of subnets to be created
    num_subnets = input("Enter the number of subnets: ")

    # Calculates and display the subnets
    subnets = calculator.calculate_subnets(num_subnets)
    calculator.display_subnets(subnets)


if __name__ == '__main__':
    main()

# If time and skill premit GUI interface and print to spreadsheet option