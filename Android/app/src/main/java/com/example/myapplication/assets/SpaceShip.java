package com.example.myapplication.assets;

import android.content.Context;
import android.content.res.Resources;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.graphics.PixelFormat;
import android.graphics.drawable.Drawable;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.support.v4.content.ContextCompat;
import android.support.v4.content.res.ResourcesCompat;
import android.util.Log;
import android.view.SurfaceHolder;
import android.view.SurfaceView;
import android.view.View;
import android.widget.ImageView;
import android.widget.LinearLayout;

import com.example.myapplication.R;
import com.example.myapplication.tmp.MySurfaceView;

import static java.lang.Math.*;

public class SpaceShip extends SurfaceView implements SensorEventListener, SurfaceHolder.Callback {

    final String TAG="SPACE SHIP";
    SensorManager mSensorManager;
    private Sensor mGyroscope;
    private SurfaceHolder surfaceHolder = null;
    private int width = 300;
    private int height = 300;
    private float posx = 300;
    private float posy = 300;

    public SpaceShip(Context context) {
        super(context);
        setFocusable(true);
        //this.setBackgroundColor(Color.CYAN);
        if(surfaceHolder == null) {
            // Get surfaceHolder object.
            surfaceHolder = getHolder();
            // Add this as surfaceHolder callback object.
            surfaceHolder.addCallback(this);
        }
        //this.setBackgroundResource(R.drawable.space);
        this.setZOrderOnTop(true);
        this.getHolder().setFormat(PixelFormat.TRANSLUCENT);
    }

    public void draw(ImageView spaceShipView, float x, float y) {
        // Get and lock canvas object from surfaceHolder.

        if (spaceShipView != null) {
            posx = posx - 2 * x;
            posy = posy + 2 * y;

            spaceShipView.setTranslationX(posx);
            spaceShipView.setTranslationY(posy);
            double s = 0.4; // sensor sensitivity
            if ((x>-s) && (x<s)) {
                spaceShipView.setScaleX(1);
            }
            else {
                double t = cos(x*0.2);
                spaceShipView.setScaleX((x > 0) ? ((float) t) : ((float) -t));
            }
        }
    }

    @Override
    public void onSensorChanged(SensorEvent event) {

    }

    @Override
    public void onAccuracyChanged(Sensor sensor, int accuracy) {

    }

    @Override
    public void surfaceCreated(SurfaceHolder holder) {

    }

    @Override
    public void surfaceChanged(SurfaceHolder holder, int format, int width, int height) {

    }

    @Override
    public void surfaceDestroyed(SurfaceHolder holder) {

    }
}
