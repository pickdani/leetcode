class Solution {
    public String destCity(List<List<String>> paths) {
        HashSet<String> sources = new HashSet<String>();
        for (int i=0;i<paths.size();i++) {
            sources.add(paths.get(i).get(0));
        }
        for (int i=0;i<paths.size();i++) {
            if (!sources.contains(paths.get(i).get(1))) {
                return paths.get(i).get(1);
            }
        }
        return null;
    }
}
