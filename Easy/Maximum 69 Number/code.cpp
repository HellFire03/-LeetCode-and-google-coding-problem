class Solution {
public:
    int maximum69Number (int num) {
        vector<int> a;
        a.push_back(num);
	    string s = to_string(num);
	    for(int i = 0 ; i<s.size();i++){
	        if(s[i] == '6'){
	            s[i] = '9';
	            a.push_back(stoi(s));
	            s[i] = '6';
	        }
	        else{
	            s[i] = '6';
	            a.push_back(stoi(s));
	            s[i] = '9';
	        }
	    }
	return *max_element(a.begin(), a.end());
    }
};
