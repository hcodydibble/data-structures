export class Node {
    constructor(public data:number, 
                public next:Node){
        data = data
        next = next
    }
}

export class LinkedList{
    private counter:number = 0
    private head:Node = null

    constructor(iterable?:number[]){
        if(iterable instanceof Array)
            iterable.forEach(x => this.push(x))
    }

    // Push a new Node into the Linked List containing the given value as long as it is a number
    push(val:number): void {
        this.head = new Node(val, this.head) // Create a new Node with the given value and assign it as the head
        this.counter++ // Increase the counter by one
    }

    // Pop the first Node (head Node) off the Linked List and return the value attached to it
    pop():number {
        let output:number

        if(this.head === null) // If the Linked List is empty return undefined
            return undefined

        output = this.head.data // Store the value of the head Node
        this.head = this.head.next // Set the next Node in the Linked List as the head (or null if there is only one Node)
        this.counter-- // Subtract one from the counter
        return output 

    }

    size():number {
        return this.counter
    }

    // Search the Linked List for a Node containing the given value
    search(val:number): Node {
        let current:Node = this.head // Store head Node in variable
        while(current){
            if(current.data === val) // If the Node in the current variable contains the given value, return it
                return current
            current = current.next // Set current Node to the next Node in the line
        }
        return undefined
    }

    remove(node:Node): void {
        let current:Node

        if(node === null)
            return

        if(this.head === node){
            this.head = this.head.next
            this.counter--
            return
        }

        current = this.head
        while(current){
            if(current.next === node){
                current.next = node.next
                this.counter--
                return
            }
            current = current.next
        }
    }

    display(): string {
        let current: Node = this.head
        let displayThis: number[] = []

        while(current){
            displayThis.push(current.data)
            current = current.next
        }
        return displayThis.join(", ")
    }
}
