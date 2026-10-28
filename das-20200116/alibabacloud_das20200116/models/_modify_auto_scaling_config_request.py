# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class ModifyAutoScalingConfigRequest(DaraModel):
    def __init__(
        self,
        bandwidth: main_models.ModifyAutoScalingConfigRequestBandwidth = None,
        instance_id: str = None,
        resource: main_models.ModifyAutoScalingConfigRequestResource = None,
        shard: main_models.ModifyAutoScalingConfigRequestShard = None,
        spec: main_models.ModifyAutoScalingConfigRequestSpec = None,
        storage: main_models.ModifyAutoScalingConfigRequestStorage = None,
    ):
        # The configuration items for the bandwidth elastic scaling feature.
        self.bandwidth = bandwidth
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The configuration items for the resource elastic scaling feature.
        self.resource = resource
        # The configuration items for the shard elastic scaling feature.
        self.shard = shard
        # The configuration items for the specification elastic scaling feature.
        self.spec = spec
        # The configuration items for the automatic storage expansion feature.
        self.storage = storage

    def validate(self):
        if self.bandwidth:
            self.bandwidth.validate()
        if self.resource:
            self.resource.validate()
        if self.shard:
            self.shard.validate()
        if self.spec:
            self.spec.validate()
        if self.storage:
            self.storage.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth.to_map()

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.resource is not None:
            result['Resource'] = self.resource.to_map()

        if self.shard is not None:
            result['Shard'] = self.shard.to_map()

        if self.spec is not None:
            result['Spec'] = self.spec.to_map()

        if self.storage is not None:
            result['Storage'] = self.storage.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            temp_model = main_models.ModifyAutoScalingConfigRequestBandwidth()
            self.bandwidth = temp_model.from_map(m.get('Bandwidth'))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Resource') is not None:
            temp_model = main_models.ModifyAutoScalingConfigRequestResource()
            self.resource = temp_model.from_map(m.get('Resource'))

        if m.get('Shard') is not None:
            temp_model = main_models.ModifyAutoScalingConfigRequestShard()
            self.shard = temp_model.from_map(m.get('Shard'))

        if m.get('Spec') is not None:
            temp_model = main_models.ModifyAutoScalingConfigRequestSpec()
            self.spec = temp_model.from_map(m.get('Spec'))

        if m.get('Storage') is not None:
            temp_model = main_models.ModifyAutoScalingConfigRequestStorage()
            self.storage = temp_model.from_map(m.get('Storage'))

        return self

class ModifyAutoScalingConfigRequestStorage(DaraModel):
    def __init__(
        self,
        apply: bool = None,
        disk_usage_upper_threshold: int = None,
        max_storage: int = None,
        upgrade: bool = None,
    ):
        # Specifies whether to apply the configurations under the **Storage** configuration item for the automatic storage expansion feature:
        # 
        # - **true**: Yes.
        # - **false**: No.
        self.apply = apply
        # The threshold of average storage space utilization that triggers automatic storage expansion. Unit: %. Valid values:
        # - **50**
        # - **60**
        # - **70**
        # - **80**
        # - **90**
        self.disk_usage_upper_threshold = disk_usage_upper_threshold
        # The upper limit of the storage space. The value must be greater than or equal to the current total storage space of the instance. Valid values:
        # 
        # - ESSD cloud disk upper limit: 32,000 GB.
        # - Standard SSD upper limit: 6,000 GB.
        # 
        # > Standard SSDs are retired. [Upgrade to ESSD cloud disks](https://help.aliyun.com/document_detail/314678.html).
        self.max_storage = max_storage
        # Specifies whether to enable automatic storage expansion:
        # 
        # - **true**: Yes.
        # - **false**: No.
        self.upgrade = upgrade

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply is not None:
            result['Apply'] = self.apply

        if self.disk_usage_upper_threshold is not None:
            result['DiskUsageUpperThreshold'] = self.disk_usage_upper_threshold

        if self.max_storage is not None:
            result['MaxStorage'] = self.max_storage

        if self.upgrade is not None:
            result['Upgrade'] = self.upgrade

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Apply') is not None:
            self.apply = m.get('Apply')

        if m.get('DiskUsageUpperThreshold') is not None:
            self.disk_usage_upper_threshold = m.get('DiskUsageUpperThreshold')

        if m.get('MaxStorage') is not None:
            self.max_storage = m.get('MaxStorage')

        if m.get('Upgrade') is not None:
            self.upgrade = m.get('Upgrade')

        return self

