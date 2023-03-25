use reqwest::blocking::Client;
use serde_json::Value;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Get IP
    let ip_info = reqwest::blocking::get("http://httpbin.org/ip")?.text()?;
    let ip: String = serde_json::from_str::<Value>(&ip_info)?
        .get("origin")
        .and_then(|val| val.as_str())
        .ok_or("Unable to extract IP address")?
        .to_string();
    println!("IP Address: {}", ip);

    // Get GeoLocation - Country
    let client = Client::new();
    let geo_lo = client
        .get(&format!("http://ipinfo.io/{}/country", ip))
        .send()?
        .text()?;
    let loc = geo_lo.trim().to_string();
    println!("Country: {}", loc);

    // Get GeoLocation - City
    let geo_city = client
        .get(&format!("http://ipinfo.io/{}/city", ip))
        .send()?
        .text()?;
    let city = geo_city.trim().to_string();
    println!("City: {}", city);

    // Get GeoLocation - Region
    let geo_region = client
        .get(&format!("http://ipinfo.io/{}/region", ip))
        .send()?
        .text()?;
    let region = geo_region.trim().to_string();
    println!("Region: {}", region);

    Ok(())
}
