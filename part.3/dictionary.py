from double_linked_lists import DoubleLinkedList


class Dictionary:
    def __init__(self, num_buckets=256):
        self.map = DoubleLinkedList()
        for i in range(num_buckets):
            self.map.push(DoubleLinkedList())

    def hash_key(self, key):
        return hash(key) % self.map.count()

    def get_bucket(self, key):
        bucket_id = self.hash_key(key)
        return self.map.get(bucket_id)

    def get_slot(self, key, default=None):
        bucket = self.get_bucket(key)
        if bucket:
            node = bucket.begin
            i = 0
            while node:
                if key == node.value[0]:
                    return bucket, node
                else:
                    node = node.next
                    i += 1
        return bucket, None

    def get(self, key, default=None):
        bucket, node = self.get_slot(key, default=default)
        return node and node.value[1] or node

    def set(self, key, value):
        bucket, slot = self.get_slot(key)
        if slot:
            self.value = (key, value)
        else:
            bucket.push((key, value))

    def delete(self, key):
        bucket = self.get_bucket(key)
        node = bucket.begin
        while node:
            k, v = node.value
            if key == k:
                bucket.detach_node(node)
                break

    def list(self):
        bucket_node = self.map.begin
        while bucket_node:
            slot_node = bucket_node.value.begin
            while slot_node:
                print(slot_node.value)
                slot_node = slot_node.next
            bucket_node = bucket_node.next


def main():
    d = Dictionary()
    print(d)


if __name__ == '__main__':
    main()


main()
