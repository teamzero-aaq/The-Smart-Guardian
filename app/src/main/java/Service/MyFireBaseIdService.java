package Service;

import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.iid.FirebaseInstanceId;
import com.google.firebase.iid.FirebaseInstanceIdService;

import luhar.sohil.thesmartguardian.Common.Common;
import luhar.sohil.thesmartguardian.Model.Token;

public class MyFireBaseIdService extends FirebaseInstanceIdService {

    @Override
    public void onTokenRefresh() {
        super.onTokenRefresh();
        String tokenRefreshed =FirebaseInstanceId.getInstance().getToken();
        if (Common.currentParent != null)
            updateTokenToFirebase(tokenRefreshed);
    }

    private void updateTokenToFirebase(String str) {
        FirebaseDatabase db=FirebaseDatabase.getInstance();
        DatabaseReference tokens=db.getReference("Tokens");
        Token token=new Token(str,false);//send from client
        tokens.child(Common.currentParent.getPhone()).setValue(token);
    }
}