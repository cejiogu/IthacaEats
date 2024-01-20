package com.example.ithacaeats

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
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

class MainActivity : ComponentActivity() {
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
        recyclerView.adapter = RestaurantAdapter(exampleRestaurants)
    }
}