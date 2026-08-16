import 'package:flutter/material.dart';

import '../data/feelings.dart';
import '../data/needs.dart';
import '../models/interaction.dart';
import '../services/storage_service.dart';
import '../theme/app_theme.dart';
import '../widgets/step_scaffold.dart';
import '../widgets/vertical_mood_slider.dart';

class NewInteractionFlow extends StatefulWidget {
  const NewInteractionFlow({
    super.key,
    required this.storage,
    required this.interaction,
  });

  final StorageService storage;
  final Interaction interaction;

  @override
  State<NewInteractionFlow> createState() => _NewInteractionFlowState();
}

class _NewInteractionFlowState extends State<NewInteractionFlow> {
  late Interaction _draft;
  int _step = 0;
  late final TextEditingController _observationController;
  late final TextEditingController _requestController;
  final Set<String> _selectedFeelings = {};
  final Set<String> _selectedNeeds = {};

  @override
  void initState() {
    super.initState();
    _draft = widget.interaction;
    _observationController = TextEditingController(text: _draft.observation);
    _requestController = TextEditingController(text: _draft.request);
    _selectedFeelings.addAll(_draft.feelings);
    _selectedNeeds.addAll(_draft.needs);
  }

  @override
  void dispose() {
    _observationController.dispose();
    _requestController.dispose();
    super.dispose();
  }

  void _next() {
    if (_step < 5) {
      setState(() => _step++);
    } else {
      final result = _draft.copyWith(
        observation: _observationController.text.trim(),
        feelings: _selectedFeelings.toList(),
        needs: _selectedNeeds.toList(),
        request: _requestController.text.trim(),
      );
      Navigator.pop(context, result);
    }
  }

  void _back() {
    if (_step > 0) {
      setState(() => _step--);
    } else {
      Navigator.pop(context);
    }
  }

  @override
  Widget build(BuildContext context) {
    switch (_step) {
      case 0:
        return _observationStep();
      case 1:
        return _energyStep();
      case 2:
        return _unpleasantnessStep();
      case 3:
        return _feelingsStep();
      case 4:
        return _needsStep();
      case 5:
        return _requestStep();
      default:
        return _observationStep();
    }
  }

