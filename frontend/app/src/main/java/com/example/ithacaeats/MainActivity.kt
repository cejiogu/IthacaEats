package com.example.ithacaeats

import android.annotation.SuppressLint
import android.content.Intent
import android.net.Uri
import android.os.Bundle
import android.widget.Button
import android.widget.Toast
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.cardview.widget.CardView
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.example.ithacaeats.ui.theme.IthacaEatsTheme

class MainActivity : ComponentActivity(), RestaurantAdapter.AdapterOnClickHandler {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val exampleRestaurants = listOf(
            Restaurant(name = "Okenshields", location = "Central"),
            Restaurant(name = "Morrison", location = "North"),
            Restaurant(name = "Bethe", location = "West"),
            Restaurant(name = "Appel", location = "North"),
            Restaurant(name = "Alice Cook", location = "West"),
            Restaurant(name = "Terrace", location = "Central"),
            Restaurant(name = "Trillium", location = "Central"),
            Restaurant(name = "Mattin's", location = "Central"),
            Restaurant(name = "Becker", location = "West"),
            Restaurant(name = "Zeus", location = "Central")
        )

        val recyclerView : RecyclerView = findViewById(R.id.recycler)
        recyclerView.layoutManager = LinearLayoutManager(this)
        recyclerView.adapter = RestaurantAdapter(exampleRestaurants, this)
    }

    override fun onClick(holder: RestaurantAdapter.RestaurantViewHolder) {
        val restName: String = holder.nameText.text.toString()
        val restLocation: String = holder.locationText.text.toString()

        val intent = Intent(this, RestaurantActivity::class.java)
        intent.putExtra("REST_NAME", restName)
        intent.putExtra("REST_LOCATION", restLocation)
        startActivity(intent)
    }
}