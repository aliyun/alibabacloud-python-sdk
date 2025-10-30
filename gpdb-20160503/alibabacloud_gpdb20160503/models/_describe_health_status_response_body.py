# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class DescribeHealthStatusResponseBody(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        request_id: str = None,
        status: main_models.DescribeHealthStatusResponseBodyStatus = None,
    ):
        # The ID of instance.
        self.dbcluster_id = dbcluster_id
        # The ID of the request.
        self.request_id = request_id
        # The queried performance metrics. Each performance metric consists of the parameter name, status, and metric value. The metric information is returned only for the performance parameters specified by **Key**. For example, if you set **Key** to **adbpg_status**, only the metric information of **adbpg_status** is returned.
        # 
        # For more information about performance parameters, see [Performance parameters](https://help.aliyun.com/document_detail/86943.html).
        self.status = status

    def validate(self):
        if self.status:
            self.status.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            temp_model = main_models.DescribeHealthStatusResponseBodyStatus()
            self.status = temp_model.from_map(m.get('Status'))

        return self

class DescribeHealthStatusResponseBodyStatus(DaraModel):
    def __init__(
        self,
        adbgp_segment_disk_usage_percent_max: main_models.DescribeHealthStatusResponseBodyStatusAdbgpSegmentDiskUsagePercentMax = None,
        adbpg_connection_status: main_models.DescribeHealthStatusResponseBodyStatusAdbpgConnectionStatus = None,
        adbpg_disk_status: main_models.DescribeHealthStatusResponseBodyStatusAdbpgDiskStatus = None,
        adbpg_disk_usage_percent: main_models.DescribeHealthStatusResponseBodyStatusAdbpgDiskUsagePercent = None,
        adbpg_instance_cold_data_gb: main_models.DescribeHealthStatusResponseBodyStatusAdbpgInstanceColdDataGb = None,
        adbpg_instance_hot_data_gb: main_models.DescribeHealthStatusResponseBodyStatusAdbpgInstanceHotDataGb = None,
        adbpg_instance_total_data_gb: main_models.DescribeHealthStatusResponseBodyStatusAdbpgInstanceTotalDataGb = None,
        adbpg_master_disk_usage_percent_max: main_models.DescribeHealthStatusResponseBodyStatusAdbpgMasterDiskUsagePercentMax = None,
        adbpg_master_status: main_models.DescribeHealthStatusResponseBodyStatusAdbpgMasterStatus = None,
        adbpg_segment_status: main_models.DescribeHealthStatusResponseBodyStatusAdbpgSegmentStatus = None,
        adbpg_status: main_models.DescribeHealthStatusResponseBodyStatusAdbpgStatus = None,
        node_master_connection_status: main_models.DescribeHealthStatusResponseBodyStatusNodeMasterConnectionStatus = None,
        node_master_status: main_models.DescribeHealthStatusResponseBodyStatusNodeMasterStatus = None,
        node_segment_connection_status: main_models.DescribeHealthStatusResponseBodyStatusNodeSegmentConnectionStatus = None,
        node_segment_disk_status: main_models.DescribeHealthStatusResponseBodyStatusNodeSegmentDiskStatus = None,
    ):
        # The information of maximum compute node storage usage.
        # 
        # >  This parameter value is returned only for instances in elastic storage mode.
        self.adbgp_segment_disk_usage_percent_max = adbgp_segment_disk_usage_percent_max
        # The information of instance connection health status.
        self.adbpg_connection_status = adbpg_connection_status
        # The information of instance storage status.
        # 
        # >  This parameter value is returned only for instances in elastic storage mode.
        self.adbpg_disk_status = adbpg_disk_status
        # The information of instance storage usage.
        # 
        # >  This parameter value is returned only for instances in elastic storage mode.
        self.adbpg_disk_usage_percent = adbpg_disk_usage_percent
        # The total amount of cold data storage.
        self.adbpg_instance_cold_data_gb = adbpg_instance_cold_data_gb
        # The total amount of hot data storage.
        self.adbpg_instance_hot_data_gb = adbpg_instance_hot_data_gb
        # The total amount of data storage of the instance.
        self.adbpg_instance_total_data_gb = adbpg_instance_total_data_gb
        # The information of maximum coordinator node storage usage.
        # 
        # >  This parameter value is returned only for instances in elastic storage mode.
        self.adbpg_master_disk_usage_percent_max = adbpg_master_disk_usage_percent_max
        # The information of coordinator node availability status.
        self.adbpg_master_status = adbpg_master_status
        # The information of compute node availability status.
        self.adbpg_segment_status = adbpg_segment_status
        # The information of instance health status.
        self.adbpg_status = adbpg_status
        # The information of coordinator node connection health status.
        self.node_master_connection_status = node_master_connection_status
        # The information of coordinator node health status.
        self.node_master_status = node_master_status
        # The information of compute node connection health status.
        self.node_segment_connection_status = node_segment_connection_status
        # The information of compute node storage status.
        # 
        # >  This parameter value is returned only for instances in elastic storage mode.
        self.node_segment_disk_status = node_segment_disk_status

    def validate(self):
        if self.adbgp_segment_disk_usage_percent_max:
            self.adbgp_segment_disk_usage_percent_max.validate()
        if self.adbpg_connection_status:
            self.adbpg_connection_status.validate()
        if self.adbpg_disk_status:
            self.adbpg_disk_status.validate()
        if self.adbpg_disk_usage_percent:
            self.adbpg_disk_usage_percent.validate()
        if self.adbpg_instance_cold_data_gb:
            self.adbpg_instance_cold_data_gb.validate()
        if self.adbpg_instance_hot_data_gb:
            self.adbpg_instance_hot_data_gb.validate()
        if self.adbpg_instance_total_data_gb:
            self.adbpg_instance_total_data_gb.validate()
        if self.adbpg_master_disk_usage_percent_max:
            self.adbpg_master_disk_usage_percent_max.validate()
        if self.adbpg_master_status:
            self.adbpg_master_status.validate()
        if self.adbpg_segment_status:
            self.adbpg_segment_status.validate()
        if self.adbpg_status:
            self.adbpg_status.validate()
        if self.node_master_connection_status:
            self.node_master_connection_status.validate()
        if self.node_master_status:
            self.node_master_status.validate()
        if self.node_segment_connection_status:
            self.node_segment_connection_status.validate()
        if self.node_segment_disk_status:
            self.node_segment_disk_status.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adbgp_segment_disk_usage_percent_max is not None:
            result['adbgp_segment_disk_usage_percent_max'] = self.adbgp_segment_disk_usage_percent_max.to_map()

        if self.adbpg_connection_status is not None:
            result['adbpg_connection_status'] = self.adbpg_connection_status.to_map()

        if self.adbpg_disk_status is not None:
            result['adbpg_disk_status'] = self.adbpg_disk_status.to_map()

        if self.adbpg_disk_usage_percent is not None:
            result['adbpg_disk_usage_percent'] = self.adbpg_disk_usage_percent.to_map()

        if self.adbpg_instance_cold_data_gb is not None:
            result['adbpg_instance_cold_data_gb'] = self.adbpg_instance_cold_data_gb.to_map()

        if self.adbpg_instance_hot_data_gb is not None:
            result['adbpg_instance_hot_data_gb'] = self.adbpg_instance_hot_data_gb.to_map()

        if self.adbpg_instance_total_data_gb is not None:
            result['adbpg_instance_total_data_gb'] = self.adbpg_instance_total_data_gb.to_map()

        if self.adbpg_master_disk_usage_percent_max is not None:
            result['adbpg_master_disk_usage_percent_max'] = self.adbpg_master_disk_usage_percent_max.to_map()

        if self.adbpg_master_status is not None:
            result['adbpg_master_status'] = self.adbpg_master_status.to_map()

        if self.adbpg_segment_status is not None:
            result['adbpg_segment_status'] = self.adbpg_segment_status.to_map()

        if self.adbpg_status is not None:
            result['adbpg_status'] = self.adbpg_status.to_map()

        if self.node_master_connection_status is not None:
            result['node_master_connection_status'] = self.node_master_connection_status.to_map()

        if self.node_master_status is not None:
            result['node_master_status'] = self.node_master_status.to_map()

        if self.node_segment_connection_status is not None:
            result['node_segment_connection_status'] = self.node_segment_connection_status.to_map()

        if self.node_segment_disk_status is not None:
            result['node_segment_disk_status'] = self.node_segment_disk_status.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('adbgp_segment_disk_usage_percent_max') is not None:
            temp_model = main_models.DescribeHealthStatusResponseBodyStatusAdbgpSegmentDiskUsagePercentMax()
            self.adbgp_segment_disk_usage_percent_max = temp_model.from_map(m.get('adbgp_segment_disk_usage_percent_max'))

        if m.get('adbpg_connection_status') is not None:
            temp_model = main_models.DescribeHealthStatusResponseBodyStatusAdbpgConnectionStatus()
            self.adbpg_connection_status = temp_model.from_map(m.get('adbpg_connection_status'))

        if m.get('adbpg_disk_status') is not None:
            temp_model = main_models.DescribeHealthStatusResponseBodyStatusAdbpgDiskStatus()
            self.adbpg_disk_status = temp_model.from_map(m.get('adbpg_disk_status'))

        if m.get('adbpg_disk_usage_percent') is not None:
            temp_model = main_models.DescribeHealthStatusResponseBodyStatusAdbpgDiskUsagePercent()
            self.adbpg_disk_usage_percent = temp_model.from_map(m.get('adbpg_disk_usage_percent'))

        if m.get('adbpg_instance_cold_data_gb') is not None:
            temp_model = main_models.DescribeHealthStatusResponseBodyStatusAdbpgInstanceColdDataGb()
            self.adbpg_instance_cold_data_gb = temp_model.from_map(m.get('adbpg_instance_cold_data_gb'))

        if m.get('adbpg_instance_hot_data_gb') is not None:
            temp_model = main_models.DescribeHealthStatusResponseBodyStatusAdbpgInstanceHotDataGb()
            self.adbpg_instance_hot_data_gb = temp_model.from_map(m.get('adbpg_instance_hot_data_gb'))

        if m.get('adbpg_instance_total_data_gb') is not None:
            temp_model = main_models.DescribeHealthStatusResponseBodyStatusAdbpgInstanceTotalDataGb()
            self.adbpg_instance_total_data_gb = temp_model.from_map(m.get('adbpg_instance_total_data_gb'))

        if m.get('adbpg_master_disk_usage_percent_max') is not None:
            temp_model = main_models.DescribeHealthStatusResponseBodyStatusAdbpgMasterDiskUsagePercentMax()
            self.adbpg_master_disk_usage_percent_max = temp_model.from_map(m.get('adbpg_master_disk_usage_percent_max'))

        if m.get('adbpg_master_status') is not None:
            temp_model = main_models.DescribeHealthStatusResponseBodyStatusAdbpgMasterStatus()
            self.adbpg_master_status = temp_model.from_map(m.get('adbpg_master_status'))

        if m.get('adbpg_segment_status') is not None:
            temp_model = main_models.DescribeHealthStatusResponseBodyStatusAdbpgSegmentStatus()
            self.adbpg_segment_status = temp_model.from_map(m.get('adbpg_segment_status'))

        if m.get('adbpg_status') is not None:
            temp_model = main_models.DescribeHealthStatusResponseBodyStatusAdbpgStatus()
            self.adbpg_status = temp_model.from_map(m.get('adbpg_status'))

        if m.get('node_master_connection_status') is not None:
            temp_model = main_models.DescribeHealthStatusResponseBodyStatusNodeMasterConnectionStatus()
            self.node_master_connection_status = temp_model.from_map(m.get('node_master_connection_status'))

        if m.get('node_master_status') is not None:
            temp_model = main_models.DescribeHealthStatusResponseBodyStatusNodeMasterStatus()
            self.node_master_status = temp_model.from_map(m.get('node_master_status'))

        if m.get('node_segment_connection_status') is not None:
            temp_model = main_models.DescribeHealthStatusResponseBodyStatusNodeSegmentConnectionStatus()
            self.node_segment_connection_status = temp_model.from_map(m.get('node_segment_connection_status'))

        if m.get('node_segment_disk_status') is not None:
            temp_model = main_models.DescribeHealthStatusResponseBodyStatusNodeSegmentDiskStatus()
            self.node_segment_disk_status = temp_model.from_map(m.get('node_segment_disk_status'))

        return self

