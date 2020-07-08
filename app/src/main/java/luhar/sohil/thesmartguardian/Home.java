package luhar.sohil.thesmartguardian;

import android.support.annotation.NonNull;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;
import com.google.firebase.iid.FirebaseInstanceId;
import com.squareup.picasso.Picasso;

import luhar.sohil.thesmartguardian.Common.Common;
import luhar.sohil.thesmartguardian.Model.Message;
import luhar.sohil.thesmartguardian.Model.Parent;
import luhar.sohil.thesmartguardian.Model.Student;
import luhar.sohil.thesmartguardian.Model.Token;

public class Home extends AppCompatActivity {

    TextView wlcmUser,tvdate,tvmsg;
    ImageView ivstdPhoto;


    FirebaseDatabase firebaseDatabase;
    DatabaseReference student,message;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home);

        wlcmUser = (TextView) findViewById(R.id.wlcmUser);
        tvdate = (TextView) findViewById(R.id.date);
        tvmsg = (TextView) findViewById(R.id.msg);
        ivstdPhoto = (ImageView) findViewById(R.id.stdphoto);


        if (Common.haveInternet(this)) {
            String msg = "Hello ! " + Common.currentParent.getName();
            wlcmUser.setText(msg);

            firebaseDatabase = FirebaseDatabase.getInstance();
            student = firebaseDatabase.getReference("Student");
            message = firebaseDatabase.getReference("Message");

            Log.d("datastudent", Common.currentParent.getPhone());


            student.addValueEventListener(new ValueEventListener() {

                @Override
                public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
                    for (DataSnapshot ds : dataSnapshot.getChildren()) {
                        Student student = ds.getValue(Student.class);
                        Log.d("datastudent", student.getParent_phone());
                        Log.d("datastudent", Common.currentParent.getPhone());

                        if (student.getParent_phone().equals(Common.currentParent.getPhone())) {
                            Common.currentStudent = student;
                            Log.d("datastudent", Common.currentStudent.getName());
                            break;
                        }
                    }

                    /*
                    Student student=dataSnapshot.child().getValue(Student.class);

                    Log.d("datastudent","Name"+dataSnapshot.child("name").getValue().toString());
                    if(student.getName().equals(Common.currentParent.getPhone()))
                         Common.currentStudent=student;*/
                }

                @Override
                public void onCancelled(@NonNull DatabaseError databaseError) {
                    Log.d("datastudent", "here in cancelled");
                }
            });


            message.addValueEventListener(new ValueEventListener() {
                @Override
                public void onDataChange(@NonNull DataSnapshot dataSnapshot) {

                    Log.d("message", "Here");
                    if (dataSnapshot.child(Common.currentStudent.getId()).exists()) {
                        Message m = dataSnapshot.child(Common.currentStudent.getId()).getValue(Message.class);
                        Common.currentMessage = m;
                        Log.d("message", Common.currentMessage.getMessage());
                        setmsg();
                        updateToken(FirebaseInstanceId.getInstance().getToken());
                    }
                }

                @Override
                public void onCancelled(@NonNull DatabaseError databaseError) {

                }
            });


        } else {
            Toast.makeText(this, "Please check your internet connection! ", Toast.LENGTH_SHORT).show();
        }


    }


    private void updateToken(String token) {
        FirebaseDatabase db=FirebaseDatabase.getInstance();
        DatabaseReference tokens=db.getReference("Tokens");
        Token data=new Token(token,false);
        tokens.child(Common.currentStudent.getId()).setValue(data);
    }

    void setmsg(){
        String date="Date: "+Common.currentMessage.getDate();
        String msg=Common.currentMessage.getMessage();
        String url=Common.currentMessage.getPhoto();
        tvdate.setText(date);
        tvmsg.setText(msg);
        Log.d("SetContent",url);
        Picasso.get().load(url).into(ivstdPhoto);

    }

}
