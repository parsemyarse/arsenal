#include<sys/socket.h>
#include<netinet/tcp.h>   
#include<netinet/ip.h>

template<char const P> class Socket;
template<>
class Socket<IPPROTO_UDP> {
  private:
    int fd;
    char datagram[4096]
  public:
    Socket(){
      fd = socket (PF_INET, SOCK_RAW, IPPROTO_UDP);
    }
};