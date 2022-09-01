#include <stdio.h>

int main()
{
    int i,n,j;
    scanf("%d",&n);
    int x[n][n];
    for(i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            scanf("%d",&x[i][j]);
            //printf("%d\n",x[i][j]);
        }
    }
    for (i=0;i<n;i++)
    {
        printf("%d ",x[i][i]);
    }
    printf("\n");
    for(i=0;i<n;i++)
    {
        printf("%d ",x[i][n-i-1]);
        
    }
    return 0;
} 
