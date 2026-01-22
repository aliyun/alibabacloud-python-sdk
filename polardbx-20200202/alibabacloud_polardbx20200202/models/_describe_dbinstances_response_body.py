# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstancesResponseBody(DaraModel):
    def __init__(
        self,
        dbinstances: List[main_models.DescribeDBInstancesResponseBodyDBInstances] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_number: int = None,
    ):
        self.dbinstances = dbinstances
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_number = total_number

    def validate(self):
        if self.dbinstances:
            for v1 in self.dbinstances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBInstances'] = []
        if self.dbinstances is not None:
            for k1 in self.dbinstances:
                result['DBInstances'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_number is not None:
            result['TotalNumber'] = self.total_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbinstances = []
        if m.get('DBInstances') is not None:
            for k1 in m.get('DBInstances'):
                temp_model = main_models.DescribeDBInstancesResponseBodyDBInstances()
                self.dbinstances.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalNumber') is not None:
            self.total_number = m.get('TotalNumber')

        return self

class DescribeDBInstancesResponseBodyDBInstances(DaraModel):
    def __init__(
        self,
        cdc_instance_name: str = None,
        cn_node_class_code: str = None,
        cn_node_count: int = None,
        columnar_instance_name: str = None,
        columnar_read_dbinstances: List[str] = None,
        commodity_code: str = None,
        contain_binlog_x: bool = None,
        cpu_type: str = None,
        create_time: str = None,
        dbinstance_name: str = None,
        dbtype: str = None,
        dbversion: str = None,
        description: str = None,
        dn_node_class_code: str = None,
        dn_node_count: int = None,
        engine: str = None,
        engine_version: str = None,
        expire_time: str = None,
        expired: bool = None,
        id: str = None,
        lock_mode: str = None,
        lock_reason: str = None,
        minor_version: str = None,
        network: str = None,
        node_class: str = None,
        node_count: int = None,
        nodes: List[main_models.DescribeDBInstancesResponseBodyDBInstancesNodes] = None,
        pay_type: str = None,
        primary_instance_id: str = None,
        primary_zone: str = None,
        read_dbinstances: List[str] = None,
        region_id: str = None,
        resource_group_id: str = None,
        secondary_zone: str = None,
        series: str = None,
        status: str = None,
        storage_type: str = None,
        storage_used: int = None,
        support_binlog_x: bool = None,
        tag_set: List[main_models.DescribeDBInstancesResponseBodyDBInstancesTagSet] = None,
        tertiary_zone: str = None,
        topology_type: str = None,
        type: str = None,
        vpcid: str = None,
        zone_id: str = None,
        gdn_role: str = None,
        is_in_gdn: bool = None,
    ):
        self.cdc_instance_name = cdc_instance_name
        self.cn_node_class_code = cn_node_class_code
        self.cn_node_count = cn_node_count
        self.columnar_instance_name = columnar_instance_name
        self.columnar_read_dbinstances = columnar_read_dbinstances
        self.commodity_code = commodity_code
        self.contain_binlog_x = contain_binlog_x
        self.cpu_type = cpu_type
        self.create_time = create_time
        self.dbinstance_name = dbinstance_name
        self.dbtype = dbtype
        self.dbversion = dbversion
        self.description = description
        self.dn_node_class_code = dn_node_class_code
        self.dn_node_count = dn_node_count
        self.engine = engine
        self.engine_version = engine_version
        self.expire_time = expire_time
        self.expired = expired
        self.id = id
        self.lock_mode = lock_mode
        self.lock_reason = lock_reason
        self.minor_version = minor_version
        self.network = network
        self.node_class = node_class
        self.node_count = node_count
        self.nodes = nodes
        self.pay_type = pay_type
        self.primary_instance_id = primary_instance_id
        # 主可用区。
        # 
        # This parameter is required.
        self.primary_zone = primary_zone
        self.read_dbinstances = read_dbinstances
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        # 次可用区。
        self.secondary_zone = secondary_zone
        self.series = series
        self.status = status
        self.storage_type = storage_type
        self.storage_used = storage_used
        self.support_binlog_x = support_binlog_x
        self.tag_set = tag_set
        # 第三可用区。
        self.tertiary_zone = tertiary_zone
        # 拓扑类型：
        # 
        # - **3azones**：三可用区；
        # - **1azone**：单可用区。
        # 
        # This parameter is required.
        self.topology_type = topology_type
        self.type = type
        # VPC ID。
        self.vpcid = vpcid
        self.zone_id = zone_id
        self.gdn_role = gdn_role
        self.is_in_gdn = is_in_gdn

    def validate(self):
        if self.nodes:
            for v1 in self.nodes:
                 if v1:
                    v1.validate()
        if self.tag_set:
            for v1 in self.tag_set:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cdc_instance_name is not None:
            result['CdcInstanceName'] = self.cdc_instance_name

        if self.cn_node_class_code is not None:
            result['CnNodeClassCode'] = self.cn_node_class_code

        if self.cn_node_count is not None:
            result['CnNodeCount'] = self.cn_node_count

        if self.columnar_instance_name is not None:
            result['ColumnarInstanceName'] = self.columnar_instance_name

        if self.columnar_read_dbinstances is not None:
            result['ColumnarReadDBInstances'] = self.columnar_read_dbinstances

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.contain_binlog_x is not None:
            result['ContainBinlogX'] = self.contain_binlog_x

        if self.cpu_type is not None:
            result['CpuType'] = self.cpu_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.dbtype is not None:
            result['DBType'] = self.dbtype

        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion

        if self.description is not None:
            result['Description'] = self.description

        if self.dn_node_class_code is not None:
            result['DnNodeClassCode'] = self.dn_node_class_code

        if self.dn_node_count is not None:
            result['DnNodeCount'] = self.dn_node_count

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.expired is not None:
            result['Expired'] = self.expired

        if self.id is not None:
            result['Id'] = self.id

        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode

        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason

        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version

        if self.network is not None:
            result['Network'] = self.network

        if self.node_class is not None:
            result['NodeClass'] = self.node_class

        if self.node_count is not None:
            result['NodeCount'] = self.node_count

        result['Nodes'] = []
        if self.nodes is not None:
            for k1 in self.nodes:
                result['Nodes'].append(k1.to_map() if k1 else None)

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.primary_instance_id is not None:
            result['PrimaryInstanceId'] = self.primary_instance_id

        if self.primary_zone is not None:
            result['PrimaryZone'] = self.primary_zone

        if self.read_dbinstances is not None:
            result['ReadDBInstances'] = self.read_dbinstances

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.secondary_zone is not None:
            result['SecondaryZone'] = self.secondary_zone

        if self.series is not None:
            result['Series'] = self.series

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.storage_used is not None:
            result['StorageUsed'] = self.storage_used

        if self.support_binlog_x is not None:
            result['SupportBinlogX'] = self.support_binlog_x

        result['TagSet'] = []
        if self.tag_set is not None:
            for k1 in self.tag_set:
                result['TagSet'].append(k1.to_map() if k1 else None)

        if self.tertiary_zone is not None:
            result['TertiaryZone'] = self.tertiary_zone

        if self.topology_type is not None:
            result['TopologyType'] = self.topology_type

        if self.type is not None:
            result['Type'] = self.type

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        if self.gdn_role is not None:
            result['gdnRole'] = self.gdn_role

        if self.is_in_gdn is not None:
            result['isInGdn'] = self.is_in_gdn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdcInstanceName') is not None:
            self.cdc_instance_name = m.get('CdcInstanceName')

        if m.get('CnNodeClassCode') is not None:
            self.cn_node_class_code = m.get('CnNodeClassCode')

        if m.get('CnNodeCount') is not None:
            self.cn_node_count = m.get('CnNodeCount')

        if m.get('ColumnarInstanceName') is not None:
            self.columnar_instance_name = m.get('ColumnarInstanceName')

        if m.get('ColumnarReadDBInstances') is not None:
            self.columnar_read_dbinstances = m.get('ColumnarReadDBInstances')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('ContainBinlogX') is not None:
            self.contain_binlog_x = m.get('ContainBinlogX')

        if m.get('CpuType') is not None:
            self.cpu_type = m.get('CpuType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')

        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DnNodeClassCode') is not None:
            self.dn_node_class_code = m.get('DnNodeClassCode')

        if m.get('DnNodeCount') is not None:
            self.dn_node_count = m.get('DnNodeCount')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('Expired') is not None:
            self.expired = m.get('Expired')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')

        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')

        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')

        if m.get('Network') is not None:
            self.network = m.get('Network')

        if m.get('NodeClass') is not None:
            self.node_class = m.get('NodeClass')

        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')

        self.nodes = []
        if m.get('Nodes') is not None:
            for k1 in m.get('Nodes'):
                temp_model = main_models.DescribeDBInstancesResponseBodyDBInstancesNodes()
                self.nodes.append(temp_model.from_map(k1))

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('PrimaryInstanceId') is not None:
            self.primary_instance_id = m.get('PrimaryInstanceId')

        if m.get('PrimaryZone') is not None:
            self.primary_zone = m.get('PrimaryZone')

        if m.get('ReadDBInstances') is not None:
            self.read_dbinstances = m.get('ReadDBInstances')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecondaryZone') is not None:
            self.secondary_zone = m.get('SecondaryZone')

        if m.get('Series') is not None:
            self.series = m.get('Series')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('StorageUsed') is not None:
            self.storage_used = m.get('StorageUsed')

        if m.get('SupportBinlogX') is not None:
            self.support_binlog_x = m.get('SupportBinlogX')

        self.tag_set = []
        if m.get('TagSet') is not None:
            for k1 in m.get('TagSet'):
                temp_model = main_models.DescribeDBInstancesResponseBodyDBInstancesTagSet()
                self.tag_set.append(temp_model.from_map(k1))

        if m.get('TertiaryZone') is not None:
            self.tertiary_zone = m.get('TertiaryZone')

        if m.get('TopologyType') is not None:
            self.topology_type = m.get('TopologyType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        if m.get('gdnRole') is not None:
            self.gdn_role = m.get('gdnRole')

        if m.get('isInGdn') is not None:
            self.is_in_gdn = m.get('isInGdn')

        return self

class DescribeDBInstancesResponseBodyDBInstancesTagSet(DaraModel):
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

class DescribeDBInstancesResponseBodyDBInstancesNodes(DaraModel):
    def __init__(
        self,
        class_code: str = None,
        id: str = None,
        name: str = None,
        region_id: str = None,
        zone_id: str = None,
    ):
        self.class_code = class_code
        self.id = id
        self.name = name
        self.region_id = region_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.class_code is not None:
            result['ClassCode'] = self.class_code

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassCode') is not None:
            self.class_code = m.get('ClassCode')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

