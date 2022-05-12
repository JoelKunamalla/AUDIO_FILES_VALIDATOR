#include<bits/stdc++.h>
using namespace std ;
void solve()
{
    string s1;
    cin>>s1;
    cout<<s1.size();
    for(int i=0;i <s1.size();i++)
    {
        if(s1[i] >='A' &&  s1[i] <='Z')
            cout<<s1[i]-'A'+1<<" ";
            else if( s1[i] >='a' && s1[i] <='z')
            cout<<s1[i]-'a'+1<<" ";
    }
}
int main()
{
ios_base :: sync_with_stdio(false);
cin.tie(NULL);
solve();
return 0;
}