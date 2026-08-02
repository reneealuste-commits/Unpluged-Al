const unpleasantFeelings = [
  'šokeeritud',
  'frustreeritud',
  'pinges',
  'stressis',
  'närviline',
  'rahutu',
  'mures',
  'ärritunud',
  'vihane',
  'pettunud',
  'üksildane',
  'haavatud',
  'hirmul',
  'kurb',
  'väsinud',
  'ülekoormatud',
];

const pleasantFeelings = [
  'rahulik',
  'tänulik',
  'rõõmus',
  'hoitud',
  'kindel',
  'lootusrikas',
  'energiline',
  'rahul',
  'hell',
  'uudishimulik',
];

List<String> feelingsForUnpleasantness(double value) {
  return value >= 0.5 ? unpleasantFeelings : pleasantFeelings;
}
