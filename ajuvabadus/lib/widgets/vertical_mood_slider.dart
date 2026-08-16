import 'package:flutter/material.dart';

class VerticalMoodSlider extends StatelessWidget {
  const VerticalMoodSlider({
    super.key,
    required this.value,
    required this.onChanged,
    required this.gradient,
    required this.topIcon,
    this.bottomIcon,
    this.topLabel,
    this.bottomLabel,
  });

  final double value;
  final ValueChanged<double> onChanged;
  final Gradient gradient;
  final IconData topIcon;
  final IconData? bottomIcon;
  final String? topLabel;
  final String? bottomLabel;

  @override
  Widget build(BuildContext context) {
    return LayoutBuilder(
      builder: (context, constraints) {
        final height = constraints.maxHeight.clamp(200.0, 400.0);
        return Center(
          child: SizedBox(
            height: height,
            width: 120,
            child: Stack(
              alignment: Alignment.center,
              children: [
                Container(
                  width: 56,
                  height: height,
                  decoration: BoxDecoration(
                    gradient: gradient,
                    borderRadius: BorderRadius.circular(28),
                  ),
                ),
                RotatedBox(
                  quarterTurns: 3,
                  child: SliderTheme(
                    data: SliderTheme.of(context).copyWith(
                      trackHeight: 56,
                      thumbShape: const RoundSliderThumbShape(
                        enabledThumbRadius: 14,
                      ),
                      overlayShape: const RoundSliderOverlayShape(
                        overlayRadius: 22,
                      ),
                      activeTrackColor: Colors.white.withValues(alpha: 0.3),
                      inactiveTrackColor: Colors.transparent,
                      thumbColor: Colors.white,
                    ),
                    child: Slider(
                      value: value,
                      onChanged: onChanged,
                    ),
                  ),
                ),
                Positioned(
                  top: 8,
                  child: Column(
                    children: [
                      Icon(topIcon, color: Colors.white, size: 28),
                      if (topLabel != null)
                        Text(
                          topLabel!,
                          style: const TextStyle(
                            color: Colors.white,
                            fontSize: 11,
                          ),
                        ),
                    ],
                  ),
                ),
                if (bottomIcon != null)
                  Positioned(
                    bottom: 8,
                    child: Column(
                      children: [
                        if (bottomLabel != null)
                          Text(
                            bottomLabel!,
                            style: const TextStyle(
                              color: Colors.white70,
                              fontSize: 11,
                            ),
                          ),
                        Icon(bottomIcon, color: Colors.white70, size: 28),
                      ],
                    ),
                  ),
              ],
            ),
          ),
        );
      },
    );
  }
}
