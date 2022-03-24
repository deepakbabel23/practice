// client_server_nexthink.cpp : Defines the entry point for the application.
//

#include "client_server_nexthink.h"
#include <unordered_map>
#include <set>
#include <chrono>
#include <ctime>

using namespace std;

struct Msg
{
	private:
		static int msg_id;
		std::string msg;
		std::chrono::system_clock::time_point time_stamp;
		std::string new_msg_string;
	public:
		Msg() {}
		Msg(std::string msg)
		{
			this->msg = msg;
			//Msg::msg_id += 1;
			time_stamp = std::chrono::system_clock::now();
			new_msg_string = "new";
		}
		void get_msg_info(std::string &ret_msg) const
		{
			cout << endl << "{ timestamp:" << std::chrono::system_clock::to_time_t(time_stamp) << ", ";
			cout << "id: " << msg_id << ", ";
			cout << "new: " << new_msg_string<<" }"<<endl;
		}
};

int Msg::msg_id = 0;
class Client
{
	public:
		Client()
		{
			clientId.clear();
			clientMsgSet.clear();
		}
		Client(std::string clientId, std::string clientMsg)
		{
			this->clientId = clientId;
			this->clientMsg = clientMsg;
		}
		Client(const Client& obj)
		{
			this->clientId = obj.clientId;
			this->msg = obj.msg;
			this->clientMsgSet = obj.clientMsgSet;
			//copy the values
		}
		Client& operator=(const Client& obj)
		{
			this->clientId = obj.clientId;
			this->msg = obj.msg;
			this->clientMsgSet = obj.clientMsgSet;

			//copy the values into existing object
			return *this;
		}
		~Client()
		{
			//any cleanup which is required
		}
	private:
		//a client will be uniquely identified using
		//his id and respective msgs for his client id.
		std::string clientId;
		std::set<std::string> clientMsgSet;
		Msg msg;
		unordered_map<std::string, std::string> client_msg_map;
		std::string clientMsg;
	public:
		void process_msg(std::string clientMsg, std::string clientId)
		{
			this->clientId = clientId;
			auto ret = this->clientMsgSet.insert(clientMsg);
			if (ret.second == true)
			{
				this->msg = Msg(clientMsg);
				//prepare response:
				//std::list<std::string> tempList = {"1",}
				//timestamp, msg_id, "new"
			}
			else
			{
				//prepare response:
				//clientid, msg, timestamp, "new"
			}
			std::string ret_msg;
			this->msg.get_msg_info(ret_msg);
		}
};


int main()
{
	Client client;
	client.process_msg("hi", "Ram");
	cout << "Hello CMake." << endl;
	return 0;
}
