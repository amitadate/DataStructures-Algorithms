class Hashy{
    static void printPairs(int arr[],int sum){
        boolean binmap[]=new boolean[10000];
        for(int i=0;i<arr.length;i++){
            int temp=sum-arr[i];
            if(temp>=0 && binmap[temp]){
                System.out.println("Pair is ("+temp+","+arr[i]+")");
            }
            binmap[arr[i]]=true;
        }
    }
    public static void main (String[] args) {
        int A[] = {1, 4, 45, 6, 10, 8, 15,0,16};
        int n = 16;
        printPairs(A,  n);
    }
}
