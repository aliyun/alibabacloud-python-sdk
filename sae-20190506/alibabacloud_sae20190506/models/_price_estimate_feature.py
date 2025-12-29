# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class PriceEstimateFeature(DaraModel):
    def __init__(
        self,
        app_count: int = None,
        app_type: str = None,
        cpu_core: float = None,
        cpu_strategy: str = None,
        cpu_util_level: str = None,
        cpu_util_metrics: List[float] = None,
        enable_cpu_idle: bool = None,
        env_type: str = None,
        ephemeral_storage_gi_b: int = None,
        high_load_instance_count: int = None,
        high_load_qps: float = None,
        high_load_seconds: int = None,
        instance_qps: float = None,
        internet_outbound_gi_b: float = None,
        low_load_instance_count: int = None,
        low_load_qps: float = None,
        low_load_seconds: int = None,
        max_instance_count: int = None,
        memory_gi_b: float = None,
        min_instance_count: int = None,
        new_sae_version: str = None,
        none_load_instance_count: int = None,
        none_load_seconds: int = None,
        region_id: str = None,
        resource_type: str = None,
    ):
        self.app_count = app_count
        # This parameter is required.
        self.app_type = app_type
        # This parameter is required.
        self.cpu_core = cpu_core
        # This parameter is required.
        self.cpu_strategy = cpu_strategy
        self.cpu_util_level = cpu_util_level
        self.cpu_util_metrics = cpu_util_metrics
        self.enable_cpu_idle = enable_cpu_idle
        # This parameter is required.
        self.env_type = env_type
        self.ephemeral_storage_gi_b = ephemeral_storage_gi_b
        self.high_load_instance_count = high_load_instance_count
        self.high_load_qps = high_load_qps
        self.high_load_seconds = high_load_seconds
        self.instance_qps = instance_qps
        self.internet_outbound_gi_b = internet_outbound_gi_b
        self.low_load_instance_count = low_load_instance_count
        self.low_load_qps = low_load_qps
        self.low_load_seconds = low_load_seconds
        self.max_instance_count = max_instance_count
        # This parameter is required.
        self.memory_gi_b = memory_gi_b
        self.min_instance_count = min_instance_count
        self.new_sae_version = new_sae_version
        self.none_load_instance_count = none_load_instance_count
        self.none_load_seconds = none_load_seconds
        # This parameter is required.
        self.region_id = region_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_count is not None:
            result['AppCount'] = self.app_count

        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.cpu_core is not None:
            result['CpuCore'] = self.cpu_core

        if self.cpu_strategy is not None:
            result['CpuStrategy'] = self.cpu_strategy

        if self.cpu_util_level is not None:
            result['CpuUtilLevel'] = self.cpu_util_level

        if self.cpu_util_metrics is not None:
            result['CpuUtilMetrics'] = self.cpu_util_metrics

        if self.enable_cpu_idle is not None:
            result['EnableCpuIdle'] = self.enable_cpu_idle

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.ephemeral_storage_gi_b is not None:
            result['EphemeralStorageGiB'] = self.ephemeral_storage_gi_b

        if self.high_load_instance_count is not None:
            result['HighLoadInstanceCount'] = self.high_load_instance_count

        if self.high_load_qps is not None:
            result['HighLoadQps'] = self.high_load_qps

        if self.high_load_seconds is not None:
            result['HighLoadSeconds'] = self.high_load_seconds

        if self.instance_qps is not None:
            result['InstanceQps'] = self.instance_qps

        if self.internet_outbound_gi_b is not None:
            result['InternetOutboundGiB'] = self.internet_outbound_gi_b

        if self.low_load_instance_count is not None:
            result['LowLoadInstanceCount'] = self.low_load_instance_count

        if self.low_load_qps is not None:
            result['LowLoadQps'] = self.low_load_qps

        if self.low_load_seconds is not None:
            result['LowLoadSeconds'] = self.low_load_seconds

        if self.max_instance_count is not None:
            result['MaxInstanceCount'] = self.max_instance_count

        if self.memory_gi_b is not None:
            result['MemoryGiB'] = self.memory_gi_b

        if self.min_instance_count is not None:
            result['MinInstanceCount'] = self.min_instance_count

        if self.new_sae_version is not None:
            result['NewSaeVersion'] = self.new_sae_version

        if self.none_load_instance_count is not None:
            result['NoneLoadInstanceCount'] = self.none_load_instance_count

        if self.none_load_seconds is not None:
            result['NoneLoadSeconds'] = self.none_load_seconds

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCount') is not None:
            self.app_count = m.get('AppCount')

        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('CpuCore') is not None:
            self.cpu_core = m.get('CpuCore')

        if m.get('CpuStrategy') is not None:
            self.cpu_strategy = m.get('CpuStrategy')

        if m.get('CpuUtilLevel') is not None:
            self.cpu_util_level = m.get('CpuUtilLevel')

        if m.get('CpuUtilMetrics') is not None:
            self.cpu_util_metrics = m.get('CpuUtilMetrics')

        if m.get('EnableCpuIdle') is not None:
            self.enable_cpu_idle = m.get('EnableCpuIdle')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('EphemeralStorageGiB') is not None:
            self.ephemeral_storage_gi_b = m.get('EphemeralStorageGiB')

        if m.get('HighLoadInstanceCount') is not None:
            self.high_load_instance_count = m.get('HighLoadInstanceCount')

        if m.get('HighLoadQps') is not None:
            self.high_load_qps = m.get('HighLoadQps')

        if m.get('HighLoadSeconds') is not None:
            self.high_load_seconds = m.get('HighLoadSeconds')

        if m.get('InstanceQps') is not None:
            self.instance_qps = m.get('InstanceQps')

        if m.get('InternetOutboundGiB') is not None:
            self.internet_outbound_gi_b = m.get('InternetOutboundGiB')

        if m.get('LowLoadInstanceCount') is not None:
            self.low_load_instance_count = m.get('LowLoadInstanceCount')

        if m.get('LowLoadQps') is not None:
            self.low_load_qps = m.get('LowLoadQps')

        if m.get('LowLoadSeconds') is not None:
            self.low_load_seconds = m.get('LowLoadSeconds')

        if m.get('MaxInstanceCount') is not None:
            self.max_instance_count = m.get('MaxInstanceCount')

        if m.get('MemoryGiB') is not None:
            self.memory_gi_b = m.get('MemoryGiB')

        if m.get('MinInstanceCount') is not None:
            self.min_instance_count = m.get('MinInstanceCount')

        if m.get('NewSaeVersion') is not None:
            self.new_sae_version = m.get('NewSaeVersion')

        if m.get('NoneLoadInstanceCount') is not None:
            self.none_load_instance_count = m.get('NoneLoadInstanceCount')

        if m.get('NoneLoadSeconds') is not None:
            self.none_load_seconds = m.get('NoneLoadSeconds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

