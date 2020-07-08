package luhar.sohil.thesmartguardian.Common;

import android.content.Context;
import android.net.ConnectivityManager;
import android.net.NetworkInfo;

import luhar.sohil.thesmartguardian.Model.Message;
import luhar.sohil.thesmartguardian.Model.Parent;
import luhar.sohil.thesmartguardian.Model.Student;

public class Common {
    public static Parent currentParent;
    public static Student currentStudent;
    public static Message currentMessage;

    public static boolean haveInternet(Context ctx) {
        NetworkInfo info = (NetworkInfo) ((ConnectivityManager) ctx.getSystemService(Context.CONNECTIVITY_SERVICE)).getActiveNetworkInfo();
        if (info == null || !info.isConnected()) {
            return false;
        }
        return true;
    }
}
