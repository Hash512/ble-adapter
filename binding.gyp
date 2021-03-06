{
  'targets': [
    {
      'target_name': 'ble-adapter-native',
      'conditions': [
        ['OS=="win"', {
          'sources': [ 'src/ble_adapter.cc' ],
          'include_dirs': ["<!(node -e \"require('nan')\")"],
          'cflags!': [ '-fno-exceptions' ],
          'cflags_cc!': [ '-fno-exceptions' ],
          'msvs_settings': {
            'VCCLCompilerTool': { 'ExceptionHandling': 1 },
          }
        }]
      ]
    }
  ]
}