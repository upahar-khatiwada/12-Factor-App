import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:flutter_dotenv/flutter_dotenv.dart';
import 'package:logger/logger.dart';

final logger = Logger();

class Result extends StatefulWidget {
  const Result({super.key});

  @override
  State<Result> createState() => _ResultState();
}

class _ResultState extends State<Result> {
  Map data_from_input = {};
  final String? apiUrl = dotenv.env['API_URL'];
  double? prediction;

  @override
  void initState() {
  super.initState();
  logger.i("Logger started at result_page.dart");
}


  Future<void> getResult(apiUrl) async {
    try {
      print(jsonEncode(data_from_input));
      final response = await http.post(
        Uri.parse(apiUrl),
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode(data_from_input),
      );

      if (response.statusCode == 200) {
        final result = jsonDecode(response.body);
        setState(() {
          prediction = result['result']; //result is the api's key
        });
        logger.i("Prediction value: $prediction at result_page.dart");
      }
    } catch (e) {
      logger.e("There was an error at result_page.dart: $e");
    }
  }

  @override
  Widget build(BuildContext context) {
    if (data_from_input.isEmpty) {
      data_from_input = ModalRoute.of(context)!.settings.arguments as Map;
      setState(() {
        getResult(apiUrl);
      });
    }

    return Scaffold(
      appBar: AppBar(
        title: Text(
          "Result",
          style: TextStyle(color: Colors.black, fontWeight: FontWeight.bold),
        ),
        centerTitle: true,
        backgroundColor: Colors.cyanAccent,
      ),
      body: Center(
        child:
            prediction == null
                ? CircularProgressIndicator()
                : Center(
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Text(
                        "Predicted value: $prediction",
                        style: TextStyle(color: Colors.black, fontSize: 50),
                      ),
                      Center(
                        child: Text(
                          "Hence, the median price of the house is \$${prediction! * 1000}",
                          style: TextStyle(fontSize: 25),
                        ),
                      ),
                    ],
                  ),
                ),
      ),
    );
  }
}
