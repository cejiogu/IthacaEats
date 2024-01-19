package com.example.ithacaeats

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.ImageView
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView

class RestaurantAdapter(
    val restaurantList: List<Restaurant>
) : RecyclerView.Adapter<RestaurantAdapter.RestaurantViewHolder>() {

    class RestaurantViewHolder(view: View): RecyclerView.ViewHolder(view) {
        val nameText : TextView = view.findViewById(R.id.nameText)
        val descriptionText : TextView = view.findViewById(R.id.descriptionText)
        val image : ImageView = view.findViewById(R.id.restaurantImage)
        val button: Button = view.findViewById(R.id.button)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): RestaurantViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.restaurantcard, parent, false)
        return RestaurantViewHolder(view)
    }

    override fun onBindViewHolder(holder: RestaurantViewHolder, position: Int) {
        val restaurant : Restaurant = restaurantList[position]
        holder.nameText.text = restaurant.name
        holder.descriptionText.text = restaurant.description
    }

    override fun getItemCount(): Int {
        return restaurantList.size
    }
}