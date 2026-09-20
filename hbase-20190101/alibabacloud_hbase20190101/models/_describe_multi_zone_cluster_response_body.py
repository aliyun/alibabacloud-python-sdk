# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbase20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeMultiZoneClusterResponseBody(DaraModel):
    def __init__(
        self,
        arbiter_vswitch_ids: str = None,
        arbiter_zone_id: str = None,
        auto_renewal: bool = None,
        cluster_id: str = None,
        cluster_name: str = None,
        cold_storage_size: int = None,
        core_disk_count: str = None,
        core_disk_size: int = None,
        core_disk_type: str = None,
        core_instance_type: str = None,
        core_node_count: int = None,
        created_time: str = None,
        created_time_utc: str = None,
        duration: int = None,
        encryption_key: str = None,
        encryption_type: str = None,
        engine: str = None,
        expire_time: str = None,
        expire_time_utc: str = None,
        initial_root_password: str = None,
        instance_id: str = None,
        instance_name: str = None,
        is_deletion_protection: bool = None,
        log_disk_count: str = None,
        log_disk_size: int = None,
        log_disk_type: str = None,
        log_instance_type: str = None,
        log_node_count: int = None,
        maintain_end_time: str = None,
        maintain_start_time: str = None,
        major_version: str = None,
        master_disk_size: int = None,
        master_disk_type: str = None,
        master_instance_type: str = None,
        master_node_count: int = None,
        module_id: int = None,
        module_stack_version: str = None,
        multi_zone_combination: str = None,
        multi_zone_instance_models: main_models.DescribeMultiZoneClusterResponseBodyMultiZoneInstanceModels = None,
        network_type: str = None,
        parent_id: str = None,
        pay_type: str = None,
        primary_vswitch_ids: str = None,
        primary_zone_id: str = None,
        region_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        standby_vswitch_ids: str = None,
        standby_zone_id: str = None,
        status: str = None,
        tags: main_models.DescribeMultiZoneClusterResponseBodyTags = None,
        task_progress: str = None,
        task_status: str = None,
        vpc_id: str = None,
    ):
        # The vSwitch ID of the arbiter zone.
        self.arbiter_vswitch_ids = arbiter_vswitch_ids
        # The zone ID of the arbiter zone.
        self.arbiter_zone_id = arbiter_zone_id
        # Indicates whether auto-renewal is enabled for the multi-zone instance when PayType is set to Prepaid. Valid values:
        # - True: Auto-renewal is enabled.
        # - False: Auto-renewal is disabled.
        self.auto_renewal = auto_renewal
        # The cluster ID.
        self.cluster_id = cluster_id
        # The cluster name.
        self.cluster_name = cluster_name
        # The cold storage size. Unit: GB.
        self.cold_storage_size = cold_storage_size
        # The number of core node disks.
        self.core_disk_count = core_disk_count
        # The disk size of a core node. Unit: GB.
        self.core_disk_size = core_disk_size
        # The disk type of core nodes. Valid values:
        # - cloud_efficiency: ultra cloud disk.
        # - cloud_ssd: standard SSD.
        # - local_hdd_pro: throughput-intensive local disk.
        # - local_ssd_pro: I/O-intensive local disk.
        self.core_disk_type = core_disk_type
        # The node specifications of core nodes.
        self.core_instance_type = core_instance_type
        # The number of core nodes. The minimum value is 4, and the increment is a multiple of 2.
        self.core_node_count = core_node_count
        # The creation time in the current time zone.
        self.created_time = created_time
        # The creation time in UTC.
        self.created_time_utc = created_time_utc
        # The Unified Auto Renewal Cycle. This parameter is not returned for pay-as-you-go instances.
        # - Monthly subscription: The auto-renewal epoch is 1 month.
        # - Yearly subscription: The auto-renewal epoch is 1 year (12 months).
        self.duration = duration
        # The ID of the encryption key. This parameter is empty if encryption is not enabled.
        # 
        # > Cloud disk encryption cannot be disabled after it is enabled.
        self.encryption_key = encryption_key
        # The encryption type. Valid values:
        # 
        # - NULL: Encryption is not enabled. This is the default value.
        # 
        # - CloudDisk: Cloud disk encryption. The encryption key is specified by the **EncryptionKey** parameter.
        self.encryption_type = encryption_type
        # The service type. Currently, only hbaseue is supported.
        self.engine = engine
        # The expiration time in the current time zone. This parameter is returned only when PayType is set to Prepaid.
        self.expire_time = expire_time
        # The expiration time in UTC. This parameter is returned only when PayType is set to Prepaid.
        self.expire_time_utc = expire_time_utc
        # The initial default password.
        self.initial_root_password = initial_root_password
        # The cluster ID.
        self.instance_id = instance_id
        # The cluster name.
        self.instance_name = instance_name
        # Indicates whether deletion protection is enabled. Valid values:
        # - True: Deletion protection is enabled. The instance cannot be deleted. An error message is returned if you attempt to delete the instance.
        # - False: Deletion protection is disabled. The instance can be deleted.
        self.is_deletion_protection = is_deletion_protection
        # The number of disks per log node.
        self.log_disk_count = log_disk_count
        # The size of a single disk on a log node. Unit: GB.
        self.log_disk_size = log_disk_size
        # The disk type of log nodes. Valid values:
        # - cloud_efficiency: ultra cloud disk.
        # - cloud_ssd: standard SSD.
        # - local_hdd_pro: throughput-intensive local disk.
        # - local_ssd_pro: I/O-intensive local disk.
        self.log_disk_type = log_disk_type
        # The node specifications of log nodes. You can call [DescribeInstanceType](https://help.aliyun.com/document_detail/145796.html) to query the exact information.
        self.log_instance_type = log_instance_type
        # The number of log nodes. The minimum value is 4, and the value must be a multiple of 4.
        self.log_node_count = log_node_count
        # The end time of the O&M window. The format is HH:MMZ, such as 20:00Z.
        self.maintain_end_time = maintain_end_time
        # The start time of the O&M window. The format is HH:MMZ, such as 20:00Z.
        self.maintain_start_time = maintain_start_time
        # The major version based on the engine type. Currently, only version 2.0 of hbaseue is supported.
        self.major_version = major_version
        # The disk size of master nodes.
        self.master_disk_size = master_disk_size
        # The disk type of master nodes.
        self.master_disk_type = master_disk_type
        # The node specifications of master nodes.
        self.master_instance_type = master_instance_type
        # The number of master nodes.
        self.master_node_count = master_node_count
        # The module ID.
        self.module_id = module_id
        # The module software stack version.
        self.module_stack_version = module_stack_version
        # The zone combination of the multi-zone instance.
        self.multi_zone_combination = multi_zone_combination
        self.multi_zone_instance_models = multi_zone_instance_models
        # The network type. Currently, only VPC is supported.
        self.network_type = network_type
        # The instance ID of the primary instance. This parameter is returned only when the instance is a component instance.
        self.parent_id = parent_id
        # The billing method. Valid values:
        # - Prepaid: subscription.
        # - Postpaid: pay-as-you-go.
        self.pay_type = pay_type
        # The vSwitch ID of the primary zone instance.
        self.primary_vswitch_ids = primary_vswitch_ids
        # The zone ID of the primary zone instance.
        self.primary_zone_id = primary_zone_id
        # The region ID.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The ID of the resource group to which the resource belongs.
        self.resource_group_id = resource_group_id
        # The vSwitch ID of the secondary zone instance.
        self.standby_vswitch_ids = standby_vswitch_ids
        # The zone ID of the secondary zone instance.
        self.standby_zone_id = standby_zone_id
        # The cluster status. Valid values:
        # - CREATING: The cluster is being created.
        # - ACTIVATION: The cluster is running.
        # - DELETING: The cluster is being deleted.
        # - RESTARTING: The cluster is being restarted.
        self.status = status
        self.tags = tags
        # The progress of the task running on the instance, in percentage (%). Tasks initiated from the ApsaraDB for HBase console include specification changes, node scale-out, node scale-in, instance restart, and minor engine version update.
        self.task_progress = task_progress
        # The task status. Valid values:
        # - running: The task is running.
        # - pause: The task is paused.
        # - fail: The task is interrupted.
        # - finish: The task is completed.
        self.task_status = task_status
        # The VPC ID.
        self.vpc_id = vpc_id

    def validate(self):
        if self.multi_zone_instance_models:
            self.multi_zone_instance_models.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arbiter_vswitch_ids is not None:
            result['ArbiterVSwitchIds'] = self.arbiter_vswitch_ids

        if self.arbiter_zone_id is not None:
            result['ArbiterZoneId'] = self.arbiter_zone_id

        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.cold_storage_size is not None:
            result['ColdStorageSize'] = self.cold_storage_size

        if self.core_disk_count is not None:
            result['CoreDiskCount'] = self.core_disk_count

        if self.core_disk_size is not None:
            result['CoreDiskSize'] = self.core_disk_size

        if self.core_disk_type is not None:
            result['CoreDiskType'] = self.core_disk_type

        if self.core_instance_type is not None:
            result['CoreInstanceType'] = self.core_instance_type

        if self.core_node_count is not None:
            result['CoreNodeCount'] = self.core_node_count

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.created_time_utc is not None:
            result['CreatedTimeUTC'] = self.created_time_utc

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key

        if self.encryption_type is not None:
            result['EncryptionType'] = self.encryption_type

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.expire_time_utc is not None:
            result['ExpireTimeUTC'] = self.expire_time_utc

        if self.initial_root_password is not None:
            result['InitialRootPassword'] = self.initial_root_password

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.is_deletion_protection is not None:
            result['IsDeletionProtection'] = self.is_deletion_protection

        if self.log_disk_count is not None:
            result['LogDiskCount'] = self.log_disk_count

        if self.log_disk_size is not None:
            result['LogDiskSize'] = self.log_disk_size

        if self.log_disk_type is not None:
            result['LogDiskType'] = self.log_disk_type

        if self.log_instance_type is not None:
            result['LogInstanceType'] = self.log_instance_type

        if self.log_node_count is not None:
            result['LogNodeCount'] = self.log_node_count

        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time

        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time

        if self.major_version is not None:
            result['MajorVersion'] = self.major_version

        if self.master_disk_size is not None:
            result['MasterDiskSize'] = self.master_disk_size

        if self.master_disk_type is not None:
            result['MasterDiskType'] = self.master_disk_type

        if self.master_instance_type is not None:
            result['MasterInstanceType'] = self.master_instance_type

        if self.master_node_count is not None:
            result['MasterNodeCount'] = self.master_node_count

        if self.module_id is not None:
            result['ModuleId'] = self.module_id

        if self.module_stack_version is not None:
            result['ModuleStackVersion'] = self.module_stack_version

        if self.multi_zone_combination is not None:
            result['MultiZoneCombination'] = self.multi_zone_combination

        if self.multi_zone_instance_models is not None:
            result['MultiZoneInstanceModels'] = self.multi_zone_instance_models.to_map()

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.primary_vswitch_ids is not None:
            result['PrimaryVSwitchIds'] = self.primary_vswitch_ids

        if self.primary_zone_id is not None:
            result['PrimaryZoneId'] = self.primary_zone_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.standby_vswitch_ids is not None:
            result['StandbyVSwitchIds'] = self.standby_vswitch_ids

        if self.standby_zone_id is not None:
            result['StandbyZoneId'] = self.standby_zone_id

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.task_progress is not None:
            result['TaskProgress'] = self.task_progress

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArbiterVSwitchIds') is not None:
            self.arbiter_vswitch_ids = m.get('ArbiterVSwitchIds')

        if m.get('ArbiterZoneId') is not None:
            self.arbiter_zone_id = m.get('ArbiterZoneId')

        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ColdStorageSize') is not None:
            self.cold_storage_size = m.get('ColdStorageSize')

        if m.get('CoreDiskCount') is not None:
            self.core_disk_count = m.get('CoreDiskCount')

        if m.get('CoreDiskSize') is not None:
            self.core_disk_size = m.get('CoreDiskSize')

        if m.get('CoreDiskType') is not None:
            self.core_disk_type = m.get('CoreDiskType')

        if m.get('CoreInstanceType') is not None:
            self.core_instance_type = m.get('CoreInstanceType')

        if m.get('CoreNodeCount') is not None:
            self.core_node_count = m.get('CoreNodeCount')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('CreatedTimeUTC') is not None:
            self.created_time_utc = m.get('CreatedTimeUTC')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')

        if m.get('EncryptionType') is not None:
            self.encryption_type = m.get('EncryptionType')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('ExpireTimeUTC') is not None:
            self.expire_time_utc = m.get('ExpireTimeUTC')

        if m.get('InitialRootPassword') is not None:
            self.initial_root_password = m.get('InitialRootPassword')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('IsDeletionProtection') is not None:
            self.is_deletion_protection = m.get('IsDeletionProtection')

        if m.get('LogDiskCount') is not None:
            self.log_disk_count = m.get('LogDiskCount')

        if m.get('LogDiskSize') is not None:
            self.log_disk_size = m.get('LogDiskSize')

        if m.get('LogDiskType') is not None:
            self.log_disk_type = m.get('LogDiskType')

        if m.get('LogInstanceType') is not None:
            self.log_instance_type = m.get('LogInstanceType')

        if m.get('LogNodeCount') is not None:
            self.log_node_count = m.get('LogNodeCount')

        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')

        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')

        if m.get('MajorVersion') is not None:
            self.major_version = m.get('MajorVersion')

        if m.get('MasterDiskSize') is not None:
            self.master_disk_size = m.get('MasterDiskSize')

        if m.get('MasterDiskType') is not None:
            self.master_disk_type = m.get('MasterDiskType')

        if m.get('MasterInstanceType') is not None:
            self.master_instance_type = m.get('MasterInstanceType')

        if m.get('MasterNodeCount') is not None:
            self.master_node_count = m.get('MasterNodeCount')

        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')

        if m.get('ModuleStackVersion') is not None:
            self.module_stack_version = m.get('ModuleStackVersion')

        if m.get('MultiZoneCombination') is not None:
            self.multi_zone_combination = m.get('MultiZoneCombination')

        if m.get('MultiZoneInstanceModels') is not None:
            temp_model = main_models.DescribeMultiZoneClusterResponseBodyMultiZoneInstanceModels()
            self.multi_zone_instance_models = temp_model.from_map(m.get('MultiZoneInstanceModels'))

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('PrimaryVSwitchIds') is not None:
            self.primary_vswitch_ids = m.get('PrimaryVSwitchIds')

        if m.get('PrimaryZoneId') is not None:
            self.primary_zone_id = m.get('PrimaryZoneId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('StandbyVSwitchIds') is not None:
            self.standby_vswitch_ids = m.get('StandbyVSwitchIds')

        if m.get('StandbyZoneId') is not None:
            self.standby_zone_id = m.get('StandbyZoneId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeMultiZoneClusterResponseBodyTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('TaskProgress') is not None:
            self.task_progress = m.get('TaskProgress')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeMultiZoneClusterResponseBodyTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeMultiZoneClusterResponseBodyTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeMultiZoneClusterResponseBodyTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeMultiZoneClusterResponseBodyTagsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeMultiZoneClusterResponseBodyMultiZoneInstanceModels(DaraModel):
    def __init__(
        self,
        multi_zone_instance_model: List[main_models.DescribeMultiZoneClusterResponseBodyMultiZoneInstanceModelsMultiZoneInstanceModel] = None,
    ):
        self.multi_zone_instance_model = multi_zone_instance_model

    def validate(self):
        if self.multi_zone_instance_model:
            for v1 in self.multi_zone_instance_model:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MultiZoneInstanceModel'] = []
        if self.multi_zone_instance_model is not None:
            for k1 in self.multi_zone_instance_model:
                result['MultiZoneInstanceModel'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.multi_zone_instance_model = []
        if m.get('MultiZoneInstanceModel') is not None:
            for k1 in m.get('MultiZoneInstanceModel'):
                temp_model = main_models.DescribeMultiZoneClusterResponseBodyMultiZoneInstanceModelsMultiZoneInstanceModel()
                self.multi_zone_instance_model.append(temp_model.from_map(k1))

        return self

class DescribeMultiZoneClusterResponseBodyMultiZoneInstanceModelsMultiZoneInstanceModel(DaraModel):
    def __init__(
        self,
        hdfs_minor_version: str = None,
        ins_name: str = None,
        is_hdfs_latest_version: str = None,
        is_latest_version: bool = None,
        latest_hdfs_minor_version: str = None,
        latest_minor_version: str = None,
        minor_version: str = None,
        role: str = None,
        status: str = None,
    ):
        self.hdfs_minor_version = hdfs_minor_version
        self.ins_name = ins_name
        self.is_hdfs_latest_version = is_hdfs_latest_version
        self.is_latest_version = is_latest_version
        self.latest_hdfs_minor_version = latest_hdfs_minor_version
        self.latest_minor_version = latest_minor_version
        self.minor_version = minor_version
        self.role = role
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hdfs_minor_version is not None:
            result['HdfsMinorVersion'] = self.hdfs_minor_version

        if self.ins_name is not None:
            result['InsName'] = self.ins_name

        if self.is_hdfs_latest_version is not None:
            result['IsHdfsLatestVersion'] = self.is_hdfs_latest_version

        if self.is_latest_version is not None:
            result['IsLatestVersion'] = self.is_latest_version

        if self.latest_hdfs_minor_version is not None:
            result['LatestHdfsMinorVersion'] = self.latest_hdfs_minor_version

        if self.latest_minor_version is not None:
            result['LatestMinorVersion'] = self.latest_minor_version

        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version

        if self.role is not None:
            result['Role'] = self.role

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HdfsMinorVersion') is not None:
            self.hdfs_minor_version = m.get('HdfsMinorVersion')

        if m.get('InsName') is not None:
            self.ins_name = m.get('InsName')

        if m.get('IsHdfsLatestVersion') is not None:
            self.is_hdfs_latest_version = m.get('IsHdfsLatestVersion')

        if m.get('IsLatestVersion') is not None:
            self.is_latest_version = m.get('IsLatestVersion')

        if m.get('LatestHdfsMinorVersion') is not None:
            self.latest_hdfs_minor_version = m.get('LatestHdfsMinorVersion')

        if m.get('LatestMinorVersion') is not None:
            self.latest_minor_version = m.get('LatestMinorVersion')

        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

