#include<bits/stdc++.h>
using namespace std;

const int N = 2e5;
int a[N];

int main(void)
{
    int tc=0, n;
    scanf("%d",&tc);
    while(tc--)
    {
		scanf("%d",&n);
		for(int i=1;i<=n;i++) scanf("%d",&a[i]);
		int cur = n-1, ans = 0;
		while(cur)
		{
			if(a[cur] == a[n]) cur--;
			else
			{
				cur -= (n-cur);
				ans ++;
			}
		}
		printf("%d\n", ans);
    }
}
