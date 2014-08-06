require 'ostruct'
class Heap

  @repr = []
  attr_accessor :repr

  #creates a max heap
  def initialize(list)
    @repr = heapify(list)
  end

  def children(root)
    kin = OpenStruct.new
    kin.left_position = left_pos = left(root)
    kin.right_position = right_pos = right(root)
    kin.left_value = @repr[left_pos]
    kin.right_value = @repr[right_pos]
    kin
  end

  def heapsort
    sorted = []
    (@repr.length-1).times do |e|
      sorted.push @repr.shift
      @repr = heapify(@repr)
    end
      sorted
  end

  private
  def left(i)
    2*i+1
  end

  def right(i)
    2*i+2
  end

  def parent_of(i)
    ((i-1)/2).floor
  end

  # this is O(n)
  # siftbottom method
  def heapify(arr)
    (1..arr.length-1).to_a.reverse.each do |e|
      parent_position = parent_of(e)
      if arr[e] > arr[parent_position]
        arr[e] , arr[parent_position] = arr[parent_position], arr[e]
      end
    end
    arr
  end
end
