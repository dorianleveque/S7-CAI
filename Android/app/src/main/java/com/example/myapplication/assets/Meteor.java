package com.example.myapplication.assets;

import android.content.Context;
import android.content.res.Resources;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.support.v7.app.ActionBar;
import android.view.SurfaceHolder;
import android.view.SurfaceView;
import android.view.ViewGroup;
import android.widget.ImageView;

import com.example.myapplication.R;

public class Meteor extends SurfaceView implements SensorEventListener, SurfaceHolder.Callback {

    private int posX = 0;
    private int posY = 0;
    private int width = 200;
    private int height= 200;
    private ImageView meteorImage;

    public Meteor(Context context) {
        super(context);
        ImageView meteorImage =  new ImageView(context);
        ViewGroup.LayoutParams params = new ActionBar.LayoutParams(width, height);
        meteorImage.setLayoutParams(params);
        meteorImage.setBackgroundResource(R.drawable.meteor);

        this.meteorImage = meteorImage;
    }

    public void move(int x, int y) {
        posX += x;
        posY += y;
        meteorImage.setTranslationX(posX);
        meteorImage.setTranslationY(posY);
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

    public int getPosX() {
        return posX;
    }

    public void setPosX(int x) {
        this.move(-posX+x,0);
        this.posX = x;
    }

    public int getPosY() {
        return posY;
    }

    public void setPosY(int y) {
        this.move(0,-posY+y);
        this.posY = y;
    }

    public int width() {
        return width;
    }

    public int height() {
        return height;
    }

    public ImageView getMeteorImage() {
        return meteorImage;
    }
}