class ModifyAutoScalingConfigRequestSpec(DaraModel):
    def __init__(
        self,
        apply: bool = None,
        cool_down_time: str = None,
        cpu_usage_upper_threshold: int = None,
        downgrade: bool = None,
        max_read_only_nodes: int = None,
        max_spec: str = None,
        mem_usage_upper_threshold: int = None,
        observation_window_size: str = None,
        upgrade: bool = None,
    ):
        # Specifies whether to apply the configurations under the **Spec** configuration item for the specification elastic scaling feature:
        # 
        # - **true**: Yes.
        # - **false**: No.
        self.apply = apply
        # The cool-down period. The parameter value consists of a number and a time unit suffix. The supported database instances and valid values are as follows. The time suffix **m** indicates minutes, **h** indicates hours, and **d** indicates days:
        # 
        # - PolarDB for MySQL Cluster Edition: **5m**, **10m**, **30m**, **1h**, **2h**, **3h**, **1d**, and **7d**.
        # - ApsaraDB RDS for MySQL high availability series cloud disk edition: **5m**, **10m**, **30m**, **1h**, **2h**, **3h**, **1d**, and **7d**.
        self.cool_down_time = cool_down_time
        # The threshold of average CPU utilization that triggers automatic specification scale-up. Unit: %. Valid values:
        # 
        # - **50**
        # - **60**
        # - **70**
        # - **80**
        # - **90**
        # 
        # >Notice: You must set this parameter when the target database instance is PolarDB for MySQL Cluster Edition or ApsaraDB RDS for MySQL high availability series cloud disk edition.
        self.cpu_usage_upper_threshold = cpu_usage_upper_threshold
        # Specifies whether automatic specification scale-down is enabled:
        # - **true**: Yes.
        # - **false**: No.
        # 
        # >Notice: You must set this parameter when the target database instance is PolarDB for MySQL Cluster Edition or ApsaraDB RDS for MySQL high availability series cloud disk edition.
        self.downgrade = downgrade
        # The maximum number of read-only nodes for the instance.
        # 
        # >Notice: You must set this parameter when the target database instance is PolarDB for MySQL Cluster Edition.
        self.max_read_only_nodes = max_read_only_nodes
        # The upper limit of the specification for automatic scale-up. You can only scale up to a higher specification within the same series of the database instance. For more details, see the specification documentation for each database instance:
        # <props="china">
        # 
        # - For PolarDB for MySQL Cluster Edition, see [Compute node specifications](https://help.aliyun.com/document_detail/102542.html).
        # - For ApsaraDB RDS for MySQL high availability series cloud disk edition, see [Product specifications](https://help.aliyun.com/document_detail/276974.html).
        # - For Tair (Redis® OSS-Compatible) cloud-native (formerly cloud disk) open-source edition, see [Instance specifications](https://help.aliyun.com/document_detail/144986.html).
        # 
        # 
        # 
        # <props="intl">
        # 
        # - For PolarDB for MySQL Cluster Edition, see [Compute node specifications](https://help.aliyun.com/document_detail/102542.html).
        # - For ApsaraDB RDS for MySQL high availability series cloud disk edition, see [Product specifications](https://help.aliyun.com/document_detail/276974.html).
        self.max_spec = max_spec
        # The threshold of average memory utilization that triggers automatic specification scale-up. Unit: %. Valid values:
        # - **50**
        # - **60**
        # - **70**
        # - **80**
        # - **90**
        # 
        # >Notice: You must set this parameter when the target database instance is Tair (Redis® OSS-Compatible) cloud-native (formerly cloud disk) open-source edition on the China site.
        self.mem_usage_upper_threshold = mem_usage_upper_threshold
        # The observation window. The parameter value consists of a number and a time unit suffix. The supported database instances and valid values are as follows. The time suffix **m** indicates minutes, and **h** indicates hours:
        # 
        # - PolarDB for MySQL Cluster Edition: **5m**, **10m**, **15m**, and **30m**.
        # - ApsaraDB RDS for MySQL high availability series cloud disk edition: **5m**, **20m**, **30m**, **40m**, and **1h**.
        # - Tair (Redis® OSS-Compatible) cloud-native (formerly cloud disk) open-source edition: **5m**, **10m**, **15m**, and **30m**.
        self.observation_window_size = observation_window_size
        # Specifies whether to enable automatic specification scale-up:
        # 
        # - **true**: Yes.
        # - **false**: No.
        self.upgrade = upgrade

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply is not None:
            result['Apply'] = self.apply

        if self.cool_down_time is not None:
            result['CoolDownTime'] = self.cool_down_time

        if self.cpu_usage_upper_threshold is not None:
            result['CpuUsageUpperThreshold'] = self.cpu_usage_upper_threshold

        if self.downgrade is not None:
            result['Downgrade'] = self.downgrade

        if self.max_read_only_nodes is not None:
            result['MaxReadOnlyNodes'] = self.max_read_only_nodes

        if self.max_spec is not None:
            result['MaxSpec'] = self.max_spec

        if self.mem_usage_upper_threshold is not None:
            result['MemUsageUpperThreshold'] = self.mem_usage_upper_threshold

        if self.observation_window_size is not None:
            result['ObservationWindowSize'] = self.observation_window_size

        if self.upgrade is not None:
            result['Upgrade'] = self.upgrade

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Apply') is not None:
            self.apply = m.get('Apply')

        if m.get('CoolDownTime') is not None:
            self.cool_down_time = m.get('CoolDownTime')

        if m.get('CpuUsageUpperThreshold') is not None:
            self.cpu_usage_upper_threshold = m.get('CpuUsageUpperThreshold')

        if m.get('Downgrade') is not None:
            self.downgrade = m.get('Downgrade')

        if m.get('MaxReadOnlyNodes') is not None:
            self.max_read_only_nodes = m.get('MaxReadOnlyNodes')

        if m.get('MaxSpec') is not None:
            self.max_spec = m.get('MaxSpec')

        if m.get('MemUsageUpperThreshold') is not None:
            self.mem_usage_upper_threshold = m.get('MemUsageUpperThreshold')

        if m.get('ObservationWindowSize') is not None:
            self.observation_window_size = m.get('ObservationWindowSize')

        if m.get('Upgrade') is not None:
            self.upgrade = m.get('Upgrade')

        return self

