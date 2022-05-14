class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        a=[]
        def lol(image,i,j,k,n):
            if i<0 or i>=len(image) or j>=len(image[0]) or j<0 or image[i][j]!=k or [i,j] in a:
                return
            image[i][j]=n
            a.append([i,j])
            lol(image,i-1,j,k,n)
            lol(image,i+1,j,k,n)
            lol(image,i,j+1,k,n)
            lol(image,i,j-1,k,n)
        lol(image,sr,sc,image[sr][sc],newColor)
        return image
