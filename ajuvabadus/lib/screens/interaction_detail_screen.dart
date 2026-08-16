import 'package:flutter/material.dart';
import 'package:intl/intl.dart';

import '../models/interaction.dart';
import '../services/storage_service.dart';
import '../theme/app_theme.dart';
import 'new_interaction_flow.dart';

class InteractionDetailScreen extends StatelessWidget {
  const InteractionDetailScreen({
    super.key,
    required this.storage,
    required this.interaction,
  });

  final StorageService storage;
  final Interaction interaction;

  @override
  Widget build(BuildContext context) {
    final date = DateFormat('d. MMMM yyyy, HH:mm', 'et').format(
      interaction.createdAt,
    );

    return Scaffold(
      appBar: AppBar(
        title: const Text('Kirje'),
        actions: [
          IconButton(
            icon: Icon(
              interaction.resolved ? Icons.undo : Icons.check_circle_outline,
            ),
            tooltip: interaction.resolved
                ? 'Märgi lahendamata'
                : 'Märgi lahendatuks',
            onPressed: () async {
              await storage.toggleResolved(interaction.id);
              if (context.mounted) Navigator.pop(context);
            },
          ),
        ],
      ),
      body: ListView(
        padding: const EdgeInsets.all(20),
        children: [
          Text(date, style: const TextStyle(color: AppColors.textSecondary)),
          const SizedBox(height: 16),
          _section('Tähelepanek', interaction.observation),
          _section('Energia', '${(interaction.energy * 100).round()}%'),
          _section(
            'Ebameeldivus',
            '${(interaction.unpleasantness * 100).round()}%',
          ),
          _section('Tunded', interaction.feelings.join(', ')),
          _section('Vajadused', interaction.needs.join(', ')),
          _section('Palve', interaction.request),
        ],
      ),
      bottomNavigationBar: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(16),
          child: OutlinedButton(
            onPressed: () async {
              final updated = await Navigator.of(context).push<Interaction>(
                MaterialPageRoute(
                  builder: (_) => NewInteractionFlow(
                    storage: storage,
                    interaction: interaction,
                  ),
                ),
              );
              if (updated != null) {
                await storage.saveInteraction(updated);
                if (context.mounted) Navigator.pop(context);
              }
            },
            child: const Text('MUUDA'),
          ),
        ),
      ),
    );
  }

  Widget _section(String title, String value) {
    if (value.isEmpty) return const SizedBox.shrink();
    return Padding(
      padding: const EdgeInsets.only(bottom: 16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            title,
            style: const TextStyle(
              fontWeight: FontWeight.w600,
              color: AppColors.tealDark,
            ),
          ),
          const SizedBox(height: 4),
          Text(value),
        ],
      ),
    );
  }
}
