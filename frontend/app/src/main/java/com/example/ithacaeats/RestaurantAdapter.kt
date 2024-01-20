package com.example.ithacaeats

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.ImageView
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView

class RestaurantAdapter(
    val restaurantList: List<Restaurant>,
    private val mAdapterOnClickHandler: AdapterOnClickHandler
) : RecyclerView.Adapter<RestaurantAdapter.RestaurantViewHolder>() {

    interface AdapterOnClickHandler {
        fun onClick(position: Int)
    }

    class RestaurantViewHolder(view: View): RecyclerView.ViewHolder(view) {
        val nameText : TextView = view.findViewById(R.id.nameText)
        val locationText : TextView = view.findViewById(R.id.locationText)
//        val image : ImageView = view.findViewById(R.id.restaurantImage)
        val button: Button = view.findViewById(R.id.button)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): RestaurantViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.restaurantcard, parent, false)
        return RestaurantViewHolder(view)
    }

    override fun onBindViewHolder(holder: RestaurantViewHolder, position: Int) {
        val restaurant : Restaurant = restaurantList[position]
        holder.nameText.text = restaurant.name
        holder.locationText.text = restaurant.location

        val button:Button = holder.button
        button.setOnClickListener{
            mAdapterOnClickHandler.onClick(position)
        }
    }

    override fun getItemCount(): Int {
        return restaurantList.size
    }
}