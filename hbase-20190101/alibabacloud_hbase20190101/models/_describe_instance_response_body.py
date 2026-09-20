# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbase20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceResponseBody(DaraModel):
    def __init__(
        self,
        auto_renewal: bool = None,
        backup_status: str = None,
        cluster_id: str = None,
        cluster_name: str = None,
        cluster_type: str = None,
        cold_storage_size: int = None,
        cold_storage_status: str = None,
        confirm_maintain_time: str = None,
        core_disk_count: str = None,
        core_disk_size: int = None,
        core_disk_type: str = None,
        core_instance_type: str = None,
        core_node_count: int = None,
        created_time: str = None,
        created_time_utc: str = None,
        duration: int = None,
        enable_hbase_proxy: bool = None,
        encryption_key: str = None,
        encryption_type: str = None,
        engine: str = None,
        expire_time: str = None,
        expire_time_utc: str = None,
        initial_root_password: str = None,
        instance_id: str = None,
        instance_name: str = None,
        is_deletion_protection: bool = None,
        is_ha: bool = None,
        is_latest_version: bool = None,
        is_multi_model: bool = None,
        lproxy_minor_version: str = None,
        maintain_end_time: str = None,
        maintain_start_time: str = None,
        major_version: str = None,
        master_disk_size: int = None,
        master_disk_type: str = None,
        master_instance_type: str = None,
        master_node_count: int = None,
        minor_version: str = None,
        module_id: int = None,
        module_stack_version: str = None,
        need_upgrade: bool = None,
        need_upgrade_comps: main_models.DescribeInstanceResponseBodyNeedUpgradeComps = None,
        network_type: str = None,
        parent_id: str = None,
        pay_type: str = None,
        region_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        single_zone_risk_alert: main_models.DescribeInstanceResponseBodySingleZoneRiskAlert = None,
        status: str = None,
        tags: main_models.DescribeInstanceResponseBodyTags = None,
        task_progress: str = None,
        task_status: str = None,
        vpc_id: str = None,
        vswitch_id: str = None,
        zone_id: str = None,
    ):
        # Indicates whether auto-renewal is enabled for the instance. Valid values:
        # - **true**: Auto-renewal is enabled.
        # - **false**: Auto-renewal is not enabled.
        # 
        # > This parameter is returned only when PayType is set to Prepaid (subscription).
        self.auto_renewal = auto_renewal
        # Indicates whether the backup feature is supported. Valid values:
        # - **open**: The backup feature is supported.
        # - **close**: The backup feature is not supported.
        self.backup_status = backup_status
        # The instance ID.
        self.cluster_id = cluster_id
        # The instance name.
        self.cluster_name = cluster_name
        # The instance type. Valid values:
        # - **cluster**: Cluster Edition.
        # - **single**: single-node.
        self.cluster_type = cluster_type
        # The cold storage size. Unit: GB.
        self.cold_storage_size = cold_storage_size
        # Indicates whether the cold storage feature is supported. Valid values:
        # - **open**: The cold storage feature is supported.
        # - **close**: The cold storage feature is not supported.
        self.cold_storage_status = cold_storage_status
        # Indicates whether the O&M window of the instance has been confirmed for the first time. Valid values:
        # - **true**: Confirmed.
        # - **false**: Not confirmed.
        # 
        # > The **Confirm the O&M window for the first time** dialog box appears only when you access the **Basic Information** page of the instance for the first time.
        self.confirm_maintain_time = confirm_maintain_time
        # The number of core node disks.
        self.core_disk_count = core_disk_count
        # The disk capacity of core nodes. Unit: GB.
        self.core_disk_size = core_disk_size
        # The disk type of core nodes. Valid values:
        # - **cloud_efficiency**: ultra cloud disk.
        # - **cloud_ssd**: standard SSD.
        # - **local_hdd**: local HDD.
        # - **local__ssd**: local SSD.
        self.core_disk_type = core_disk_type
        # The node specifications of core nodes.
        self.core_instance_type = core_instance_type
        # The number of core nodes.
        self.core_node_count = core_node_count
        # The time when the instance was created.
        self.created_time = created_time
        # The time when the instance was created, in UTC format.
        self.created_time_utc = created_time_utc
        # The Unified Auto Renewal Cycle.
        # 
        # - Monthly subscription: The auto-renewal epoch is 1 month.
        # - Yearly subscription: The auto-renewal epoch is 1 year (12 months).
        # 
        # > This parameter is returned only when PayType is set to Prepaid (subscription).
        self.duration = duration
        # Indicates whether access from the HBase open source client is supported. Valid values:
        # 
        # - **true**: Access is supported.
        # 
        # - **false**: Access is not supported.
        # 
        # This parameter is required.
        self.enable_hbase_proxy = enable_hbase_proxy
        # The encryption key.
        # 
        # > This parameter is returned only when the encryption type is **CloudDisk**.
        self.encryption_key = encryption_key
        # The encryption type. Valid values:
        # - **NoEncryption**: Encryption is not enabled.
        # - **CloudDisk**: Cloud disk encryption is enabled.
        # - **EncryptionKey**: The encryption key specified by the parameter.
        # 
        # > Cloud disk encryption cannot be disabled after it is enabled.
        self.encryption_type = encryption_type
        # The database engine type. Valid values:
        # - **hbase**: ApsaraDB for HBase Standard Edition or ApsaraDB for HBase single-node.
        # - **hbaseue**: ApsaraDB for HBase Performance-enhanced Edition.
        # - **serverlesshbase**: ApsaraDB for HBase Serverless Edition.
        # - **bds**: BDS instance.
        self.engine = engine
        # The time when the instance expires.
        self.expire_time = expire_time
        # The time when the instance expires, in UTC format.
        self.expire_time_utc = expire_time_utc
        # The initial default password.
        self.initial_root_password = initial_root_password
        # The instance ID.
        self.instance_id = instance_id
        # The instance name.
        self.instance_name = instance_name
        # Indicates whether deletion protection is enabled. Valid values:
        # - **true**: Enabled.
        # - **false**: Not enabled.
        self.is_deletion_protection = is_deletion_protection
        # Indicates whether the instance is configured for high availability. Valid values:
        # - **true**: Configured for high availability.
        # - **false**: Not configured for high availability.
        # 
        # > - Cluster Edition instances are configured for high availability with default configurations and use 2 master nodes.
        # - Single-node instances are configured with the actual active capacity.
        self.is_ha = is_ha
        # Indicates whether the instance is the latest version. Valid values:
        # - **true**: The instance is the latest version.
        # - **false**: The instance is not the latest version.
        self.is_latest_version = is_latest_version
        # Indicates whether the instance is a multi-model Cluster Edition instance. Valid values:
        # - **true**: The instance is a multi-model Cluster Edition instance.
        # - **false**: The instance is not a multi-model Cluster Edition instance.
        self.is_multi_model = is_multi_model
        # The minor version of the LPROXY service.
        self.lproxy_minor_version = lproxy_minor_version
        # The end time of the O&M window.
        self.maintain_end_time = maintain_end_time
        # The start time of the O&M window.
        self.maintain_start_time = maintain_start_time
        # The major version number.
        self.major_version = major_version
        # The disk capacity of master nodes. Unit: GB.
        self.master_disk_size = master_disk_size
        # The disk type of master nodes. Valid values:
        # - **cloud_efficiency**: ultra cloud disk.
        # - **cloud_ssd**: standard SSD.
        # 
        # > This parameter is returned for single-node instances.
        self.master_disk_type = master_disk_type
        # The node specifications of master nodes.
        self.master_instance_type = master_instance_type
        # The master node type. Valid values:
        # - **0**: The master node is a single node.
        # - **2**: The master node is in Cluster Edition.
        self.master_node_count = master_node_count
        # The minor version number of the instance.
        self.minor_version = minor_version
        # The module ID.
        self.module_id = module_id
        # The module type version.
        self.module_stack_version = module_stack_version
        # Indicates whether the instance components need to be upgraded. Valid values:
        # - **true**: Upgrade is required.
        # - **false**: Upgrade is not required.
        self.need_upgrade = need_upgrade
        self.need_upgrade_comps = need_upgrade_comps
        # The network type. Valid values:
        # - **VPC**: Virtual Private Cloud. If the network type is VPC, the VswitchId and VpcId parameters are returned.
        # - **CLASSIC**: classic network.
        self.network_type = network_type
        # The parent instance ID.
        self.parent_id = parent_id
        # The billing method of the instance. Valid values:
        # 
        # - **Prepaid**: subscription.
        # - **Postpaid**: pay-as-you-go.
        self.pay_type = pay_type
        # The ID of the region in which the instance resides.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The single-zone risk alert information.
        self.single_zone_risk_alert = single_zone_risk_alert
        # The instance status. Valid values:
        # - **CREATING**: The instance is being created.
        # - **ACTIVATION**: The instance is running.
        # - **DELETING**: The instance is being deleted.
        # - **RESTARTING**: The instance is being restarted.
        # - **MINOR_VERSION_TRANSING**: A minor engine version update is in progress.
        self.status = status
        self.tags = tags
        # The task progress of the instance, in percentage (%). Tasks initiated from the ApsaraDB for HBase console include specification changes, node scale-out, node scale-in, instance restart, and minor engine version updates.
        self.task_progress = task_progress
        # The task status. Valid values:
        # - running: The task is running.
        # - pause: The task is paused.
        # - fail: The task is interrupted.
        # - finish: The task is completed.
        self.task_status = task_status
        # The VPC ID. This parameter is returned when **NetworkType** is **2**.
        self.vpc_id = vpc_id
        # The vSwitch ID. This parameter is returned when **NetworkType** is **2**.
        self.vswitch_id = vswitch_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.need_upgrade_comps:
            self.need_upgrade_comps.validate()
        if self.single_zone_risk_alert:
            self.single_zone_risk_alert.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal

        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.cold_storage_size is not None:
            result['ColdStorageSize'] = self.cold_storage_size

        if self.cold_storage_status is not None:
            result['ColdStorageStatus'] = self.cold_storage_status

        if self.confirm_maintain_time is not None:
            result['ConfirmMaintainTime'] = self.confirm_maintain_time

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

        if self.enable_hbase_proxy is not None:
            result['EnableHbaseProxy'] = self.enable_hbase_proxy

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

        if self.is_ha is not None:
            result['IsHa'] = self.is_ha

        if self.is_latest_version is not None:
            result['IsLatestVersion'] = self.is_latest_version

        if self.is_multi_model is not None:
            result['IsMultiModel'] = self.is_multi_model

        if self.lproxy_minor_version is not None:
            result['LproxyMinorVersion'] = self.lproxy_minor_version

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

        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version

        if self.module_id is not None:
            result['ModuleId'] = self.module_id

        if self.module_stack_version is not None:
            result['ModuleStackVersion'] = self.module_stack_version

        if self.need_upgrade is not None:
            result['NeedUpgrade'] = self.need_upgrade

        if self.need_upgrade_comps is not None:
            result['NeedUpgradeComps'] = self.need_upgrade_comps.to_map()

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.single_zone_risk_alert is not None:
            result['SingleZoneRiskAlert'] = self.single_zone_risk_alert.to_map()

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

        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')

        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('ColdStorageSize') is not None:
            self.cold_storage_size = m.get('ColdStorageSize')

        if m.get('ColdStorageStatus') is not None:
            self.cold_storage_status = m.get('ColdStorageStatus')

        if m.get('ConfirmMaintainTime') is not None:
            self.confirm_maintain_time = m.get('ConfirmMaintainTime')

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

        if m.get('EnableHbaseProxy') is not None:
            self.enable_hbase_proxy = m.get('EnableHbaseProxy')

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

        if m.get('IsHa') is not None:
            self.is_ha = m.get('IsHa')

        if m.get('IsLatestVersion') is not None:
            self.is_latest_version = m.get('IsLatestVersion')

        if m.get('IsMultiModel') is not None:
            self.is_multi_model = m.get('IsMultiModel')

        if m.get('LproxyMinorVersion') is not None:
            self.lproxy_minor_version = m.get('LproxyMinorVersion')

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

        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')

        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')

        if m.get('ModuleStackVersion') is not None:
            self.module_stack_version = m.get('ModuleStackVersion')

        if m.get('NeedUpgrade') is not None:
            self.need_upgrade = m.get('NeedUpgrade')

        if m.get('NeedUpgradeComps') is not None:
            temp_model = main_models.DescribeInstanceResponseBodyNeedUpgradeComps()
            self.need_upgrade_comps = temp_model.from_map(m.get('NeedUpgradeComps'))

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SingleZoneRiskAlert') is not None:
            temp_model = main_models.DescribeInstanceResponseBodySingleZoneRiskAlert()
            self.single_zone_risk_alert = temp_model.from_map(m.get('SingleZoneRiskAlert'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeInstanceResponseBodyTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('TaskProgress') is not None:
            self.task_progress = m.get('TaskProgress')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeInstanceResponseBodyTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeInstanceResponseBodyTagsTag] = None,
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
                temp_model = main_models.DescribeInstanceResponseBodyTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeInstanceResponseBodyTagsTag(DaraModel):
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

class DescribeInstanceResponseBodySingleZoneRiskAlert(DaraModel):
    def __init__(
        self,
        confirm_date: str = None,
        disposition_type: str = None,
        need_alert: bool = None,
        planned_completion_date: str = None,
    ):
        # The confirmation date.
        self.confirm_date = confirm_date
        # The disposition type.
        self.disposition_type = disposition_type
        # Indicates whether an alert is required.
        self.need_alert = need_alert
        # The planned completion date.
        self.planned_completion_date = planned_completion_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.confirm_date is not None:
            result['ConfirmDate'] = self.confirm_date

        if self.disposition_type is not None:
            result['DispositionType'] = self.disposition_type

        if self.need_alert is not None:
            result['NeedAlert'] = self.need_alert

        if self.planned_completion_date is not None:
            result['PlannedCompletionDate'] = self.planned_completion_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfirmDate') is not None:
            self.confirm_date = m.get('ConfirmDate')

        if m.get('DispositionType') is not None:
            self.disposition_type = m.get('DispositionType')

        if m.get('NeedAlert') is not None:
            self.need_alert = m.get('NeedAlert')

        if m.get('PlannedCompletionDate') is not None:
            self.planned_completion_date = m.get('PlannedCompletionDate')

        return self

class DescribeInstanceResponseBodyNeedUpgradeComps(DaraModel):
    def __init__(
        self,
        comps: List[str] = None,
    ):
        self.comps = comps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comps is not None:
            result['Comps'] = self.comps

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comps') is not None:
            self.comps = m.get('Comps')

        return self

