import 'package:flutter/material.dart';
import 'package:price_predictor/screens/home_page.dart';
import 'package:price_predictor/screens/input_page.dart';
import 'package:price_predictor/screens/result_page.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await dotenv.load(fileName: ".env");
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      initialRoute: "/home",
      routes: {
        "/home": (context) => Home(),
        "/result": (context) => Result(),
        "/input": (context) => Input(),
      },
    );
  }
}
