package com.example.myapplication;
import android.content.Context;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.MotionEvent;
import android.view.SurfaceView;
import android.view.View;
import android.view.WindowManager;
import android.widget.LinearLayout;

import com.example.myapplication.assets.SpaceShip;

public class App extends AppCompatActivity implements SensorEventListener, View.OnTouchListener {

    final String TAG="App";
    SensorManager mSensorManager;
    private Sensor mAccelerometer;
    public SpaceShip spaceShip = null;
    private LinearLayout canvasLayout = null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        if(mSensorManager == null) {
            mSensorManager = (SensorManager) getSystemService(Context.SENSOR_SERVICE);
        }
        mAccelerometer = mSensorManager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER);
        // on créé notre spaceShip
        spaceShip = new SpaceShip(getApplicationContext());

        // on place ajoute notre spaceShip à notre app layout
        this.getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,WindowManager.LayoutParams.FLAG_FULLSCREEN);
        canvasLayout = findViewById(R.id.appViewLayout);
        canvasLayout.addView(this.spaceShip);
    }

    @Override
    protected void onResume(){
        super.onResume();
        if(mSensorManager != null){
            mSensorManager.registerListener(this,mAccelerometer,SensorManager.SENSOR_DELAY_NORMAL);
        }
    }

    @Override
    public void onSensorChanged(SensorEvent event) {
        if(event.sensor.getType() == Sensor.TYPE_ACCELEROMETER){
            float Ax = event.values[0];
            float Ay = event.values[1];
            float Az = event.values[2];
            Log.v(TAG, String.format("TimeAcc = %s | Ax = %s Ay = %s Az = %s", event.timestamp, Ax, Ay, Az));
            spaceShip.posx  = spaceShip.posx - 2 *Ax ;
            spaceShip.posy = spaceShip.posy + 2 *Ay ;
            spaceShip.draw(spaceShip.posx,spaceShip.posy);
        }
    }

    @Override
    public void onAccuracyChanged(Sensor sensor, int accuracy) {

    }

    @Override
    public boolean onTouch(View v, MotionEvent event) {
        return false;
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
}
