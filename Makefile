main: main.o foo.o
	g++ -o $@ $^

%.o: %.cxx
	g++ -c $<

clean:
	rm -f *.o main