class DescribeHealthStatusResponseBodyStatusNodeSegmentDiskStatus(DaraModel):
    def __init__(
        self,
        status: str = None,
        value: float = None,
    ):
        # The storage status of compute nodes. Valid values:
        # 
        # *   **critical**: The compute node storage usage is greater than or equal to 90%. In this case, this metric is marked in red in the console and the instance is locked.
        # *   **warning**: The compute node storage usage is greater than or equal to 80% and less than 90%. In this case, this metric is marked in yellow in the console.
        # *   **healthy**: The compute node storage usage is less than 80%. In this case, this metric is marked in green in the console.
        # 
        # >  The compute node storage usage is the maximum storage usage among all compute nodes.
        self.status = status
        # The metric value of maximum compute node storage usage.
        # 
        # Unit: %.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeHealthStatusResponseBodyStatusNodeSegmentConnectionStatus(DaraModel):
    def __init__(
        self,
        status: str = None,
        value: float = None,
    ):
        # The connection health status of compute nodes. Valid values:
        # 
        # *   **critical**: The compute node connection usage is greater than or equal to 95%. In this case, this metric is marked in red in the console.
        # *   **warning**: The compute node connection usage is greater than or equal to 90% and less than 95%. In this case, this metric is marked in yellow in the console.
        # *   **healthy**: The compute node connection usage is less than 90%. In this case, this metric is marked in green in the console.
        # 
        # >  The compute node connection usage is the maximum connection usage among all compute nodes.
        self.status = status
        # The metric value of maximum compute node connection usage.
        # 
        # Unit: %.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeHealthStatusResponseBodyStatusNodeMasterStatus(DaraModel):
    def __init__(
        self,
        status: str = None,
        value: float = None,
    ):
        # The health status of the coordinator node. Valid values:
        # 
        # *   **critical**: The primary or standby coordinator node is unavailable. In this case, this metric is marked in red in the console.
        # *   **healthy**: Both the primary and standby coordinator nodes are available. In this case, this metric is marked in green in the console.
        self.status = status
        # The metric value of coordinator node health status. Valid values:
        # 
        # *   **1**: healthy
        # *   **0**: critical
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeHealthStatusResponseBodyStatusNodeMasterConnectionStatus(DaraModel):
    def __init__(
        self,
        status: str = None,
        value: float = None,
    ):
        # The connection health status of the coordinator node. Valid values:
        # 
        # *   **critical**: The coordinator node connection usage is greater than 95%. In this case, this metric is marked in red in the console.
        # *   **warning**: The coordinator node connection usage is greater than or equal to 90% and less than 95%. In this case, this metric is marked in yellow in the console.
        # *   **healthy**: The coordinator node connection usage is less than 90%. In this case, this metric is marked in green in the console.
        # 
        # >  The coordinator node connection usage is the maximum connection usage of the coordinator node.
        self.status = status
        # The metric value of coordinator node connection usage.
        # 
        # Unit: %.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeHealthStatusResponseBodyStatusAdbpgStatus(DaraModel):
    def __init__(
        self,
        status: str = None,
        value: float = None,
    ):
        # The health status of the instance. Valid values:
        # 
        # *   **critical**: The coordinator node or a compute node is unavailable. In this case, this metric is marked in red in the console.
        # *   **healthy**: All nodes are available. In this case, this metric is marked in green in the console.
        self.status = status
        # The metric value of instance health status. Valid values:
        # 
        # *   **1**: healthy
        # *   **0**: critical
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeHealthStatusResponseBodyStatusAdbpgSegmentStatus(DaraModel):
    def __init__(
        self,
        status: str = None,
        value: float = None,
    ):
        # The availability status of compute nodes. Valid values:
        # 
        # *   **critical**: All the primary and secondary compute nodes are unavailable. In this case, this metric is marked in red in the console.
        # *   **warning**: Fifty percent or more than fifty percent of compute nodes are unavailable. In this case, this metric is marked in yellow in the console.
        # *   **healthy**: All compute nodes are available. In this case, this metric is marked in green in the console.
        self.status = status
        # The metric value of compute node availability status.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeHealthStatusResponseBodyStatusAdbpgMasterStatus(DaraModel):
    def __init__(
        self,
        status: str = None,
        value: float = None,
    ):
        # The availability status of the coordinator node. Valid values:
        # 
        # *   **critical**: Both the primary and standby coordinator nodes are unavailable. In this case, this metric is marked in red in the console.
        # *   **warning**: The primary or standby coordinator node is unavailable. In this case, this metric is marked in yellow in the console.
        # *   **healthy**: Both the primary and standby coordinator nodes are available. In this case, this metric is marked in green in the console.
        self.status = status
        # The metric value of coordinator node availability status. Valid values:
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeHealthStatusResponseBodyStatusAdbpgMasterDiskUsagePercentMax(DaraModel):
    def __init__(
        self,
        status: str = None,
        value: float = None,
    ):
        # The status corresponding to the maximum storage usage of the coordinator node. Valid values:
        # 
        # *   **critical**: The coordinator node storage usage is greater than or equal to 90%. In this case, the instance is locked.
        # *   **warning**: The coordinator node storage usage is greater than or equal to 70% and less than 90%.
        # *   **healthy**: The coordinator node storage usage is less than 70%.
        self.status = status
        # The metric value of maximum coordinator node storage usage.
        # 
        # Unit: %.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeHealthStatusResponseBodyStatusAdbpgInstanceTotalDataGb(DaraModel):
    def __init__(
        self,
        value: float = None,
    ):
        # The total amount of data storage of the instance. Unit: GB.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeHealthStatusResponseBodyStatusAdbpgInstanceHotDataGb(DaraModel):
    def __init__(
        self,
        value: float = None,
    ):
        # The total amount of hot data storage. Unit: GB.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeHealthStatusResponseBodyStatusAdbpgInstanceColdDataGb(DaraModel):
    def __init__(
        self,
        value: float = None,
    ):
        # The total amount of cold data storage. Unit: GB.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeHealthStatusResponseBodyStatusAdbpgDiskUsagePercent(DaraModel):
    def __init__(
        self,
        status: str = None,
        value: float = None,
    ):
        # The status corresponding to the storage usage of the instance. Valid values:
        # 
        # *   **critical**: The instance storage usage is greater than or equal to 90%. In this case, the instance is locked.
        # *   **warning**: The instance storage usage is greater than or equal to 70% and less than 90%.
        # *   **healthy**: The instance storage usage is less than 70%.
        # 
        # >  The instance storage usage is the average storage usage of all compute nodes.
        self.status = status
        # The metric value of instance storage usage.
        # 
        # Unit: %.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeHealthStatusResponseBodyStatusAdbpgDiskStatus(DaraModel):
    def __init__(
        self,
        status: str = None,
        value: float = None,
    ):
        # The storage status of the instance. Valid values:
        # 
        # *   **critical**: The instance storage usage is greater than or equal to 90%. In this case, this metric is marked in red in the console and the instance is locked.
        # *   **warning**: The instance storage usage is greater than or equal to 70% and less than 90%. In this case, this metric is marked in yellow in the console.
        # *   **healthy**: The instance storage usage is less than 70%. In this case, this metric is marked in green in the console.
        # 
        # >  The instance storage usage is the average storage usage of all compute nodes.
        self.status = status
        # The metric value of instance storage usage.
        # 
        # Unit: %.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeHealthStatusResponseBodyStatusAdbpgConnectionStatus(DaraModel):
    def __init__(
        self,
        status: str = None,
        value: float = None,
    ):
        # The connection health status of the instance. Valid values:
        # 
        # *   **critical**: The instance connection usage is greater than 95%. In this case, this metric is marked in red in the console.
        # *   **warning**: The instance connection usage is greater than 90% and less than or equal to 95%. In this case, this metric is marked in yellow in the console.
        # *   **healthy**: The instance connection usage is less than or equal to 90%. In this case, this metric is marked in green in the console.
        # 
        # >  The instance connection usage is the maximum connection usage among all the coordinator and compute nodes.
        self.status = status
        # The metric value of instance connection usage.
        # 
        # Unit: %.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeHealthStatusResponseBodyStatusAdbgpSegmentDiskUsagePercentMax(DaraModel):
    def __init__(
        self,
        status: str = None,
        value: float = None,
    ):
        # The status corresponding to the maximum storage usage among all compute nodes. Valid values:
        # 
        # *   **critical**: The compute node storage usage is greater than or equal to 90%. In this case, the instance is locked.
        # *   **warning**: The compute node storage usage is greater than or equal to 80% and less than 90%.
        # *   **healthy**: The compute node storage usage is less than 80%.
        self.status = status
        # The metric value of maximum compute node storage usage.
        # 
        # Unit: %.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

