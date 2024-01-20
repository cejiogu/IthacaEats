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
            Restaurant(name = "Okenshields", description = "Central"),
            Restaurant(name = "Morrison", description = "North"),
            Restaurant(name = "Bethe", description = "West"),
            Restaurant(name = "Appel", description = "North"),
            Restaurant(name = "Alice Cook", description = "West"),
            Restaurant(name = "Terrace", description = "Central"),
            Restaurant(name = "Trillium", description = "Central"),
            Restaurant(name = "Mattin's", description = "Central"),
            Restaurant(name = "Becker", description = "West"),
            Restaurant(name = "Zeus", description = "Central")
        )

        val recyclerView : RecyclerView = findViewById(R.id.recycler)
        recyclerView.layoutManager = LinearLayoutManager(this)
        recyclerView.adapter = RestaurantAdapter(exampleRestaurants)
    }
}