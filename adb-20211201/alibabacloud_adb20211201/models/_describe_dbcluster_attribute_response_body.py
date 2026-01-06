# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeDBClusterAttributeResponseBody(DaraModel):
    def __init__(
        self,
        items: main_models.DescribeDBClusterAttributeResponseBodyItems = None,
        request_id: str = None,
    ):
        # The queried cluster.
        self.items = items
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = main_models.DescribeDBClusterAttributeResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDBClusterAttributeResponseBodyItems(DaraModel):
    def __init__(
        self,
        dbcluster: List[main_models.DescribeDBClusterAttributeResponseBodyItemsDBCluster] = None,
    ):
        self.dbcluster = dbcluster

    def validate(self):
        if self.dbcluster:
            for v1 in self.dbcluster:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBCluster'] = []
        if self.dbcluster is not None:
            for k1 in self.dbcluster:
                result['DBCluster'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbcluster = []
        if m.get('DBCluster') is not None:
            for k1 in m.get('DBCluster'):
                temp_model = main_models.DescribeDBClusterAttributeResponseBodyItemsDBCluster()
                self.dbcluster.append(temp_model.from_map(k1))

        return self

class DescribeDBClusterAttributeResponseBodyItemsDBCluster(DaraModel):
    def __init__(
        self,
        ainode_number: int = None,
        ainode_spec: str = None,
        clickhouse_engine_cache_size: int = None,
        clickhouse_engine_enabled: bool = None,
        commodity_code: str = None,
        compute_resource: str = None,
        compute_resource_total: str = None,
        connection_string: str = None,
        creation_time: str = None,
        dbcluster_description: str = None,
        dbcluster_id: str = None,
        dbcluster_network_type: str = None,
        dbcluster_status: str = None,
        dbcluster_type: str = None,
        dbversion: str = None,
        disk_encryption: bool = None,
        engine: str = None,
        engine_version: str = None,
        expire_time: str = None,
        expired: str = None,
        kms_id: str = None,
        lock_mode: str = None,
        lock_reason: str = None,
        maintain_time: str = None,
        mode: str = None,
        pay_type: str = None,
        port: int = None,
        product_form: str = None,
        product_version: str = None,
        region_id: str = None,
        reserved_acu: str = None,
        reserved_node_count: int = None,
        reserved_node_size: str = None,
        resource_group_id: str = None,
        secondary_vswitch_id: str = None,
        secondary_zone_id: str = None,
        storage_resource: str = None,
        storage_resource_total: str = None,
        supported_features: Dict[str, str] = None,
        tags: main_models.DescribeDBClusterAttributeResponseBodyItemsDBClusterTags = None,
        task_info: main_models.DescribeDBClusterAttributeResponseBodyItemsDBClusterTaskInfo = None,
        user_enistatus: bool = None,
        user_enivswitch_options: str = None,
        user_enivpc_id: str = None,
        user_enizone_options: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        self.ainode_number = ainode_number
        self.ainode_spec = ainode_spec
        # The cache size of the ClickHouse wide table engine. Unit: GB. If a value of -1 is returned, the ClickHouse wide table engine is disabled. If a value other than -1 is returned, this parameter indicates the disk cache size.
        self.clickhouse_engine_cache_size = clickhouse_engine_cache_size
        # Indicates whether the ClickHouse wide table engine is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.clickhouse_engine_enabled = clickhouse_engine_enabled
        # The billing method of the cluster. Valid values:
        # 
        # *   **ads**: pay-as-you-go.
        # *   **ads_pre**: subscription.
        self.commodity_code = commodity_code
        # The specifications of reserved computing resources. Each ACU is approximately equal to 1 core and 4 GB memory. Computing resources are used to compute data. The increase in the computing resources can accelerate queries. You can scale computing resources based on your business requirements.
        self.compute_resource = compute_resource
        # The total amount of computing resources in the cluster. Each ACU is approximately equal to 1 core and 4 GB memory.
        self.compute_resource_total = compute_resource_total
        # The public endpoint that is used to connect to the cluster.
        self.connection_string = connection_string
        # The time when the cluster was created. The time follows the ISO 8601 standard in the `YYYY-MM-DDThh:mm:ssZ` format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The description of the cluster.
        self.dbcluster_description = dbcluster_description
        # The ID of the AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        self.dbcluster_id = dbcluster_id
        # The network type of the cluster. **VPC** is returned.
        self.dbcluster_network_type = dbcluster_network_type
        # The status of the cluster. Valid values:
        # 
        # *   **Preparing**
        # *   **Creating**
        # *   **Running**
        # *   **Deleting**
        # *   **Restoring**
        # *   **ClassChanging**
        # *   **NetAddressCreating**
        # *   **NetAddressDeleting**
        # *   **NetAddressModifying**
        self.dbcluster_status = dbcluster_status
        # The type of the cluster. By default, **Common** is returned, which indicates a common cluster.
        self.dbcluster_type = dbcluster_type
        # The engine version of the AnalyticDB for MySQL Data Lakehouse Edition cluster. **5.0** is returned.
        self.dbversion = dbversion
        self.disk_encryption = disk_encryption
        # The engine of the cluster. **AnalyticDB** is returned.
        self.engine = engine
        # The minor version of the cluster.
        self.engine_version = engine_version
        # The time when the cluster expires.
        # 
        # *   If the billing method of the cluster is subscription, the actual expiration time is returned.
        # *   If the billing method of the cluster is pay-as-you-go, null is returned.
        self.expire_time = expire_time
        # Indicates whether the subscription cluster has expired. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # > 
        # 
        # *   If the cluster has expired, the system locks or releases the cluster within a period of time. We recommend that you renew the expired cluster. For more information, see [Renewal policy](https://help.aliyun.com/document_detail/135248.html).
        # 
        # *   This parameter is not returned for pay-as-you-go clusters.
        self.expired = expired
        # The ID of the key that is used to encrypt disk data.
        # 
        # >  This parameter is returned only when disk encryption is enabled.
        self.kms_id = kms_id
        # The lock mode of the cluster. Valid values:
        # 
        # *   **Unlock**: The cluster is not locked.
        # *   **ManualLock**: The cluster is manually locked.
        # *   **LockByExpiration**: The cluster is automatically locked due to cluster expiration.
        self.lock_mode = lock_mode
        # The reason why the cluster is locked.
        # 
        # >  This parameter is returned only when the cluster was locked. **instance_expire** is returned.
        self.lock_reason = lock_reason
        # The maintenance window of the cluster. The time is displayed in the `HH:mmZ-HH:mmZ` format in UTC.
        # 
        # >  For more information about maintenance windows, see [Configure a maintenance window](https://help.aliyun.com/document_detail/122569.html).
        self.maintain_time = maintain_time
        # The mode of the cluster. By default, **flexible** is returned, which indicates that the cluster is in elastic mode.
        self.mode = mode
        # The billing method of the cluster. Valid values:
        # 
        # *   **Postpaid**: pay-as-you-go.
        # *   **Prepaid**: subscription.
        self.pay_type = pay_type
        # The port number that is used to connect to the cluster.
        self.port = port
        # A reserved parameter.
        self.product_form = product_form
        # The edition of the cluster. Valid values:
        # 
        # *   **BasicVersion**: Basic Edition.
        # *   **EnterpriseVersion**: Enterprise Edition.
        self.product_version = product_version
        # The region ID of the cluster.
        self.region_id = region_id
        # The amount of remaining reserved computing resources that are available in the cluster. Each ACU is approximately equal to 1 core and 4 GB memory.
        self.reserved_acu = reserved_acu
        # A reserved parameter.
        self.reserved_node_count = reserved_node_count
        # A reserved parameter.
        self.reserved_node_size = reserved_node_size
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.secondary_vswitch_id = secondary_vswitch_id
        self.secondary_zone_id = secondary_zone_id
        # The specifications of reserved storage resources. Each AnalyticDB compute unit (ACU) is approximately equal to 1 core and 4 GB memory. Storage resources are used to read and write data. The increase in the storage resources can improve the read and write performance of the cluster.
        self.storage_resource = storage_resource
        # The total amount of storage resources in the cluster. Each ACU is approximately equal to 1 core and 4 GB memory.
        self.storage_resource_total = storage_resource_total
        # Reserved parameters.
        self.supported_features = supported_features
        # The tags that are added to the cluster.
        self.tags = tags
        # The job information.
        self.task_info = task_info
        # Indicates whether Elastic Network Interface (ENI) is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.user_enistatus = user_enistatus
        # The vSwitch connected to the ENI. Separate multiple vSwitches with commas (,).
        self.user_enivswitch_options = user_enivswitch_options
        # The VPC information of the ENI.
        self.user_enivpc_id = user_enivpc_id
        # The zone associated with the ENI. Separate multiple zones with commas (,).
        self.user_enizone_options = user_enizone_options
        # The virtual private cloud (VPC) ID of the cluster.
        self.vpcid = vpcid
        # The vSwitch ID of the cluster.
        self.v_switch_id = v_switch_id
        # The zone ID of the cluster.
        self.zone_id = zone_id

    def validate(self):
        if self.tags:
            self.tags.validate()
        if self.task_info:
            self.task_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ainode_number is not None:
            result['AINodeNumber'] = self.ainode_number

        if self.ainode_spec is not None:
            result['AINodeSpec'] = self.ainode_spec

        if self.clickhouse_engine_cache_size is not None:
            result['ClickhouseEngineCacheSize'] = self.clickhouse_engine_cache_size

        if self.clickhouse_engine_enabled is not None:
            result['ClickhouseEngineEnabled'] = self.clickhouse_engine_enabled

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.compute_resource is not None:
            result['ComputeResource'] = self.compute_resource

        if self.compute_resource_total is not None:
            result['ComputeResourceTotal'] = self.compute_resource_total

        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbcluster_network_type is not None:
            result['DBClusterNetworkType'] = self.dbcluster_network_type

        if self.dbcluster_status is not None:
            result['DBClusterStatus'] = self.dbcluster_status

        if self.dbcluster_type is not None:
            result['DBClusterType'] = self.dbcluster_type

        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion

        if self.disk_encryption is not None:
            result['DiskEncryption'] = self.disk_encryption

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.expired is not None:
            result['Expired'] = self.expired

        if self.kms_id is not None:
            result['KmsId'] = self.kms_id

        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode

        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason

        if self.maintain_time is not None:
            result['MaintainTime'] = self.maintain_time

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.port is not None:
            result['Port'] = self.port

        if self.product_form is not None:
            result['ProductForm'] = self.product_form

        if self.product_version is not None:
            result['ProductVersion'] = self.product_version

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.reserved_acu is not None:
            result['ReservedACU'] = self.reserved_acu

        if self.reserved_node_count is not None:
            result['ReservedNodeCount'] = self.reserved_node_count

        if self.reserved_node_size is not None:
            result['ReservedNodeSize'] = self.reserved_node_size

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.secondary_vswitch_id is not None:
            result['SecondaryVSwitchId'] = self.secondary_vswitch_id

        if self.secondary_zone_id is not None:
            result['SecondaryZoneId'] = self.secondary_zone_id

        if self.storage_resource is not None:
            result['StorageResource'] = self.storage_resource

        if self.storage_resource_total is not None:
            result['StorageResourceTotal'] = self.storage_resource_total

        if self.supported_features is not None:
            result['SupportedFeatures'] = self.supported_features

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.task_info is not None:
            result['TaskInfo'] = self.task_info.to_map()

        if self.user_enistatus is not None:
            result['UserENIStatus'] = self.user_enistatus

        if self.user_enivswitch_options is not None:
            result['UserENIVSwitchOptions'] = self.user_enivswitch_options

        if self.user_enivpc_id is not None:
            result['UserENIVpcId'] = self.user_enivpc_id

        if self.user_enizone_options is not None:
            result['UserENIZoneOptions'] = self.user_enizone_options

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AINodeNumber') is not None:
            self.ainode_number = m.get('AINodeNumber')

        if m.get('AINodeSpec') is not None:
            self.ainode_spec = m.get('AINodeSpec')

        if m.get('ClickhouseEngineCacheSize') is not None:
            self.clickhouse_engine_cache_size = m.get('ClickhouseEngineCacheSize')

        if m.get('ClickhouseEngineEnabled') is not None:
            self.clickhouse_engine_enabled = m.get('ClickhouseEngineEnabled')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('ComputeResource') is not None:
            self.compute_resource = m.get('ComputeResource')

        if m.get('ComputeResourceTotal') is not None:
            self.compute_resource_total = m.get('ComputeResourceTotal')

        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBClusterNetworkType') is not None:
            self.dbcluster_network_type = m.get('DBClusterNetworkType')

        if m.get('DBClusterStatus') is not None:
            self.dbcluster_status = m.get('DBClusterStatus')

        if m.get('DBClusterType') is not None:
            self.dbcluster_type = m.get('DBClusterType')

        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')

        if m.get('DiskEncryption') is not None:
            self.disk_encryption = m.get('DiskEncryption')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('Expired') is not None:
            self.expired = m.get('Expired')

        if m.get('KmsId') is not None:
            self.kms_id = m.get('KmsId')

        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')

        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')

        if m.get('MaintainTime') is not None:
            self.maintain_time = m.get('MaintainTime')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('ProductForm') is not None:
            self.product_form = m.get('ProductForm')

        if m.get('ProductVersion') is not None:
            self.product_version = m.get('ProductVersion')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReservedACU') is not None:
            self.reserved_acu = m.get('ReservedACU')

        if m.get('ReservedNodeCount') is not None:
            self.reserved_node_count = m.get('ReservedNodeCount')

        if m.get('ReservedNodeSize') is not None:
            self.reserved_node_size = m.get('ReservedNodeSize')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecondaryVSwitchId') is not None:
            self.secondary_vswitch_id = m.get('SecondaryVSwitchId')

        if m.get('SecondaryZoneId') is not None:
            self.secondary_zone_id = m.get('SecondaryZoneId')

        if m.get('StorageResource') is not None:
            self.storage_resource = m.get('StorageResource')

        if m.get('StorageResourceTotal') is not None:
            self.storage_resource_total = m.get('StorageResourceTotal')

        if m.get('SupportedFeatures') is not None:
            self.supported_features = m.get('SupportedFeatures')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeDBClusterAttributeResponseBodyItemsDBClusterTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('TaskInfo') is not None:
            temp_model = main_models.DescribeDBClusterAttributeResponseBodyItemsDBClusterTaskInfo()
            self.task_info = temp_model.from_map(m.get('TaskInfo'))

        if m.get('UserENIStatus') is not None:
            self.user_enistatus = m.get('UserENIStatus')

        if m.get('UserENIVSwitchOptions') is not None:
            self.user_enivswitch_options = m.get('UserENIVSwitchOptions')

        if m.get('UserENIVpcId') is not None:
            self.user_enivpc_id = m.get('UserENIVpcId')

        if m.get('UserENIZoneOptions') is not None:
            self.user_enizone_options = m.get('UserENIZoneOptions')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeDBClusterAttributeResponseBodyItemsDBClusterTaskInfo(DaraModel):
    def __init__(
        self,
        name: str = None,
        progress: str = None,
        status: str = None,
        step_list: main_models.DescribeDBClusterAttributeResponseBodyItemsDBClusterTaskInfoStepList = None,
    ):
        # The name of the job.
        self.name = name
        # The progress of the job. Unit: %.
        self.progress = progress
        # The status of the job. Valid values:
        # 
        # *   NOT_RUN
        # *   RUNNING
        # *   SUCCEED
        self.status = status
        # The job steps.
        self.step_list = step_list

    def validate(self):
        if self.step_list:
            self.step_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.status is not None:
            result['Status'] = self.status

        if self.step_list is not None:
            result['StepList'] = self.step_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StepList') is not None:
            temp_model = main_models.DescribeDBClusterAttributeResponseBodyItemsDBClusterTaskInfoStepList()
            self.step_list = temp_model.from_map(m.get('StepList'))

        return self

class DescribeDBClusterAttributeResponseBodyItemsDBClusterTaskInfoStepList(DaraModel):
    def __init__(
        self,
        step_list: List[main_models.DescribeDBClusterAttributeResponseBodyItemsDBClusterTaskInfoStepListStepList] = None,
    ):
        self.step_list = step_list

    def validate(self):
        if self.step_list:
            for v1 in self.step_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['StepList'] = []
        if self.step_list is not None:
            for k1 in self.step_list:
                result['StepList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.step_list = []
        if m.get('StepList') is not None:
            for k1 in m.get('StepList'):
                temp_model = main_models.DescribeDBClusterAttributeResponseBodyItemsDBClusterTaskInfoStepListStepList()
                self.step_list.append(temp_model.from_map(k1))

        return self

class DescribeDBClusterAttributeResponseBodyItemsDBClusterTaskInfoStepListStepList(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        step_desc: str = None,
        step_name: str = None,
        step_progress: str = None,
        step_status: str = None,
    ):
        # The end time of the job step. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.end_time = end_time
        # The start time of the job step. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.start_time = start_time
        # The description of the job step.
        self.step_desc = step_desc
        # The name of the job step.
        self.step_name = step_name
        # The progress of the job step. Unit: %.
        self.step_progress = step_progress
        # The status of the job step. Valid values:
        # 
        # *   NOT_RUN
        # *   RUNNING
        # *   SUCCEED
        self.step_status = step_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.step_desc is not None:
            result['StepDesc'] = self.step_desc

        if self.step_name is not None:
            result['StepName'] = self.step_name

        if self.step_progress is not None:
            result['StepProgress'] = self.step_progress

        if self.step_status is not None:
            result['StepStatus'] = self.step_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StepDesc') is not None:
            self.step_desc = m.get('StepDesc')

        if m.get('StepName') is not None:
            self.step_name = m.get('StepName')

        if m.get('StepProgress') is not None:
            self.step_progress = m.get('StepProgress')

        if m.get('StepStatus') is not None:
            self.step_status = m.get('StepStatus')

        return self

class DescribeDBClusterAttributeResponseBodyItemsDBClusterTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeDBClusterAttributeResponseBodyItemsDBClusterTagsTag] = None,
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
                temp_model = main_models.DescribeDBClusterAttributeResponseBodyItemsDBClusterTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeDBClusterAttributeResponseBodyItemsDBClusterTagsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        # 
        # >  You can call the [TagResources](https://help.aliyun.com/document_detail/179253.html) operation to add tags to a cluster.
        self.key = key
        # The tag value.
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

