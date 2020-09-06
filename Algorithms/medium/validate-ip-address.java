class Solution {
    public String validIPAddress(String IP) {
        if (isIPv4(IP)) return "IPv4";
        if (isIPv6(IP)) return "IPv6";
        return "Neither";
    }

    private boolean isIPv4(String IP) {
        if (IP.length() < 1 || IP.charAt(IP.length() - 1) == '.') return false;
        String[] pieces = IP.split("\\.");
        if (pieces.length != 4) return false;
        for (int i = 0; i < 4; i++) {
            if (pieces[i].length() > 4 ||
                    pieces[i].length() < 1) return false;
            if (pieces[i].length() > 1 && pieces[i].charAt(0) == '0') return false;
            for (int j = 0; j < pieces[i].length(); j++) {
                char x = pieces[i].charAt(j);
                if (!Character.isDigit(x) || x == ' ') return false;
            }
            if (Integer.parseInt(pieces[i]) > 255) return false;
        }
        return true;
    }
    private boolean isIPv6(String IP) {
        if (IP.length() < 1 || IP.charAt(IP.length() - 1) == ':') return false;
        String[] pieces = IP.split("\\:");
        if (pieces.length != 8) return false;
        for (int i = 0; i < 8; i++) {
            if (pieces[i].length() > 4 ||
                    pieces[i].length() < 1) return false;
            for (int j = 0; j < pieces[i].length(); j++) {
                char x = pieces[i].charAt(j);
                if (!Character.isDigit(x) &&
                        !((x >= 'A') && (x <= 'F') || (x >= 'a') && (x <= 'f'))) return false;
            }
        }
        return true;
    }
}