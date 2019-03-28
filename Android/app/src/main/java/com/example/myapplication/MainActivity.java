package com.example.myapplication;

import android.content.Context;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.MotionEvent;
import android.view.SurfaceView;
import android.view.View;
import android.view.WindowManager;
import android.widget.LinearLayout;

public class MainActivity extends AppCompatActivity implements SensorEventListener, View.OnTouchListener {

    final String TAG="sensor";
    SensorManager mSensorManager;
    private Sensor mAccelerometer;
    private Sensor mGyroscope;
    private  MySurfaceView view;
    private LinearLayout canvasLayout = null;
    MySurfaceView customSurfaceView = null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        if(mSensorManager == null) {
            mSensorManager = (SensorManager) getSystemService(Context.SENSOR_SERVICE);
        }
        if(view == null){
            view = new MySurfaceView(this);
        }

        mGyroscope = mSensorManager.getDefaultSensor(Sensor.TYPE_GYROSCOPE);
        mAccelerometer = mSensorManager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER);

        canvasLayout = (LinearLayout) findViewById(R.id.customViewLayout);
        this.getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN, WindowManager.LayoutParams.FLAG_FULLSCREEN);
        customSurfaceView = new MySurfaceView(getApplicationContext());
        customSurfaceView.setOnTouchListener(this);
        canvasLayout.addView(customSurfaceView);
    }

    @Override
    protected void onResume(){
        super.onResume();
        if(mSensorManager != null){
            mSensorManager.registerListener(this,mAccelerometer,SensorManager.SENSOR_DELAY_NORMAL);
            mSensorManager.registerListener(this,mGyroscope,SensorManager.SENSOR_DELAY_NORMAL);

        }
    }

    @Override
    public void onSensorChanged(SensorEvent event) {
        if(event.sensor.getType() == Sensor.TYPE_ACCELEROMETER){
            float Ax = event.values[0];
            float Ay = event.values[1];
            float Az = event.values[2];
            Log.v(TAG, String.format("TimeAcc = %s | Ax = %s Ay = %s Az = %s", event.timestamp, Ax, Ay, Az));
        }
        if(event.sensor.getType() == Sensor.TYPE_GYROSCOPE){
            float Gx = event.values[0];
            float Gy = event.values[1];
            float Gz = event.values[2];
            Log.v(TAG, String.format("TimeAcc = %s | Gx = %s Gy = %s Gz = %s", event.timestamp, Gx, Gy, Gz));
        }
    }

    @Override
    public void onAccuracyChanged(Sensor sensor, int accuracy) {

    }

    @Override
    public boolean onTouch(View v, MotionEvent event) {
        // If user touch the custom SurfaceView object.
        if(view instanceof SurfaceView) {

            // Create and set a red paint to custom surfaceview.
            float x = event.getX();
            float y = event.getY();
            customSurfaceView.drawRedBall(x,y);

            // Tell android os the onTouch event has been processed.
            return true;
        }else
        {
            // Tell android os the onTouch event has not been processed.
            return false;
        }
    }
}
