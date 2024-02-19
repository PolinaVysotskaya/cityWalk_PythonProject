//
//  ViewController.swift
//  Walk
//
//  Created by Маринина Дарья Сергеевна on 14.02.2024.
//

import UIKit
import YandexMapKit
class ViewController: UIViewController {
    @IBOutlet weak var mapView: YMKMapView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        mapView.mapWindow.map.move(
               with: YMKCameraPosition(
                   target: YMKPoint(latitude: 59.935493, longitude: 30.327392),
                   zoom: 15,
                   azimuth: 0,
                   tilt: 0
               ),
               animationType: YMKAnimation(type: YMKAnimationType.smooth, duration: 5),
               cameraCallback: nil)
    }


}

