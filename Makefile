INC=-Iincludes/
USR_INC=-I/usr/local/include
SRC=src/
CPPCONN =-I/usr/lical/include/cppconn
SQL_ARG=-lmysqlcppconn
TESTS=-Itest/
all:
	g++ -c src/g2a.cpp -o g2a.so $(INC) -L/usr/lib/x86_64-linux-gnu -lcurl
	g++ -c src/converter.cpp -o converter.so $(INC)
	g++ arsenal.cpp converter.so g2a.so -o arsenal $(INC) -L/usr/lib/x86_64-linux-gnu -lcurl
install:
	mv arsenal /usr/bin

arsenal arsenal.cpp:
	g++ -c arsenal.cpp converter.so g2a.so $(INC) -o arsenal
