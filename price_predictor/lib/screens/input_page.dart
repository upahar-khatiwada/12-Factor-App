import 'package:flutter/material.dart';
import 'package:logger/logger.dart';

final logger = Logger();

class Input extends StatefulWidget {
  const Input({super.key});

  @override
  State<Input> createState() => _InputState();
}

class _InputState extends State<Input> {
  @override
  Widget build(BuildContext context) {
    logger.i("Logger started at input_page.dart");
    final List<TextEditingController> _controllers = List.generate(
      13,
      (_) => TextEditingController(),
    );

    final List<String> _labels = [
      "CRIM (double)",
      "ZN (double)",
      "INDUS (double)",
      "CHAS (int)",
      "NOX (double)",
      "RM (double)",
      "AGE (double)",
      "DIS (double)",
      "RAD (int)",
      "TAX (int)",
      "PTRATIO (double)",
      "B (double)",
      "LSTAT (double)",
    ];

    @override
    void dispose() {
      for (final controller in _controllers) {
        controller.dispose();
      }
      super.dispose();
    }

    void _onPredictPressed() {
      try {
        final double CRIM = double.parse(_controllers[0].text);
        final double ZN = double.parse(_controllers[1].text);
        final double INDUS = double.parse(_controllers[2].text);
        final int CHAS = int.parse(_controllers[3].text);
        final double NOX = double.parse(_controllers[4].text);
        final double RM = double.parse(_controllers[5].text);
        final double AGE = double.parse(_controllers[6].text);
        final double DIS = double.parse(_controllers[7].text);
        final int RAD = int.parse(_controllers[8].text);
        final int TAX = int.parse(_controllers[9].text);
        final double PTRATIO = double.parse(_controllers[10].text);
        final double B = double.parse(_controllers[11].text);
        final double LSTAT = double.parse(_controllers[12].text);

        Navigator.pushNamed(
          context,
          "/result",
          arguments: {
            "CRIM": CRIM,
            "ZN": ZN,
            "INDUS": INDUS,
            "CHAS": CHAS,
            "NOX": NOX,
            "RM": RM,
            "AGE": AGE,
            "DIS": DIS,
            "RAD": RAD,
            "TAX": TAX,
            "PTRATIO": PTRATIO,
            "B": B,
            "LSTAT": LSTAT,
          },
        );
      } catch (e) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text("Please fill all fields correctly")),
        );
        logger.e("Error at input_page.dart: $e");
      }
    }

    return Scaffold(
      appBar: AppBar(
        title: Text(
          "Enter Housing Parameters",
          style: TextStyle(color: Colors.black, fontWeight: FontWeight.bold),
        ),
        backgroundColor: Colors.cyanAccent,
      ),
      body: SafeArea(
        child: SingleChildScrollView(
          padding: EdgeInsets.all(16),
          child: Column(
            children: [
              ...List.generate(13, (index) {
                // spread operator to work on all 13 elements inside list
                return Padding(
                  padding: const EdgeInsets.symmetric(vertical: 8),
                  child: TextField(
                    controller: _controllers[index],
                    decoration: InputDecoration(
                      labelText: _labels[index],
                      border: OutlineInputBorder(),
                    ),
                    keyboardType: TextInputType.number,
                  ),
                );
              }),
              Align(
                alignment: Alignment.bottomRight,
                child: ElevatedButton.icon(
                  onPressed: _onPredictPressed,
                  label: Text("Predict"),
                  icon: Icon(Icons.check),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
