# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20190315 import models as main_models
from darabonba.model import DaraModel

class DescribeDBClusterAttributeResponseBody(DaraModel):
    def __init__(
        self,
        items: main_models.DescribeDBClusterAttributeResponseBodyItems = None,
        request_id: str = None,
    ):
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
        category: str = None,
        commodity_code: str = None,
        compute_resource: str = None,
        connection_string: str = None,
        creation_time: str = None,
        dbcluster_description: str = None,
        dbcluster_id: str = None,
        dbcluster_network_type: str = None,
        dbcluster_status: str = None,
        dbcluster_type: str = None,
        dbnode_class: str = None,
        dbnode_count: int = None,
        dbnode_storage: int = None,
        dbversion: str = None,
        disk_encryption: bool = None,
        disk_performance_level: str = None,
        disk_type: str = None,
        dts_job_id: str = None,
        elastic_ioresource: int = None,
        elastic_ioresource_size: str = None,
        enable_airflow: bool = None,
        enable_spark: bool = None,
        engine: str = None,
        engine_version: str = None,
        executor_count: str = None,
        expire_time: str = None,
        expired: str = None,
        inner_ip: str = None,
        inner_port: str = None,
        kms_id: str = None,
        lock_mode: str = None,
        lock_reason: str = None,
        maintain_time: str = None,
        mode: str = None,
        pay_type: str = None,
        port: int = None,
        product_form: str = None,
        product_version: str = None,
        rds_instance_id: str = None,
        region_id: str = None,
        reserved_node_count: int = None,
        reserved_node_size: str = None,
        resource_group_id: str = None,
        secondary_vswitch_id: str = None,
        secondary_zone_id: str = None,
        storage_resource: str = None,
        tags: main_models.DescribeDBClusterAttributeResponseBodyItemsDBClusterTags = None,
        task_info: main_models.DescribeDBClusterAttributeResponseBodyItemsDBClusterTaskInfo = None,
        user_enistatus: bool = None,
        vpccloud_instance_id: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        self.category = category
        self.commodity_code = commodity_code
        self.compute_resource = compute_resource
        self.connection_string = connection_string
        self.creation_time = creation_time
        self.dbcluster_description = dbcluster_description
        self.dbcluster_id = dbcluster_id
        self.dbcluster_network_type = dbcluster_network_type
        self.dbcluster_status = dbcluster_status
        self.dbcluster_type = dbcluster_type
        self.dbnode_class = dbnode_class
        self.dbnode_count = dbnode_count
        self.dbnode_storage = dbnode_storage
        self.dbversion = dbversion
        self.disk_encryption = disk_encryption
        self.disk_performance_level = disk_performance_level
        self.disk_type = disk_type
        self.dts_job_id = dts_job_id
        self.elastic_ioresource = elastic_ioresource
        self.elastic_ioresource_size = elastic_ioresource_size
        self.enable_airflow = enable_airflow
        self.enable_spark = enable_spark
        self.engine = engine
        self.engine_version = engine_version
        self.executor_count = executor_count
        self.expire_time = expire_time
        self.expired = expired
        self.inner_ip = inner_ip
        self.inner_port = inner_port
        self.kms_id = kms_id
        self.lock_mode = lock_mode
        self.lock_reason = lock_reason
        self.maintain_time = maintain_time
        self.mode = mode
        self.pay_type = pay_type
        self.port = port
        self.product_form = product_form
        self.product_version = product_version
        self.rds_instance_id = rds_instance_id
        self.region_id = region_id
        self.reserved_node_count = reserved_node_count
        self.reserved_node_size = reserved_node_size
        self.resource_group_id = resource_group_id
        self.secondary_vswitch_id = secondary_vswitch_id
        self.secondary_zone_id = secondary_zone_id
        self.storage_resource = storage_resource
        self.tags = tags
        self.task_info = task_info
        self.user_enistatus = user_enistatus
        self.vpccloud_instance_id = vpccloud_instance_id
        self.vpcid = vpcid
        self.v_switch_id = v_switch_id
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
        if self.category is not None:
            result['Category'] = self.category

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.compute_resource is not None:
            result['ComputeResource'] = self.compute_resource

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

        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class

        if self.dbnode_count is not None:
            result['DBNodeCount'] = self.dbnode_count

        if self.dbnode_storage is not None:
            result['DBNodeStorage'] = self.dbnode_storage

        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion

        if self.disk_encryption is not None:
            result['DiskEncryption'] = self.disk_encryption

        if self.disk_performance_level is not None:
            result['DiskPerformanceLevel'] = self.disk_performance_level

        if self.disk_type is not None:
            result['DiskType'] = self.disk_type

        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id

        if self.elastic_ioresource is not None:
            result['ElasticIOResource'] = self.elastic_ioresource

        if self.elastic_ioresource_size is not None:
            result['ElasticIOResourceSize'] = self.elastic_ioresource_size

        if self.enable_airflow is not None:
            result['EnableAirflow'] = self.enable_airflow

        if self.enable_spark is not None:
            result['EnableSpark'] = self.enable_spark

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.executor_count is not None:
            result['ExecutorCount'] = self.executor_count

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.expired is not None:
            result['Expired'] = self.expired

        if self.inner_ip is not None:
            result['InnerIp'] = self.inner_ip

        if self.inner_port is not None:
            result['InnerPort'] = self.inner_port

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

        if self.rds_instance_id is not None:
            result['RdsInstanceId'] = self.rds_instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

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

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.task_info is not None:
            result['TaskInfo'] = self.task_info.to_map()

        if self.user_enistatus is not None:
            result['UserENIStatus'] = self.user_enistatus

        if self.vpccloud_instance_id is not None:
            result['VPCCloudInstanceId'] = self.vpccloud_instance_id

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('ComputeResource') is not None:
            self.compute_resource = m.get('ComputeResource')

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

        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')

        if m.get('DBNodeCount') is not None:
            self.dbnode_count = m.get('DBNodeCount')

        if m.get('DBNodeStorage') is not None:
            self.dbnode_storage = m.get('DBNodeStorage')

        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')

        if m.get('DiskEncryption') is not None:
            self.disk_encryption = m.get('DiskEncryption')

        if m.get('DiskPerformanceLevel') is not None:
            self.disk_performance_level = m.get('DiskPerformanceLevel')

        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')

        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')

        if m.get('ElasticIOResource') is not None:
            self.elastic_ioresource = m.get('ElasticIOResource')

        if m.get('ElasticIOResourceSize') is not None:
            self.elastic_ioresource_size = m.get('ElasticIOResourceSize')

        if m.get('EnableAirflow') is not None:
            self.enable_airflow = m.get('EnableAirflow')

        if m.get('EnableSpark') is not None:
            self.enable_spark = m.get('EnableSpark')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('ExecutorCount') is not None:
            self.executor_count = m.get('ExecutorCount')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('Expired') is not None:
            self.expired = m.get('Expired')

        if m.get('InnerIp') is not None:
            self.inner_ip = m.get('InnerIp')

        if m.get('InnerPort') is not None:
            self.inner_port = m.get('InnerPort')

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

        if m.get('RdsInstanceId') is not None:
            self.rds_instance_id = m.get('RdsInstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

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

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeDBClusterAttributeResponseBodyItemsDBClusterTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('TaskInfo') is not None:
            temp_model = main_models.DescribeDBClusterAttributeResponseBodyItemsDBClusterTaskInfo()
            self.task_info = temp_model.from_map(m.get('TaskInfo'))

        if m.get('UserENIStatus') is not None:
            self.user_enistatus = m.get('UserENIStatus')

        if m.get('VPCCloudInstanceId') is not None:
            self.vpccloud_instance_id = m.get('VPCCloudInstanceId')

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
        self.name = name
        self.progress = progress
        self.status = status
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
        self.end_time = end_time
        self.start_time = start_time
        self.step_desc = step_desc
        self.step_name = step_name
        self.step_progress = step_progress
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