class ModifyAutoScalingConfigRequestShard(DaraModel):
    def __init__(
        self,
        apply: bool = None,
        downgrade: bool = None,
        downgrade_observation_window_size: str = None,
        max_shards: int = None,
        mem_usage_lower_threshold: int = None,
        mem_usage_upper_threshold: int = None,
        min_shards: int = None,
        upgrade: bool = None,
        upgrade_observation_window_size: str = None,
    ):
        # Specifies whether to apply the configurations under the **Shard** configuration item for the shard elastic scaling feature:
        # 
        # - **true**: Yes.
        # - **false**: No.
        # 
        # >Notice: The shard elastic scaling feature is supported only when the target database instance is Tair (Redis® OSS-Compatible) cloud-native (formerly cloud disk) edition in cluster architecture on the China site.
        self.apply = apply
        # Specifies whether to enable automatic shard reduction:
        # 
        # - **true**: Yes.
        # - **false**: No.
        # 
        # > The automatic shard reduction feature is currently in canary release.
        self.downgrade = downgrade
        # The observation window for automatic shard reduction. The parameter value consists of a number and a time unit suffix. The time suffix **h** indicates hours, and **d** indicates days. Valid values:
        # 
        # - **1h**
        # - **2h**
        # - **3h**
        # - **1d**
        # - **7d**
        self.downgrade_observation_window_size = downgrade_observation_window_size
        # The maximum total number of shards for the instance. The value must be a positive integer. Valid values: 4 to 32.
        self.max_shards = max_shards
        # The threshold of average memory utilization that triggers automatic shard reduction. Unit: %. Valid values:
        # 
        # - **10**
        # - **20**
        # - **30**
        self.mem_usage_lower_threshold = mem_usage_lower_threshold
        # The threshold of average memory utilization that triggers automatic shard addition. Unit: %. Valid values:
        # 
        # - **50**
        # - **60**
        # - **70**
        # - **80**
        # - **90**
        self.mem_usage_upper_threshold = mem_usage_upper_threshold
        # The minimum total number of shards for the instance. The value must be a positive integer. Valid values: 4 to 32.
        self.min_shards = min_shards
        # Specifies whether to enable automatic shard addition:
        # 
        # - **true**: Yes.
        # - **false**: No.
        self.upgrade = upgrade
        # The observation window for automatic shard addition. The parameter value consists of a number and a time unit suffix. The time suffix **m** indicates minutes. Valid values:
        # 
        # - **5m**
        # - **10m**
        # - **15m**
        # - **30m**
        self.upgrade_observation_window_size = upgrade_observation_window_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply is not None:
            result['Apply'] = self.apply

        if self.downgrade is not None:
            result['Downgrade'] = self.downgrade

        if self.downgrade_observation_window_size is not None:
            result['DowngradeObservationWindowSize'] = self.downgrade_observation_window_size

        if self.max_shards is not None:
            result['MaxShards'] = self.max_shards

        if self.mem_usage_lower_threshold is not None:
            result['MemUsageLowerThreshold'] = self.mem_usage_lower_threshold

        if self.mem_usage_upper_threshold is not None:
            result['MemUsageUpperThreshold'] = self.mem_usage_upper_threshold

        if self.min_shards is not None:
            result['MinShards'] = self.min_shards

        if self.upgrade is not None:
            result['Upgrade'] = self.upgrade

        if self.upgrade_observation_window_size is not None:
            result['UpgradeObservationWindowSize'] = self.upgrade_observation_window_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Apply') is not None:
            self.apply = m.get('Apply')

        if m.get('Downgrade') is not None:
            self.downgrade = m.get('Downgrade')

        if m.get('DowngradeObservationWindowSize') is not None:
            self.downgrade_observation_window_size = m.get('DowngradeObservationWindowSize')

        if m.get('MaxShards') is not None:
            self.max_shards = m.get('MaxShards')

        if m.get('MemUsageLowerThreshold') is not None:
            self.mem_usage_lower_threshold = m.get('MemUsageLowerThreshold')

        if m.get('MemUsageUpperThreshold') is not None:
            self.mem_usage_upper_threshold = m.get('MemUsageUpperThreshold')

        if m.get('MinShards') is not None:
            self.min_shards = m.get('MinShards')

        if m.get('Upgrade') is not None:
            self.upgrade = m.get('Upgrade')

        if m.get('UpgradeObservationWindowSize') is not None:
            self.upgrade_observation_window_size = m.get('UpgradeObservationWindowSize')

        return self

