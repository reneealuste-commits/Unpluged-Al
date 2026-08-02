import 'package:flutter/material.dart';
import 'package:intl/intl.dart';
import 'package:table_calendar/table_calendar.dart';
import 'package:uuid/uuid.dart';

import '../models/interaction.dart';
import '../services/storage_service.dart';
import '../theme/app_theme.dart';
import 'interaction_detail_screen.dart';
import 'new_interaction_flow.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key, required this.storage});

  final StorageService storage;

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  List<Interaction> _interactions = [];
  DateTime _focusedDay = DateTime.now();
  DateTime? _selectedDay;

  static final _monthFormat = DateFormat('MMMM yyyy', 'et');

  @override
  void initState() {
    super.initState();
    _selectedDay = DateTime.now();
    _load();
  }

  Future<void> _load() async {
    final items = await widget.storage.loadInteractions();
    if (!mounted) return;
    setState(() => _interactions = items);
  }

  List<Interaction> _forDay(DateTime day) {
    return _interactions.where((i) {
      return i.createdAt.year == day.year &&
          i.createdAt.month == day.month &&
          i.createdAt.day == day.day;
    }).toList();
  }

  Future<void> _startNew() async {
    final draft = Interaction(
      id: const Uuid().v4(),
      createdAt: DateTime.now(),
    );
    final saved = await Navigator.of(context).push<Interaction>(
      MaterialPageRoute(
        builder: (_) => NewInteractionFlow(
          storage: widget.storage,
          interaction: draft,
        ),
      ),
    );
    if (saved != null) {
      await widget.storage.saveInteraction(saved);
      await _load();
    }
  }

  @override
  Widget build(BuildContext context) {
    final selected = _selectedDay ?? DateTime.now();
    final dayItems = _forDay(selected);
    final unresolved = _interactions.where((i) => !i.resolved).take(5);

    return Scaffold(
      appBar: AppBar(
        title: const Text('Aju vabadus'),
        actions: [
          IconButton(
            icon: const Icon(Icons.info_outline),
            tooltip: 'Info',
            onPressed: () {
              showAboutDialog(
                context: context,
                applicationName: 'Aju vabadus',
                applicationVersion: '1.0.0',
                children: const [
                  Text(
                    'Tasuta tööriist mittevägivaldseks suhtluseks endaga. '
                    'Kirjuta tähelepanek, tunne keha, vali tunded ja vajadused, '
                    'siis sõnasta palve.',
                  ),
                  SizedBox(height: 12),
                  Text(
                    'Kui sa ei tunne midagi – see on okei. Alusta kehast või '
                    'energiast, mitte sundimisest.',
                  ),
                ],
              );
            },
          ),
        ],
      ),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          Text(
            _monthFormat.format(_focusedDay),
            style: Theme.of(context).textTheme.titleMedium?.copyWith(
                  fontWeight: FontWeight.w600,
                ),
            textAlign: TextAlign.center,
          ),
          const SizedBox(height: 8),
          TableCalendar<Interaction>(
            firstDay: DateTime.utc(2020),
            lastDay: DateTime.utc(2030, 12, 31),
            focusedDay: _focusedDay,
            selectedDayPredicate: (day) => isSameDay(_selectedDay, day),
            eventLoader: _forDay,
            locale: 'et',
            startingDayOfWeek: StartingDayOfWeek.monday,
            calendarStyle: const CalendarStyle(
              todayDecoration: BoxDecoration(
                color: Color(0xFFB2DFDB),
                shape: BoxShape.circle,
              ),
              selectedDecoration: BoxDecoration(
                color: AppColors.teal,
                shape: BoxShape.circle,
              ),
              markerDecoration: BoxDecoration(
                color: AppColors.tealDark,
                shape: BoxShape.circle,
              ),
            ),
            headerVisible: false,
            onDaySelected: (selectedDay, focusedDay) {
              setState(() {
                _selectedDay = selectedDay;
                _focusedDay = focusedDay;
              });
            },
            onPageChanged: (focusedDay) {
              setState(() => _focusedDay = focusedDay);
            },
          ),
          const SizedBox(height: 20),
          ElevatedButton(
            onPressed: _startNew,
            child: const Text('UUS VESTLUS'),
          ),
          const SizedBox(height: 24),
          if (dayItems.isNotEmpty) ...[
            Text(
              'Selle päeva kirjed',
              style: Theme.of(context).textTheme.titleSmall,
            ),
            const SizedBox(height: 8),
            ...dayItems.map(_buildTile),
          ],
          if (unresolved.isNotEmpty) ...[
            const SizedBox(height: 16),
            Text(
              'Lahendamata',
              style: Theme.of(context).textTheme.titleSmall,
            ),
            const SizedBox(height: 8),
            ...unresolved.map(_buildTile),
          ],
        ],
      ),
    );
  }

  Widget _buildTile(Interaction item) {
    final month = DateFormat('MMMM', 'et').format(item.createdAt);
    return Card(
      margin: const EdgeInsets.only(bottom: 8),
      child: ListTile(
        title: Text(
          item.preview,
          maxLines: 2,
          overflow: TextOverflow.ellipsis,
        ),
        subtitle: Text(
          item.resolved ? 'Lahendatud · $month' : 'Lahendamata · $month',
          style: TextStyle(
            color: item.resolved ? AppColors.textSecondary : AppColors.tealDark,
          ),
        ),
        onTap: () async {
          await Navigator.of(context).push(
            MaterialPageRoute(
              builder: (_) => InteractionDetailScreen(
                storage: widget.storage,
                interaction: item,
              ),
            ),
          );
          await _load();
        },
      ),
    );
  }
}
