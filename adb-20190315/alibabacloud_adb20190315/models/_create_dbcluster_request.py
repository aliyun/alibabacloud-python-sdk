# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20190315 import models as main_models
from darabonba.model import DaraModel

class CreateDBClusterRequest(DaraModel):
    def __init__(
        self,
        backup_set_id: str = None,
        client_token: str = None,
        compute_resource: str = None,
        dbcluster_category: str = None,
        dbcluster_class: str = None,
        dbcluster_description: str = None,
        dbcluster_network_type: str = None,
        dbcluster_version: str = None,
        dbnode_group_count: str = None,
        dbnode_storage: str = None,
        disk_encryption: bool = None,
        elastic_ioresource: str = None,
        enable_ssl: bool = None,
        executor_count: str = None,
        kms_id: str = None,
        mode: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pay_type: str = None,
        period: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        restore_time: str = None,
        restore_type: str = None,
        source_dbinstance_name: str = None,
        storage_resource: str = None,
        storage_type: str = None,
        tag: List[main_models.CreateDBClusterRequestTag] = None,
        used_time: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # A reserved parameter.
        self.backup_set_id = backup_set_id
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The value is case-sensitive and can contain a maximum of 64 ASCII characters in length.
        self.client_token = client_token
        # The computing resources of the cluster. You can use computing resources to compute data. The increase in the computing resources can accelerate data queries. The computing resources are available for Cluster Edition and Basic Edition.
        # 
        # *   Computing resources for Cluster Edition include 16 cores and 64 GB memory, 24 cores and 96 GB memory, and 32 cores or more. Cluster Edition supports resource isolation, scheduled scaling, and tiered storage of hot and cold data.
        # *   Computing resources for Basic Edition include 8 cores and 32 GB memory and 16 cores and 64 GB memory. Alibaba Cloud does not provide an SLA guarantee for Basic Edition, and 4 to 8 hours are required for a failover. We recommend that you do not use Basic Edition in production environments.
        # 
        # > 
        # 
        # *   You can call the [DescribeAvailableResource](https://help.aliyun.com/document_detail/190632.html) operation to query the available computing resources in a region.
        # 
        # *   This parameter must be specified when Mode is set to **Flexible**.
        self.compute_resource = compute_resource
        # The edition of the cluster. Valid values:
        # 
        # *   **Cluster**: reserved mode for Cluster Edition
        # 
        # <!---->
        # 
        # *   **MixedStorage**: elastic mode for Cluster Edition
        # 
        # >  If the DBClusterCategory parameter is set to Cluster, you must set the Mode parameter to Reserver. If the DBClusterCategory parameter is set to MixedStorage, you must set the Mode parameter to Flexible. Otherwise, the cluster fails to be created.
        # 
        # This parameter is required.
        self.dbcluster_category = dbcluster_category
        # The specification of the cluster. Valid values:
        # 
        # *   **C8**
        # *   **C32**
        # 
        # >  This parameter is required if the Mode parameter is set to Reserver.
        self.dbcluster_class = dbcluster_class
        # The description of the cluster.
        # 
        # *   The description cannot start with `http://` or `https`.
        # *   The description must be 2 to 256 characters in length.
        self.dbcluster_description = dbcluster_description
        # The network type of the cluster. Set the value to **VPC**.
        # 
        # This parameter is required.
        self.dbcluster_network_type = dbcluster_network_type
        # The version of the cluster. Set the value to **3.0**.
        # 
        # This parameter is required.
        self.dbcluster_version = dbcluster_version
        # The number of node groups. Valid values: 1 to 200 (integer).
        # 
        # >  This parameter is required if the Mode parameter is set to Reserver.
        self.dbnode_group_count = dbnode_group_count
        # The storage capacity of the cluster. Unit: GB.
        # 
        # *   Valid values when DBClusterClass is set to C8: 100 to 1000
        # *   Valid values when DBClusterClass is set to C32: 100 to 8000
        # 
        # > * This parameter is required if the Mode parameter is set to Reserver.
        # > * 1000 The storage capacity less than 1,000 GB increases in 100 GB increments. The storage capacity greater than 1,000 GB increases in 1,000 GB increments.
        self.dbnode_storage = dbnode_storage
        # Indicates whether disk encryption is enabled. Valid values:
        # 
        # *   true
        # *   false
        self.disk_encryption = disk_encryption
        # The number of elastic I/O units (EIUs). For more information, see [Elasticity of the storage layer](https://help.aliyun.com/document_detail/189505.html).
        self.elastic_ioresource = elastic_ioresource
        # Specifies whether to enable SSL encryption. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.enable_ssl = enable_ssl
        # A reserved parameter.
        self.executor_count = executor_count
        # The Key Management Service (KMS) ID that is used for disk encryption. This parameter takes effect only when DiskEncryption is set to true.
        self.kms_id = kms_id
        # The mode of the cluster. Valid values:
        # 
        # *   **Reserver**: the reserved mode.
        # *   **Flexible**: the elastic mode.
        self.mode = mode
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The billing method of the cluster. Valid values:
        # 
        # *   **Postpaid**: pay-as-you-go
        # *   **Prepaid**: subscription
        # 
        # This parameter is required.
        self.pay_type = pay_type
        # The subscription type of the subscription cluster. Valid values:
        # 
        # *   **Year**: subscription on a yearly basis
        # *   **Month**: subscription on a monthly basis
        # 
        # >  This parameter is required if the PayType parameter is set to Prepaid.
        self.period = period
        # The region ID of the cluster.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/143074.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the cluster belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # A reserved parameter.
        self.restore_time = restore_time
        # A reserved parameter.
        self.restore_type = restore_type
        # A reserved parameter.
        self.source_dbinstance_name = source_dbinstance_name
        # A reserved parameter.
        self.storage_resource = storage_resource
        # A reserved parameter.
        self.storage_type = storage_type
        # The tags to add to the cluster.
        self.tag = tag
        # The subscription period of the subscription cluster.
        # 
        # *   Valid values when Period is set to Year: 1, 2, and 3 (integer)
        # *   Valid values when Period is set to Month: 1 to 9 (integer)
        # 
        # > * This parameter is required if the PayType parameter is set to Prepaid.
        # > * Longer subscription periods offer more savings. Purchasing a cluster for one year is more cost-effective than purchasing the cluster for 10 or 11 months.
        self.used_time = used_time
        # The virtual private cloud (VPC) ID of the cluster.
        self.vpcid = vpcid
        # The vSwitch ID of the cluster.
        self.v_switch_id = v_switch_id
        # The zone ID of the cluster.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/143074.html) operation to query the most recent zone list.
        self.zone_id = zone_id

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
        if self.backup_set_id is not None:
            result['BackupSetID'] = self.backup_set_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.compute_resource is not None:
            result['ComputeResource'] = self.compute_resource

        if self.dbcluster_category is not None:
            result['DBClusterCategory'] = self.dbcluster_category

        if self.dbcluster_class is not None:
            result['DBClusterClass'] = self.dbcluster_class

        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description

        if self.dbcluster_network_type is not None:
            result['DBClusterNetworkType'] = self.dbcluster_network_type

        if self.dbcluster_version is not None:
            result['DBClusterVersion'] = self.dbcluster_version

        if self.dbnode_group_count is not None:
            result['DBNodeGroupCount'] = self.dbnode_group_count

        if self.dbnode_storage is not None:
            result['DBNodeStorage'] = self.dbnode_storage

        if self.disk_encryption is not None:
            result['DiskEncryption'] = self.disk_encryption

        if self.elastic_ioresource is not None:
            result['ElasticIOResource'] = self.elastic_ioresource

        if self.enable_ssl is not None:
            result['EnableSSL'] = self.enable_ssl

        if self.executor_count is not None:
            result['ExecutorCount'] = self.executor_count

        if self.kms_id is not None:
            result['KmsId'] = self.kms_id

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.period is not None:
            result['Period'] = self.period

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.restore_time is not None:
            result['RestoreTime'] = self.restore_time

        if self.restore_type is not None:
            result['RestoreType'] = self.restore_type

        if self.source_dbinstance_name is not None:
            result['SourceDBInstanceName'] = self.source_dbinstance_name

        if self.storage_resource is not None:
            result['StorageResource'] = self.storage_resource

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.used_time is not None:
            result['UsedTime'] = self.used_time

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupSetID') is not None:
            self.backup_set_id = m.get('BackupSetID')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ComputeResource') is not None:
            self.compute_resource = m.get('ComputeResource')

        if m.get('DBClusterCategory') is not None:
            self.dbcluster_category = m.get('DBClusterCategory')

        if m.get('DBClusterClass') is not None:
            self.dbcluster_class = m.get('DBClusterClass')

        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')

        if m.get('DBClusterNetworkType') is not None:
            self.dbcluster_network_type = m.get('DBClusterNetworkType')

        if m.get('DBClusterVersion') is not None:
            self.dbcluster_version = m.get('DBClusterVersion')

        if m.get('DBNodeGroupCount') is not None:
            self.dbnode_group_count = m.get('DBNodeGroupCount')

        if m.get('DBNodeStorage') is not None:
            self.dbnode_storage = m.get('DBNodeStorage')

        if m.get('DiskEncryption') is not None:
            self.disk_encryption = m.get('DiskEncryption')

        if m.get('ElasticIOResource') is not None:
            self.elastic_ioresource = m.get('ElasticIOResource')

        if m.get('EnableSSL') is not None:
            self.enable_ssl = m.get('EnableSSL')

        if m.get('ExecutorCount') is not None:
            self.executor_count = m.get('ExecutorCount')

        if m.get('KmsId') is not None:
            self.kms_id = m.get('KmsId')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RestoreTime') is not None:
            self.restore_time = m.get('RestoreTime')

        if m.get('RestoreType') is not None:
            self.restore_type = m.get('RestoreType')

        if m.get('SourceDBInstanceName') is not None:
            self.source_dbinstance_name = m.get('SourceDBInstanceName')

        if m.get('StorageResource') is not None:
            self.storage_resource = m.get('StorageResource')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateDBClusterRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class CreateDBClusterRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N to add to the cluster. You can use tags to filter clusters. Valid values of N: 1 to 20. The values that you specify for N must be unique and consecutive integers that start from 1. Each value of `Tag.N.Key` is paired with a value of `Tag.N.Value`.
        # 
        # >  The tag key can be up to 64 characters in length and cannot start with `aliyun`, `acs:`, `http://`, or `https://`.
        self.key = key
        # The value of tag N to add to the cluster. You can use tags to filter clusters. Valid values of N: 1 to 20. The values that you specify for N must be unique and consecutive integers that start from 1. Each value of `Tag.N.Key` is paired with a value of `Tag.N.Value`.
        # 
        # >  The tag value can be up to 64 characters in length and cannot start with `aliyun`, `acs:`, `http://`, or `https://`.
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

