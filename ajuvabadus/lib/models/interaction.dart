class Interaction {
  Interaction({
    required this.id,
    required this.createdAt,
    this.observation = '',
    this.energy = 0.5,
    this.unpleasantness = 0.5,
    this.feelings = const [],
    this.needs = const [],
    this.request = '',
    this.resolved = false,
  });

  final String id;
  final DateTime createdAt;
  final String observation;
  final double energy;
  final double unpleasantness;
  final List<String> feelings;
  final List<String> needs;
  final String request;
  final bool resolved;

  Interaction copyWith({
    String? observation,
    double? energy,
    double? unpleasantness,
    List<String>? feelings,
    List<String>? needs,
    String? request,
    bool? resolved,
  }) {
    return Interaction(
      id: id,
      createdAt: createdAt,
      observation: observation ?? this.observation,
      energy: energy ?? this.energy,
      unpleasantness: unpleasantness ?? this.unpleasantness,
      feelings: feelings ?? this.feelings,
      needs: needs ?? this.needs,
      request: request ?? this.request,
      resolved: resolved ?? this.resolved,
    );
  }

  Map<String, dynamic> toJson() => {
        'id': id,
        'createdAt': createdAt.toIso8601String(),
        'observation': observation,
        'energy': energy,
        'unpleasantness': unpleasantness,
        'feelings': feelings,
        'needs': needs,
        'request': request,
        'resolved': resolved,
      };

  factory Interaction.fromJson(Map<String, dynamic> json) {
    return Interaction(
      id: json['id'] as String,
      createdAt: DateTime.parse(json['createdAt'] as String),
      observation: json['observation'] as String? ?? '',
      energy: (json['energy'] as num?)?.toDouble() ?? 0.5,
      unpleasantness: (json['unpleasantness'] as num?)?.toDouble() ?? 0.5,
      feelings: (json['feelings'] as List<dynamic>?)
              ?.map((e) => e as String)
              .toList() ??
          const [],
      needs: (json['needs'] as List<dynamic>?)
              ?.map((e) => e as String)
              .toList() ??
          const [],
      request: json['request'] as String? ?? '',
      resolved: json['resolved'] as bool? ?? false,
    );
  }

  String get preview {
    if (observation.isNotEmpty) {
      return observation.length > 80
          ? '${observation.substring(0, 80)}…'
          : observation;
    }
    if (feelings.isNotEmpty) return feelings.join(', ');
    return 'Uus vestlus';
  }
}
