# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class DescribeAutoScalingConfigResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeAutoScalingConfigResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The HTTP status code returned.
        self.code = code
        # The configurations of the auto scaling feature for instances.
        self.data = data
        # The returned message.
        # 
        # >  If the request was successful, **Successful** is returned. If the request failed, an error message such as an error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeAutoScalingConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeAutoScalingConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        bandwidth: main_models.DescribeAutoScalingConfigResponseBodyDataBandwidth = None,
        resource: main_models.DescribeAutoScalingConfigResponseBodyDataResource = None,
        shard: main_models.DescribeAutoScalingConfigResponseBodyDataShard = None,
        spec: main_models.DescribeAutoScalingConfigResponseBodyDataSpec = None,
        storage: main_models.DescribeAutoScalingConfigResponseBodyDataStorage = None,
    ):
        # The configurations of the automatic bandwidth adjustment feature.
        self.bandwidth = bandwidth
        # The configurations of the auto scaling feature for local resources.
        self.resource = resource
        # The configurations of the auto scaling feature for shards.
        self.shard = shard
        # The configurations of the auto scaling feature for specifications.
        self.spec = spec
        # The configurations of the automatic storage expansion feature.
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
            temp_model = main_models.DescribeAutoScalingConfigResponseBodyDataBandwidth()
            self.bandwidth = temp_model.from_map(m.get('Bandwidth'))

        if m.get('Resource') is not None:
            temp_model = main_models.DescribeAutoScalingConfigResponseBodyDataResource()
            self.resource = temp_model.from_map(m.get('Resource'))

        if m.get('Shard') is not None:
            temp_model = main_models.DescribeAutoScalingConfigResponseBodyDataShard()
            self.shard = temp_model.from_map(m.get('Shard'))

        if m.get('Spec') is not None:
            temp_model = main_models.DescribeAutoScalingConfigResponseBodyDataSpec()
            self.spec = temp_model.from_map(m.get('Spec'))

        if m.get('Storage') is not None:
            temp_model = main_models.DescribeAutoScalingConfigResponseBodyDataStorage()
            self.storage = temp_model.from_map(m.get('Storage'))

        return self

class DescribeAutoScalingConfigResponseBodyDataStorage(DaraModel):
    def __init__(
        self,
        disk_usage_upper_threshold: int = None,
        max_storage: int = None,
        upgrade: bool = None,
    ):
        # The average storage usage threshold that triggers automatic storage expansion. Unit: %.
        self.disk_usage_upper_threshold = disk_usage_upper_threshold
        # The maximum storage size. Unit: GB.
        self.max_storage = max_storage
        # Indicates whether the automatic storage expansion feature is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.upgrade = upgrade

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disk_usage_upper_threshold is not None:
            result['DiskUsageUpperThreshold'] = self.disk_usage_upper_threshold

        if self.max_storage is not None:
            result['MaxStorage'] = self.max_storage

        if self.upgrade is not None:
            result['Upgrade'] = self.upgrade

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskUsageUpperThreshold') is not None:
            self.disk_usage_upper_threshold = m.get('DiskUsageUpperThreshold')

        if m.get('MaxStorage') is not None:
            self.max_storage = m.get('MaxStorage')

        if m.get('Upgrade') is not None:
            self.upgrade = m.get('Upgrade')

        return self

