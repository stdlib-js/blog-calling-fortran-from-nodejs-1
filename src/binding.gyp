# file: binding.gyp

# A `.gyp` file for building a Node.js native add-on.
#
# [1]: https://gyp.gsrc.io/docs/InputFormatReference.md
# [2]: https://gyp.gsrc.io/docs/UserDocumentation.md
{
  # Define variables to be used throughout the configuration for all targets:
  'variables': {
    # Set variables based on the host OS:
    'conditions': [
      [
        'OS=="win"',
        {
          # Define the object file suffix on Windows:
          'obj': 'obj',
        },
        {
          # Define the object file suffix for other operating systems (e.g., Linux and MacOS):
          'obj': 'o',
        }
      ],
    ],
  },

  # Define compilation targets:
  'targets': [
    # Define a target to generate an add-on:
    {
      # The target name should match the add-on export name (see addon.c above):
      'target_name': 'addon',

      # List of source files:
      'sources': [
        # Relative paths should be relative to this configuration file...
        './addon.c',
        './mul.f90',
      ],

      # List directories which contain relevant headers to include during compilation:
      'include_dirs': [
        # Relative paths should be relative to this configuration file...
        './',
      ],

      # Define settings which should be applied when a target's object files are used as linker input:
      'link_settings': {
        # Define linker flags for libraries against which to link (e.g., '-lm', '-lblas', etc):
        'libraries': [],

        # Define directories in which to find libraries to link to (e.g., '/usr/lib'):
        'library_dirs': []
      },

      # Define custom build actions for particular source files:
      'rules': [
        {
          # Define a rule name:
          'rule_name': 'compile_fortran',

          # Define the filename extension for which this rule should apply:
          'extension': 'f90',

          # Set a flag specifying whether to process generated output as sources for subsequent steps:
          'process_outputs_as_sources': 1,

          # Define the pathnames to be used as inputs when performing processing:
          'inputs': [
            # Full path of the current input:
            '<(RULE_INPUT_PATH)',
          ],

          # Define the outputs produced during processing:
          'outputs': [
            # Store an output object file in a directory for placing intermediate results (only accessible within a single target):
            '<(INTERMEDIATE_DIR)/<(RULE_INPUT_ROOT).<(obj)',
          ],

          # Define the command-line invocation:
          'action': [
            'gfortran',
            '-fno-underscoring',
            '-c',
            '<@(_inputs)',
            '-o',
            '<@(_outputs)',
          ],
        },
      ],
    },
  ],
}