class ModifyAutoScalingConfigRequestResource(DaraModel):
    def __init__(
        self,
        apply: bool = None,
        cpu_usage_upper_threshold: int = None,
        downgrade_observation_window_size: str = None,
        enable: bool = None,
        upgrade_observation_window_size: str = None,
    ):
        # Specifies whether to apply the configurations under the **Resource** configuration item for the resource elastic scaling feature:
        # 
        # - **true**: Yes.
        # - **false**: No.
        self.apply = apply
        # The threshold of average CPU utilization that triggers automatic resource scale-up. Unit: %. Valid values:
        # 
        # - **70**
        # - **80**
        # - **90**
        self.cpu_usage_upper_threshold = cpu_usage_upper_threshold
        # The observation window for scale-down. The parameter value consists of a number and a time unit suffix. The time suffix **m** indicates minutes. Valid values:
        # 
        # - **1m**
        # - **3m**
        # - **5m**
        # - **10m**
        # - **20m**
        # - **30m**
        self.downgrade_observation_window_size = downgrade_observation_window_size
        # Specifies whether to enable resource elastic scaling:
        # 
        # - **true**: Yes.
        # - **false**: No.
        self.enable = enable
        # The observation window for scale-up. The parameter value consists of a number and a time unit suffix. The time suffix **m** indicates minutes. Valid values:
        # 
        # - **1m**
        # - **3m**
        # - **5m**
        # - **10m**
        # - **20m**
        # - **30m**
        self.upgrade_observation_window_size = upgrade_observation_window_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply is not None:
            result['Apply'] = self.apply

        if self.cpu_usage_upper_threshold is not None:
            result['CpuUsageUpperThreshold'] = self.cpu_usage_upper_threshold

        if self.downgrade_observation_window_size is not None:
            result['DowngradeObservationWindowSize'] = self.downgrade_observation_window_size

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.upgrade_observation_window_size is not None:
            result['UpgradeObservationWindowSize'] = self.upgrade_observation_window_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Apply') is not None:
            self.apply = m.get('Apply')

        if m.get('CpuUsageUpperThreshold') is not None:
            self.cpu_usage_upper_threshold = m.get('CpuUsageUpperThreshold')

        if m.get('DowngradeObservationWindowSize') is not None:
            self.downgrade_observation_window_size = m.get('DowngradeObservationWindowSize')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('UpgradeObservationWindowSize') is not None:
            self.upgrade_observation_window_size = m.get('UpgradeObservationWindowSize')

        return self

