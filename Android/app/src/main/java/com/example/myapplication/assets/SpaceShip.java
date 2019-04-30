package com.example.myapplication.assets;

import android.app.ActionBar;
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
import android.view.ViewGroup;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.widget.LinearLayout;

import com.example.myapplication.R;
import com.example.myapplication.tmp.MySurfaceView;

import java.util.ArrayList;
import java.util.List;

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
    private List<ImageView> rocketList = new ArrayList();

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

    public void move(ImageView spaceShipView, float x, float y, float maxx, float maxy) {
        // Get and lock canvas object from surfaceHolder.

        if (spaceShipView != null) {
            posx = posx - 2 * x;
            posy = posy + 2 * y;

            if (posx<-300){
                posx=maxx-300;
            }
            if (posx>maxx-300){
                posx=-300;
            }
            if (posy<-300){
                posy=maxy+300;
            }
            if (posy>maxy+300){
                posy=-300;
            }

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
    public void drawRotate(ImageView spaceShipView, float x, float y) {
        // Get and lock canvas object from surfaceHolder.

        if (spaceShipView != null) {
            float angle = (float) Math.toDegrees(Math.atan2(y - posy-300, x - posx-300))+90;

            if(angle < 0){
                angle += 360;
            }
            spaceShipView.setRotation(angle);

        }
    }

    public ImageView shoot() {
        ImageView rocketImage = new ImageView(this.getContext());
        ViewGroup.LayoutParams params = new ActionBar.LayoutParams(400, 400);
        rocketImage.setLayoutParams(params);
        rocketImage.setBackgroundResource(R.drawable.rocket);
        this.rocketList.add(rocketImage);
        return rocketImage;
    }

    public float getPosX() {
        return posx;
    }

    public float getPosY() {
        return posy;
    }

    public int width() {
        return width;
    }

    public int height() {
        return height;
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
