import 'package:electra_wheels/evstation/homepage.dart';
import 'package:electra_wheels/servicecenter/addspares.dart';
import 'package:electra_wheels/servicecenter/listoforders.dart';
import 'package:electra_wheels/servicecenter/paymentstatus.dart';
import 'package:electra_wheels/servicecenter/serhomepage.dart';
import 'package:electra_wheels/user/chargingstdetails.dart';
import 'package:electra_wheels/user/location.dart';
import 'package:electra_wheels/user/paymentscreen.dart';
import 'package:electra_wheels/user/slotbooking.dart';
import 'package:electra_wheels/user/userhomepage.dart';
import 'package:electra_wheels/user/viewservice.dart';
import 'package:electra_wheels/user/viewstation.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: //ChargingStationsMap(),
          //PaymentScreen(),
          //SlotBookingScreen(),
          //ServiceAndSparesScreen(),
          //ChargingStationScreen(),
          // Userhomepage(),
          //LocationPage(),
          //NearbyLocationsScreen(),
          // EVStationHomePage(),
          //AddSparesPage(),

// OrderListScreen(),
          ServiceCenterHomepage(),
    );
  }
}