class ModifyAutoScalingConfigRequestBandwidth(DaraModel):
    def __init__(
        self,
        apply: bool = None,
        bandwidth_usage_lower_threshold: int = None,
        bandwidth_usage_upper_threshold: int = None,
        downgrade: bool = None,
        observation_window_size: str = None,
        upgrade: bool = None,
    ):
        # Specifies whether to apply the configurations under the **Bandwidth** configuration item for the bandwidth elastic scaling feature:
        # 
        # - **true**: Yes.
        # - **false**: No.
        self.apply = apply
        # The threshold of average bandwidth usage that triggers automatic bandwidth downgrade. Unit: %. Valid values:
        # 
        # - **10**
        # - **20**
        # - **30**
        self.bandwidth_usage_lower_threshold = bandwidth_usage_lower_threshold
        # The threshold of average bandwidth usage that triggers automatic bandwidth upgrade. Unit: %. Valid values:
        # 
        # - **50**
        # - **60**
        # - **70**
        # - **80**
        # - **90**
        # - **95**
        self.bandwidth_usage_upper_threshold = bandwidth_usage_upper_threshold
        # Specifies whether to enable automatic bandwidth downgrade:
        # 
        # - **true**: Yes.
        # - **false**: No.
        self.downgrade = downgrade
        # The observation window for automatic bandwidth upgrade. The parameter value consists of a number and a time unit suffix. The time suffix **m** indicates minutes. Valid values:
        # 
        # - **1m**
        # - **5m**
        # - **10m**
        # - **15m**
        # - **30m**
        self.observation_window_size = observation_window_size
        # Specifies whether to enable automatic bandwidth upgrade:
        # 
        # - **true**: Yes.
        # - **false**: No.
        self.upgrade = upgrade

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply is not None:
            result['Apply'] = self.apply

        if self.bandwidth_usage_lower_threshold is not None:
            result['BandwidthUsageLowerThreshold'] = self.bandwidth_usage_lower_threshold

        if self.bandwidth_usage_upper_threshold is not None:
            result['BandwidthUsageUpperThreshold'] = self.bandwidth_usage_upper_threshold

        if self.downgrade is not None:
            result['Downgrade'] = self.downgrade

        if self.observation_window_size is not None:
            result['ObservationWindowSize'] = self.observation_window_size

        if self.upgrade is not None:
            result['Upgrade'] = self.upgrade

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Apply') is not None:
            self.apply = m.get('Apply')

        if m.get('BandwidthUsageLowerThreshold') is not None:
            self.bandwidth_usage_lower_threshold = m.get('BandwidthUsageLowerThreshold')

        if m.get('BandwidthUsageUpperThreshold') is not None:
            self.bandwidth_usage_upper_threshold = m.get('BandwidthUsageUpperThreshold')

        if m.get('Downgrade') is not None:
            self.downgrade = m.get('Downgrade')

        if m.get('ObservationWindowSize') is not None:
            self.observation_window_size = m.get('ObservationWindowSize')

        if m.get('Upgrade') is not None:
            self.upgrade = m.get('Upgrade')

        return self

