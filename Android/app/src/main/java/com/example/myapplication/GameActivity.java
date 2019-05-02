package com.example.myapplication;
import android.content.Context;
import android.content.Intent;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.os.Bundle;
import android.support.v7.app.ActionBar;
import android.support.v7.app.AppCompatActivity;
import android.util.DisplayMetrics;
import android.util.Log;
import android.view.MotionEvent;
import android.view.View;
import android.view.ViewGroup;
import android.view.WindowManager;
import android.widget.FrameLayout;
import android.widget.ImageView;
import android.widget.TextView;

import com.example.myapplication.assets.Meteor;
import com.example.myapplication.assets.SpaceShip;

import java.util.ArrayList;
import java.util.List;

public class GameActivity extends AppCompatActivity implements SensorEventListener, View.OnTouchListener {

    final String TAG="App";
    SensorManager mSensorManager;
    private Sensor mAccelerometer;
    private Sensor mLight;
    public SpaceShip spaceShip = null;
    private FrameLayout canvasLayout = null;
    private float height;
    private float width;
    private float lightValue;
    private List<Meteor> meteorList = new ArrayList();
    private int nbMeteorMax = 6;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_game);
        if(mSensorManager == null) {
            mSensorManager = (SensorManager) getSystemService(Context.SENSOR_SERVICE);
        }
        mAccelerometer = mSensorManager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER);
        mLight = mSensorManager.getDefaultSensor(Sensor.TYPE_LIGHT);
        // on créé notre spaceShip
        spaceShip = new SpaceShip(getApplicationContext());

        // on place ajoute notre spaceShip à notre app layout
        this.getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,WindowManager.LayoutParams.FLAG_FULLSCREEN);
        canvasLayout = findViewById(R.id.appViewLayout);
        canvasLayout.addView(this.spaceShip);


        //Get screen size
        DisplayMetrics displayMetrics = new DisplayMetrics();
        getWindowManager().getDefaultDisplay().getMetrics(displayMetrics);
        this.height = displayMetrics.heightPixels;
        this.width = displayMetrics.widthPixels;


    }

    @Override
    protected void onResume(){
        super.onResume();
        if(mSensorManager != null){
            mSensorManager.registerListener(this,mAccelerometer,SensorManager.SENSOR_DELAY_FASTEST);
            mSensorManager.registerListener(this, mLight, SensorManager.SENSOR_DELAY_FASTEST);
        }
    }

    @Override
    public void onSensorChanged(SensorEvent event) {
        if(event.sensor.getType() == Sensor.TYPE_ACCELEROMETER){
            float Ax = event.values[0];
            float Ay = event.values[1];
            float Az = event.values[2];
            Log.v(TAG, String.format("TimeAcc = %s | Ax = %s Ay = %s Az = %s", event.timestamp, Ax, Ay, Az));

            ImageView spaceShipView = findViewById(R.id.spaceShipView);
            spaceShip.move(spaceShipView, Ax, Ay, this.height,this.width);
            moveMeteor();

        }
        else if(event.sensor.getType() == Sensor.TYPE_LIGHT) {
            float lightValue = event.values[0];
            TextView score = findViewById(R.id.scoreValue);
            score.setText(""+lightValue);
            this.lightValue = lightValue;
            if (meteorList.size() < nbMeteorMax) {
                createMeteor(lightValue);
            }
        }
    }

    public void createMeteor(float light) {
        Meteor m = new Meteor(this);
        m.move((int) light, (int) (Math.random()*(-1000)));
        meteorList.add(m);
        canvasLayout.addView(m.getMeteorImage());
    }

    public void moveMeteor() {
        for(int i=0; i<meteorList.size(); i++) {
            Log.v(TAG, String.format("size %s", meteorList.size()));
            //int meteorPosX = meteorList.get(i).getPosX();
            Meteor meteor = meteorList.get(i);
            meteor.move((int) (Math.random()*15-7.5), 3);

            if(meteor.getPosY() > height) {
                //canvasLayout.removeView(meteor.getMeteorImage());
                //meteorList.remove(meteor);
                int scale = (int) (lightValue/1000 * width);
                meteor.setPosY(0);
                meteor.setPosX(scale);
            }

            /*if((spaceShip.getPosX() < meteor.getPosX() + meteor.width() && spaceShip.getPosX() > meteor.getPosX()) ||
                    (spaceShip.getPosX() < meteor.getPosX() && spaceShip.getPosX() + spaceShip.width() > meteor.getPosX())) {
                if((spaceShip.getPosY() < meteor.getPosY() + meteor.height() && spaceShip.getPosY() > meteor.getPosY()) ||
                        (spaceShip.getPosY() < meteor.getPosY() && spaceShip.getPosY() + spaceShip.height() > meteor.getPosY())) {
                    //Intent gameOverActivity = new Intent(getApplicationContext(), GameOverActivity.class);
                    //startActivity(gameOverActivity);
                    finish();
                }
            }*/
        }
    }

    @Override
    public void onAccuracyChanged(Sensor sensor, int accuracy) {

    }

    @Override
    public boolean onTouch(View v, MotionEvent event) {
        return false;
        /*if (v instanceof FrameLayout) {
            this.canvasLayout.addView(this.spaceShip.shoot());
            return true;
        }
        else {
            return false;
        }*/
        // If user touch the custom SurfaceView object.
       /* if(view instanceof SurfaceView) {

            // Create and set a red paint to custom surfaceview.
            float x = event.getX();
            float y = event.getY();


            // Tell android os the onTouch event has been processed.
            return true;
        }else
        {
            // Tell android os the onTouch event has not been processed.
            return false;
        }*/
    }

    @Override
    public boolean onTouchEvent(MotionEvent event){
        float x = event.getX();
        float y = event.getY();
        ImageView spaceShipView = findViewById(R.id.spaceShipView);
        spaceShip.drawRotate(spaceShipView, x,y);
        return true;
    }

}
