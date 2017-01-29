//http://www.geeksforgeeks.org/dynamic-programming-set-12-longest-palindromic-subsequence/

class LPS{
    
    static int max (int x, int y) { return (x > y)? x : y; }
    
    
    
    public static int lps(String seq, int i, int j){
        
        int n=seq.length();
        if(i==j){
            
            return 1;
        }
        if(j-i==1){
            if(seq.charAt(i)==seq.charAt(j)){
                
                return 2;
            }
            else{
                
                return 1;
            }
        }
        int ans;
        if(seq.charAt(i)==seq.charAt(j)){
            ans=lps(seq,i+1,j-1)+2;
        }
        else{
            ans=max(lps(seq,i+1,j),lps(seq,i,j-1));
        }
        
        return ans;
    }
    
    public static void main(String args[]){
        String seq="GEEKSFORGEEKS";
        int n=seq.length();
        
        System.out.println("The lps of seq is "+lps(seq,0,n-1));
    }
}
