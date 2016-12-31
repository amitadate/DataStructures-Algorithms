class KMP{
    
    void kmpSearch(String pat, String txt){
        int M=pat.length();
        int N=txt.length();
        
        int lps[]=new int[M];
        computeLps(pat,M,lps);
        int i=0;
        int j=0;
        while(i<N){
            if(pat.charAt(j)==txt.charAt(i)){
                i++;
                j++;
            }
            if(j==M){
                System.out.println("\nPattern matched at "+(i-M));
                j=lps[M-1];
            }
            else if(pat.charAt(j)!=txt.charAt(i) && i<N){
                if(j!=0){
                   j=lps[j-1]; 
                }
                else{
                    i++;
                }
            }
        }
    }
    
    void computeLps(String pat, int M, int lps[]){
        int i=0;
        int len=0;
        lps[i]=0;
        i++;
        while(i<M){
            if(pat.charAt(len)==pat.charAt(i)){
                len++;
                lps[i]=len;
                i++;
            }
            else{
                if(len!=0){
                    len=lps[len-1];
                }
                else{
                    lps[i]=len;
                    i++;
                }
            }
        }
    }
    
    public static void main(String[] args){
        String txt="AABAACAADAABAABA";
        String pat="AABA";
        KMP obj=new KMP();
        obj.kmpSearch(pat,txt);
    }
}
