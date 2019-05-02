package com.example.myapplication;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class GameOverActivity extends AppCompatActivity {

    private Button playButton;
    private Button quitButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_game_over);

        this.playButton = findViewById(R.id.playButton);
        this.quitButton = findViewById(R.id.quitButton);

        this.playButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent gameActivity = new Intent(getApplicationContext(), GameActivity.class);
                startActivity(gameActivity);
                finish();
            }
        });

        this.quitButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                finish();
            }
        });
    }
}