class DescribeAutoScalingConfigResponseBodyDataSpec(DaraModel):
    def __init__(
        self,
        cool_down_time: str = None,
        cpu_usage_upper_threshold: int = None,
        downgrade: bool = None,
        max_read_only_nodes: int = None,
        max_spec: str = None,
        mem_usage_upper_threshold: int = None,
        observation_window_size: str = None,
        upgrade: bool = None,
    ):
        # The quiescent period. The return value consists of a numeric value and a time unit suffix. Valid values of the time unit suffix:
        # 
        # *   **s**: seconds.
        # *   **m**: minutes.
        # *   **h**: hours.
        # *   **d**: days.
        # 
        # >  A value of **5m** indicates 5 minutes.
        self.cool_down_time = cool_down_time
        # The average CPU utilization threshold that triggers automatic specification scale-up. Unit: %.
        self.cpu_usage_upper_threshold = cpu_usage_upper_threshold
        # Indicates whether the automatic specification scale-down feature is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.downgrade = downgrade
        # The maximum number of read-only nodes of the instance.
        self.max_read_only_nodes = max_read_only_nodes
        # The maximum specifications to which the cluster can be scaled up. For more information about the specifications of each type of supported database instances, see the following topics:
        # 
        # *   PolarDB for MySQL Cluster Edition instances: [Compute node specifications of PolarDB for MySQL Enterprise Edition](https://help.aliyun.com/document_detail/102542.html)
        # *   ApsaraDB RDS for MySQL High-availability Edition instances that use standard SSDs or ESSDs: [Specifications](https://help.aliyun.com/document_detail/276974.html)
        self.max_spec = max_spec
        # The average memory usage threshold that triggers automatic specification scale-up. Unit: %.
        self.mem_usage_upper_threshold = mem_usage_upper_threshold
        # The observation window. The return value consists of a numeric value and a time unit suffix. Valid values of the time unit suffix:
        # 
        # *   **s**: seconds.
        # *   **m**: minutes.
        # *   **h**: hours.
        # *   **d**: days.
        # 
        # >  A value of **5m** indicates 5 minutes.
        self.observation_window_size = observation_window_size
        # Indicates whether the automatic specification scale-up feature is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.upgrade = upgrade

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class DescribeAutoScalingConfigResponseBodyDataShard(DaraModel):
    def __init__(
        self,
        downgrade: bool = None,
        downgrade_observation_window_size: str = None,
        max_shards: int = None,
        mem_usage_lower_threshold: int = None,
        mem_usage_upper_threshold: int = None,
        min_shards: int = None,
        upgrade: bool = None,
        upgrade_observation_window_size: str = None,
    ):
        # Indicates whether the feature of automatically removing shards is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.downgrade = downgrade
        # The observation window of the feature of automatically removing shards. The return value consists of a numeric value and a time unit suffix. Valid values of the time unit suffix:
        # 
        # *   **s**: seconds.
        # *   **m**: minutes.
        # *   **h**: hours.
        # *   **d**: days.
        # 
        # >  A value of **1d** indicates one day.
        self.downgrade_observation_window_size = downgrade_observation_window_size
        # The maximum number of shards in the instance.
        self.max_shards = max_shards
        # The average memory usage threshold that triggers automatic removal of shards. Unit: %.
        self.mem_usage_lower_threshold = mem_usage_lower_threshold
        # The average memory usage threshold that triggers automatic adding of shards. Unit: %.
        self.mem_usage_upper_threshold = mem_usage_upper_threshold
        # The minimum number of shards in the instance.
        self.min_shards = min_shards
        # Indicates whether the feature of automatically adding shards is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.upgrade = upgrade
        # The observation window of the feature of automatically adding shards. The return value consists of a numeric value and a time unit suffix. Valid values of the time unit suffix:
        # 
        # *   **s**: seconds.
        # *   **m**: minutes.
        # *   **h**: hours.
        # *   **d**: days.
        # 
        # >  A value of **5m** indicates 5 minutes.
        self.upgrade_observation_window_size = upgrade_observation_window_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class DescribeAutoScalingConfigResponseBodyDataResource(DaraModel):
    def __init__(
        self,
        cpu_step: int = None,
        cpu_usage_upper_threshold: int = None,
        downgrade_observation_window_size: str = None,
        enable: bool = None,
        upgrade_observation_window_size: str = None,
    ):
        # The scale-out step size of CPU.
        self.cpu_step = cpu_step
        # The average CPU utilization threshold that triggers automatic scale-out of local resources. Unit: %.
        self.cpu_usage_upper_threshold = cpu_usage_upper_threshold
        # The observation window of the automatic scale-in feature for local resources. The return value consists of a numeric value and a time unit suffix. Valid values of the time unit suffix:
        # 
        # *   **s**: seconds.
        # *   **m**: minutes.
        # *   **h**: hours.
        # *   **d**: days.
        # 
        # >  A value of **5m** indicates 5 minutes.
        self.downgrade_observation_window_size = downgrade_observation_window_size
        # Indicates whether the auto scaling feature is enabled for local resources. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.enable = enable
        # The observation window of the automatic scale-out feature for local resources. The return value consists of a numeric value and a time unit suffix. Valid values of the time unit suffix:
        # 
        # *   **s**: seconds.
        # *   **m**: minutes.
        # *   **h**: hours.
        # *   **d**: days.
        # 
        # >  A value of **5m** indicates 5 minutes.
        self.upgrade_observation_window_size = upgrade_observation_window_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu_step is not None:
            result['CpuStep'] = self.cpu_step

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
        if m.get('CpuStep') is not None:
            self.cpu_step = m.get('CpuStep')

        if m.get('CpuUsageUpperThreshold') is not None:
            self.cpu_usage_upper_threshold = m.get('CpuUsageUpperThreshold')

        if m.get('DowngradeObservationWindowSize') is not None:
            self.downgrade_observation_window_size = m.get('DowngradeObservationWindowSize')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('UpgradeObservationWindowSize') is not None:
            self.upgrade_observation_window_size = m.get('UpgradeObservationWindowSize')

        return self

class DescribeAutoScalingConfigResponseBodyDataBandwidth(DaraModel):
    def __init__(
        self,
        bandwidth_usage_lower_threshold: int = None,
        bandwidth_usage_upper_threshold: int = None,
        downgrade: bool = None,
        observation_window_size: str = None,
        upgrade: bool = None,
    ):
        # The average bandwidth usage threshold that triggers automatic bandwidth downgrade. Unit: %.
        self.bandwidth_usage_lower_threshold = bandwidth_usage_lower_threshold
        # The average bandwidth usage threshold that triggers automatic bandwidth adjustment. Unit: %.
        self.bandwidth_usage_upper_threshold = bandwidth_usage_upper_threshold
        # Indicates whether the automatic bandwidth downgrade feature is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.downgrade = downgrade
        # The observation window of the automatic bandwidth adjustment feature. The return value consists of a numeric value and a time unit suffix. Valid values of the time unit suffix:
        # 
        # *   **s**: seconds.
        # *   **m**: minutes.
        # *   **h**: hours.
        # *   **d**: days.
        # 
        # >  A value of **5m** indicates 5 minutes.
        self.observation_window_size = observation_window_size
        # Indicates whether the automatic bandwidth adjustment feature is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.upgrade = upgrade

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

