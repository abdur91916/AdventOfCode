import re

import numpy
from statistics import mode
from collections import Counter

class Solution:


    def __init__(self):
        reader = open('input.txt')
        self.ips = reader.read().splitlines()

    def count_tls_supported(self, ips):
        count = 0
        for ip in ips:
            if self.supports_tls(ip):
                count += 1
        return count

    def count_ssl_supported(self, ips):
        count = 0
        for ip in ips:
            if self.supports_ssl(ip):
                count += 1
        return count



    def supports_tls(self, ip):
        ip_split = re.split('\[|\]', ip)
        hypernet_sequences = ip_split[1::2]
        non_hypernets = ip_split[::2]

        for hypernet in hypernet_sequences:
            if self.contains_abba(hypernet):
                return False

        for non_hypernet in non_hypernets:
            if self.contains_abba(non_hypernet):
                return True

        return False

    def contains_abba(self, string):
        for i in range(0, len(string) - 3):
            substring = string[i:i+4]
            substring_reversed = substring[::-1]
            if substring[0] != substring[1] and substring[0:2] == substring_reversed[0:2]:
                return True
        return False

    def supports_ssl(self, ip):
        ip_split = re.split('\[|\]', ip)
        hypernet_sequences = ip_split[1::2]
        non_hypernets = ip_split[::2]

        babs = set()

        for non_hypernet in non_hypernets:
            babs.update(self.find_babs(non_hypernet))

        for hypernet in hypernet_sequences:
            for bab in babs:
                if bab in hypernet:
                    return True

        return False

    def find_babs(self, string):
        babs = set()
        for i in range(0, len(string) - 2):
            substring = string[i:i + 3]
            if substring[0] == substring[2] and substring[0] != substring[1]:
                bab = substring[1] + substring[0] + substring[1]
                babs.add(bab)
        return babs


    def part_one(self):
        count = self.count_tls_supported(self.ips)

        print("The answer to Day 6 part one is " + str(count))

    def part_two(self):
        count = self.count_ssl_supported(self.ips)
        print("The answer to Day 6 part two is " + str(count))





sol = Solution()
sol.part_one()
sol.part_two()
