//
//  main.swift
//  Sorting
//
//  Created by Timur on 5/2/21.
//  Copyright © 2021 Absolute Technologies lab. All rights reserved.
//

import Foundation


extension MutableCollection where Self: RandomAccessCollection, Element: Comparable, Index == Int {
    mutating func quickSort(begin: Int, end: Int) {
        if begin < end {
            let partitionIndex = partition(begin: begin, end: end)
            quickSort(begin: begin, end: partitionIndex - 1)
            quickSort(begin: partitionIndex + 1, end: end)
        }
    }
    
    mutating func bubbleSort() {
        for i in 0..<self.count {
            for j in 0..<self.count-i-1 {
                if self[j]>self[j + 1] {
                    swapAt(j + 1, j)
                }
            }
        }
    }
    
    mutating func partition(begin: Int, end: Int) -> Int {
        let pivot = self[end]
        var i = begin - 1
        for j in begin..<end where self[j] <= pivot {
            i += 1
            swapAt(i, j)
        }
        swapAt(i + 1, end)
        return i + 1
    }
}

func test_quick(array : [Int]){
    var test_array = array
    print(test_array)
    let start = DispatchTime.now()
    test_array.quickSort(begin: 0, end: array.count-1)
    let end = DispatchTime.now()
    print(test_array)
    let nanoTime = end.uptimeNanoseconds - start.uptimeNanoseconds
    let timeInterval = Double(nanoTime) / 1_000_000_000
    print(timeInterval)
}


func test_bubble(array : [Int]){
    var test_array = array
    print(test_array)
    let start = DispatchTime.now()
    test_array.bubbleSort()
    let end = DispatchTime.now()
    print(test_array)
    let nanoTime = end.uptimeNanoseconds - start.uptimeNanoseconds
    let timeInterval = Double(nanoTime) / 1_000_000_000
    print(timeInterval)
}

