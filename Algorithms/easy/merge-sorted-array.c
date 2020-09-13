int comparator(const void *p, const void *q) {
    int l = *(const int *)p;
    int r = *(const int *)q;
    if (l > r) return 1;
    if (l < r) return -1;
    return 0;
}

void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n){
    for (int i = m,j = 0; i < m + n; ++i, ++j) {
        nums1[i] = nums2[j];
    }
    qsort(nums1, n + m, 4, comparator);
}