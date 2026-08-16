import 'package:flutter_test/flutter_test.dart';
import 'package:ajuvabadus/main.dart';

void main() {
  testWidgets('App loads home screen', (WidgetTester tester) async {
    await tester.pumpWidget(const AjuVabadusApp());
    await tester.pumpAndSettle();

    expect(find.text('Aju vabadus'), findsOneWidget);
    expect(find.text('UUS VESTLUS'), findsOneWidget);
  });
}
