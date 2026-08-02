import 'package:flutter/material.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:intl/date_symbol_data_local.dart';

import 'screens/home_screen.dart';
import 'services/storage_service.dart';
import 'theme/app_theme.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await initializeDateFormatting('et');
  runApp(const AjuVabadusApp());
}

class AjuVabadusApp extends StatelessWidget {
  const AjuVabadusApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Aju vabadus',
      debugShowCheckedModeBanner: false,
      theme: buildAppTheme(),
      locale: const Locale('et'),
      supportedLocales: const [Locale('et')],
      localizationsDelegates: const [
        GlobalMaterialLocalizations.delegate,
        GlobalWidgetsLocalizations.delegate,
        GlobalCupertinoLocalizations.delegate,
      ],
      home: HomeScreen(storage: StorageService()),
    );
  }
}
