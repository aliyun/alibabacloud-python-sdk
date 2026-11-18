# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateKyuubiServiceRequest(DaraModel):
    def __init__(
        self,
        compute_instance: str = None,
        expected_replica: int = None,
        kyuubi_configs: str = None,
        kyuubi_release_version: str = None,
        name: str = None,
        public_endpoint_enabled: bool = None,
        queue: str = None,
        refresh: bool = None,
        release_version: str = None,
        replica: int = None,
        restart: bool = None,
        scale: bool = None,
        spark_configs: str = None,
    ):
        # The specifications of the Kyuubi service.
        self.compute_instance = compute_instance
        # The expected number of instances.
        self.expected_replica = expected_replica
        # The Kyuubi service configurations.
        self.kyuubi_configs = kyuubi_configs
        # The Kyuubi service DPI engine version.
        self.kyuubi_release_version = kyuubi_release_version
        # The name.
        self.name = name
        # Specifies whether to enable public network access.
        self.public_endpoint_enabled = public_endpoint_enabled
        # The running queue for the Kyuubi service.
        self.queue = queue
        # Specifies whether to update the configurations.
        self.refresh = refresh
        # The Spark DPI engine version number.
        self.release_version = release_version
        # The number of replicas enabled for high availability.
        self.replica = replica
        # Specifies whether to restart.
        self.restart = restart
        # Specifies whether to update the number of replicas.
        self.scale = scale
        # The Spark configurations.
        self.spark_configs = spark_configs

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compute_instance is not None:
            result['computeInstance'] = self.compute_instance

        if self.expected_replica is not None:
            result['expectedReplica'] = self.expected_replica

        if self.kyuubi_configs is not None:
            result['kyuubiConfigs'] = self.kyuubi_configs

        if self.kyuubi_release_version is not None:
            result['kyuubiReleaseVersion'] = self.kyuubi_release_version

        if self.name is not None:
            result['name'] = self.name

        if self.public_endpoint_enabled is not None:
            result['publicEndpointEnabled'] = self.public_endpoint_enabled

        if self.queue is not None:
            result['queue'] = self.queue

        if self.refresh is not None:
            result['refresh'] = self.refresh

        if self.release_version is not None:
            result['releaseVersion'] = self.release_version

        if self.replica is not None:
            result['replica'] = self.replica

        if self.restart is not None:
            result['restart'] = self.restart

        if self.scale is not None:
            result['scale'] = self.scale

        if self.spark_configs is not None:
            result['sparkConfigs'] = self.spark_configs

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('computeInstance') is not None:
            self.compute_instance = m.get('computeInstance')

        if m.get('expectedReplica') is not None:
            self.expected_replica = m.get('expectedReplica')

        if m.get('kyuubiConfigs') is not None:
            self.kyuubi_configs = m.get('kyuubiConfigs')

        if m.get('kyuubiReleaseVersion') is not None:
            self.kyuubi_release_version = m.get('kyuubiReleaseVersion')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('publicEndpointEnabled') is not None:
            self.public_endpoint_enabled = m.get('publicEndpointEnabled')

        if m.get('queue') is not None:
            self.queue = m.get('queue')

        if m.get('refresh') is not None:
            self.refresh = m.get('refresh')

        if m.get('releaseVersion') is not None:
            self.release_version = m.get('releaseVersion')

        if m.get('replica') is not None:
            self.replica = m.get('replica')

        if m.get('restart') is not None:
            self.restart = m.get('restart')

        if m.get('scale') is not None:
            self.scale = m.get('scale')

        if m.get('sparkConfigs') is not None:
            self.spark_configs = m.get('sparkConfigs')

        return self

