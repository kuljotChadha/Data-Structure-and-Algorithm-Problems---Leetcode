class Solution:
    def reorganizeString(self, s: str) -> str:
        dict1=collections.Counter(s)
        
        heap=[]

        for key,value in dict1.items():
            heap.append([-value,key])

        heapq.heapify(heap)
    
        a=''
        while heap:
            val,key = heapq.heappop(heap)
            if len(a)>0 and a[-1] == key:
                if heap:
                    tempval,tempkey = heapq.heappop(heap)
                    a+=tempkey

                    if tempval+1 == 0:
                        pass
                    else:
                        heapq.heappush(heap,[tempval+1,tempkey])
                else:
                    return ''
            
            a+=key
            if val+1 == 0:
                continue
            else:
                heapq.heappush(heap,[val+1,key])
        return a
