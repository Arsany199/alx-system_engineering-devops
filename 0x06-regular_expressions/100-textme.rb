#!/usr/bin/env ruby
# to get a pattern
puts ARGV[0].scan(/(?<=from:|to:|flags:).+?(?=\])/).join(',')
