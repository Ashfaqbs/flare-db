"""Apache Beam Runner implementation for executing pipelines on a FlareDB."""

from apache_beam.runners.portability.portable_runner import PortableRunner


class FlareRunner(PortableRunner):
  """A runner for submitting portable Beam pipelines to a FlareDB Job Service."""

  # Inherits run_portable_pipeline (translate/prepare/stage/run) and
  # default_environment from PortableRunner unchanged.
