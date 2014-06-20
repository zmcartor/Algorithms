#graph expected to be a Hash with structure key : [arry of nodes]
#
module Graphy
require 'ostruct'

  def dfs(graph, node)
    node.discovered = true
    puts "node labeled %s discovered!" % node.label
    graph[node].each do |n|
      unless node.discovered then dfs(graph,n) end
    end
  end

  def create_node(label=nil)
    return OpenStruct.new(discovered: false, label: label)
  end

end

if __FILE__ == $0
  include Graphy
  puts "it's graph time!\n"

  

  #create a cool graph and run DFS through it yeah!

end
