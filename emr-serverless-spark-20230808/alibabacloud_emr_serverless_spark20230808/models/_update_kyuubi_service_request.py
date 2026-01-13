# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateKyuubiServiceRequest(DaraModel):
    def __init__(
        self,
        compute_instance: str = None,
        kyuubi_configs: str = None,
        kyuubi_release_version: str = None,
        name: str = None,
        public_endpoint_enabled: bool = None,
        queue: str = None,
        release_version: str = None,
        replica: int = None,
        restart: bool = None,
        spark_configs: str = None,
    ):
        self.compute_instance = compute_instance
        self.kyuubi_configs = kyuubi_configs
        self.kyuubi_release_version = kyuubi_release_version
        self.name = name
        self.public_endpoint_enabled = public_endpoint_enabled
        self.queue = queue
        self.release_version = release_version
        self.replica = replica
        self.restart = restart
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

        if self.release_version is not None:
            result['releaseVersion'] = self.release_version

        if self.replica is not None:
            result['replica'] = self.replica

        if self.restart is not None:
            result['restart'] = self.restart

        if self.spark_configs is not None:
            result['sparkConfigs'] = self.spark_configs

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('computeInstance') is not None:
            self.compute_instance = m.get('computeInstance')

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

        if m.get('releaseVersion') is not None:
            self.release_version = m.get('releaseVersion')

        if m.get('replica') is not None:
            self.replica = m.get('replica')

        if m.get('restart') is not None:
            self.restart = m.get('restart')

        if m.get('sparkConfigs') is not None:
            self.spark_configs = m.get('sparkConfigs')

        return self

