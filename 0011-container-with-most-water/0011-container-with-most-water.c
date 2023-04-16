

int maxArea(int* height, int heightSize){
    int minIdx = 0, maxIdx = (heightSize - 1);
    int minHeight, area;
    int res = 0;
    while(minIdx < maxIdx){
        minHeight = (height[minIdx] < height[maxIdx]) ? height[minIdx] : height[maxIdx];
        area = minHeight * (maxIdx - minIdx);
        if(area > res){res = area;}
        if(height[minIdx] <= height[maxIdx]){minIdx++;}
        else{maxIdx--;}
    }
    return res;
}