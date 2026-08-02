import 'dart:convert';

import 'package:shared_preferences/shared_preferences.dart';

import '../models/interaction.dart';

class StorageService {
  static const _key = 'ajuvabadus_interactions';

  Future<List<Interaction>> loadInteractions() async {
    final prefs = await SharedPreferences.getInstance();
    final raw = prefs.getString(_key);
    if (raw == null) return [];

    final list = jsonDecode(raw) as List<dynamic>;
    return list
        .map((e) => Interaction.fromJson(e as Map<String, dynamic>))
        .toList()
      ..sort((a, b) => b.createdAt.compareTo(a.createdAt));
  }

  Future<void> saveInteraction(Interaction interaction) async {
    final all = await loadInteractions();
    final index = all.indexWhere((i) => i.id == interaction.id);
    if (index >= 0) {
      all[index] = interaction;
    } else {
      all.insert(0, interaction);
    }
    await _persist(all);
  }

  Future<void> deleteInteraction(String id) async {
    final all = await loadInteractions();
    all.removeWhere((i) => i.id == id);
    await _persist(all);
  }

  Future<void> toggleResolved(String id) async {
    final all = await loadInteractions();
    final index = all.indexWhere((i) => i.id == id);
    if (index < 0) return;
    all[index] = all[index].copyWith(resolved: !all[index].resolved);
    await _persist(all);
  }

  Future<void> _persist(List<Interaction> interactions) async {
    final prefs = await SharedPreferences.getInstance();
    final encoded = jsonEncode(interactions.map((i) => i.toJson()).toList());
    await prefs.setString(_key, encoded);
  }
}
