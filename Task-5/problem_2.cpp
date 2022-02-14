#include <bits/stdc++.h>
using namespace std;

int main() {
    
    int n , t;
    cin>>n>>t;

    vector<int>v(n);
    for (int i = 0; i < n; ++i) {
        cin>>v[i];
        v[i]=86400-v[i];
    }

   int ans=0;
    for (int i = 0; i < n; ++i) {
        if (t<=0) break;
        t-=v[i];
        ans++;
    }
    cout<<ans<<endl;

}