  Widget _observationStep() {
    return StepScaffold(
      title: 'Tähelepanek',
      helpText:
          'Kirjelda, mis juhtus. Proovi vältida sõnu, mis hinnangut annavad '
          'või teiste kavatsusi oletavad.',
      onBack: _back,
      onNext: _next,
      body: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const Text(
            'Kirjelda, mis juhtus. Proovi mitte kasutada sõnu, mis annavad '
            'hinnangu või eeldavad teiste kavatsusi või tundeid.',
          ),
          const SizedBox(height: 16),
          const Text(
            'Proovi alustada lausega:',
            style: TextStyle(fontWeight: FontWeight.w600),
          ),
          const Text('"Kui ma näen/kuulen…"'),
          const SizedBox(height: 16),
          TextField(
            controller: _observationController,
            maxLines: 6,
            decoration: const InputDecoration(
              hintText: 'Kui ma näen, et…',
            ),
          ),
        ],
      ),
    );
  }

  Widget _energyStep() {
    return StepScaffold(
      title: 'Energia',
      onBack: _back,
      onNext: _next,
      body: Column(
        children: [
          const Text(
            'Kuidas sa end tunned?',
            style: TextStyle(fontSize: 18),
            textAlign: TextAlign.center,
          ),
          const SizedBox(height: 8),
          const Text(
            'Liiguta slaidi üles-alla. Kui sa ei tunne midagi – vali lihtsalt '
            'keskmine.',
            textAlign: TextAlign.center,
            style: TextStyle(color: AppColors.textSecondary),
          ),
          const SizedBox(height: 24),
          SizedBox(
            height: 320,
            child: VerticalMoodSlider(
              value: _draft.energy,
              onChanged: (v) => setState(() => _draft = _draft.copyWith(energy: v)),
              gradient: const LinearGradient(
                begin: Alignment.topCenter,
                end: Alignment.bottomCenter,
                colors: [AppColors.energyTop, AppColors.energyBottom],
              ),
              topIcon: Icons.bolt,
              topLabel: 'palju',
              bottomIcon: Icons.bolt_outlined,
              bottomLabel: 'vähe',
            ),
          ),
        ],
      ),
    );
  }

  Widget _unpleasantnessStep() {
    return StepScaffold(
      title: 'Ebameeldivus',
      onBack: _back,
      onNext: _next,
      body: Column(
        children: [
          const Text(
            'Kuidas sa end tunned?',
            style: TextStyle(fontSize: 18),
            textAlign: TextAlign.center,
          ),
          const SizedBox(height: 24),
          SizedBox(
            height: 320,
            child: VerticalMoodSlider(
              value: _draft.unpleasantness,
              onChanged: (v) =>
                  setState(() => _draft = _draft.copyWith(unpleasantness: v)),
              gradient: const LinearGradient(
                begin: Alignment.topCenter,
                end: Alignment.bottomCenter,
                colors: [AppColors.unpleasantTop, AppColors.unpleasantBottom],
              ),
              topIcon: Icons.sentiment_dissatisfied,
              bottomIcon: Icons.sentiment_satisfied_alt,
            ),
          ),
        ],
      ),
    );
  }

  Widget _feelingsStep() {
    final options = feelingsForUnpleasantness(_draft.unpleasantness);
    return StepScaffold(
      title: 'Tunded',
      helpText:
          'Vali üks või mitu sõna. Kui ükski ei sobi – jäta valimata ja '
          'mine edasi.',
      onBack: _back,
      onNext: _next,
      body: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          if (_observationController.text.isNotEmpty) ...[
            const Text(
              'Tähelepanek:',
              style: TextStyle(fontWeight: FontWeight.w600),
            ),
            Text(
              _observationController.text,
              style: const TextStyle(color: AppColors.textSecondary),
            ),
            const SizedBox(height: 16),
          ],
          const Text('Millised tunded on sinus?'),
          const SizedBox(height: 12),
          Wrap(
            spacing: 8,
            runSpacing: 8,
            children: options.map((word) {
              final selected = _selectedFeelings.contains(word);
              return SelectableChip(
                label: word,
                selected: selected,
                onTap: () {
                  setState(() {
                    if (selected) {
                      _selectedFeelings.remove(word);
                    } else {
                      _selectedFeelings.add(word);
                    }
                  });
                },
              );
            }).toList(),
          ),
        ],
      ),
    );
  }

  Widget _needsStep() {
    return StepScaffold(
      title: 'Vajadused',
      helpText:
          'Mis on sinus elus oluline? Vajadus on universaalne – mitte konkreetne '
          'inimene või asi.',
      onBack: _back,
      onNext: _next,
      body: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const Text('Millised vajadused on taga?'),
          const SizedBox(height: 12),
          Wrap(
            spacing: 8,
            runSpacing: 8,
            children: commonNeeds.map((word) {
              final selected = _selectedNeeds.contains(word);
              return SelectableChip(
                label: word,
                selected: selected,
                onTap: () {
                  setState(() {
                    if (selected) {
                      _selectedNeeds.remove(word);
                    } else {
                      _selectedNeeds.add(word);
                    }
                  });
                },
              );
            }).toList(),
          ),
        ],
      ),
    );
  }

  Widget _requestStep() {
    return StepScaffold(
      title: 'Palve',
      helpText:
          'Sõnasta konkreetne, tehtav palve. Alusta: "Kas sa oleksid nõus…"',
      onBack: _back,
      onNext: _next,
      nextLabel: 'SALVESTA',
      body: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const Text(
            'Mida sa praegu vajad? Kirjuta selge palve – endale või teisele.',
          ),
          const SizedBox(height: 16),
          TextField(
            controller: _requestController,
            maxLines: 5,
            decoration: const InputDecoration(
              hintText: 'Kas sa oleksid nõus…',
            ),
          ),
          const SizedBox(height: 24),
          _summaryPreview(),
        ],
      ),
    );
  }

  Widget _summaryPreview() {
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(4),
        border: Border.all(color: const Color(0xFFE0E0E0)),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const Text(
            'Kokkuvõte',
            style: TextStyle(fontWeight: FontWeight.w600),
          ),
          const SizedBox(height: 8),
          if (_observationController.text.isNotEmpty)
            Text('Kui ma näen/kuulen: ${_observationController.text}'),
          if (_selectedFeelings.isNotEmpty)
            Text('Tunnen: ${_selectedFeelings.join(', ')}'),
          if (_selectedNeeds.isNotEmpty)
            Text('Sest vajan: ${_selectedNeeds.join(', ')}'),
          if (_requestController.text.isNotEmpty)
            Text('Palun: ${_requestController.text}'),
        ],
      ),
    );
  }
}
