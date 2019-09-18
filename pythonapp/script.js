function create_table_vals() {
    var rand_temp_val= Math.floor(Math.random()*20);
    var td_1 = document.createElement("td");
    td_1.innerHTML = rand_temp_val;

    var rand_humd_val= Math.floor(Math.random()*20);
    var td_2 = document.createElement("td");
    td_2.innerHTML = rand_humd_val;

    var tbl = document.getElementById("table1");
    var row = document.createElement("tr");

    row.appendChild(td_1);
    row.appendChild(td_2);
    tb1.appendChild(row);

    $(".table_data").css("display","block");
}