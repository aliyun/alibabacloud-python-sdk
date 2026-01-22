# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstanceViaEndpointResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance: main_models.DescribeDBInstanceViaEndpointResponseBodyDBInstance = None,
        request_id: str = None,
    ):
        self.dbinstance = dbinstance
        self.request_id = request_id

    def validate(self):
        if self.dbinstance:
            self.dbinstance.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance is not None:
            result['DBInstance'] = self.dbinstance.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstance') is not None:
            temp_model = main_models.DescribeDBInstanceViaEndpointResponseBodyDBInstance()
            self.dbinstance = temp_model.from_map(m.get('DBInstance'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDBInstanceViaEndpointResponseBodyDBInstance(DaraModel):
    def __init__(
        self,
        cn_node_class_code: str = None,
        cn_node_count: int = None,
        commodity_code: str = None,
        conn_addrs: List[main_models.DescribeDBInstanceViaEndpointResponseBodyDBInstanceConnAddrs] = None,
        connection_string: str = None,
        create_time: str = None,
        dbinstance_type: str = None,
        dbnode_class: str = None,
        dbnode_count: int = None,
        dbnodes: List[main_models.DescribeDBInstanceViaEndpointResponseBodyDBInstanceDBNodes] = None,
        dbtype: str = None,
        dbversion: str = None,
        description: str = None,
        dn_node_class_code: str = None,
        dn_node_count: int = None,
        engine: str = None,
        expire_date: str = None,
        expired: str = None,
        id: str = None,
        kind_code: int = None,
        ltsversions: List[str] = None,
        latest_minor_version: str = None,
        lock_mode: str = None,
        maintain_end_time: str = None,
        maintain_start_time: str = None,
        minor_version: str = None,
        network: str = None,
        pay_type: str = None,
        port: str = None,
        read_dbinstances: List[str] = None,
        region_id: str = None,
        resource_group_id: str = None,
        rights_separation_enabled: bool = None,
        rights_separation_status: str = None,
        series: str = None,
        status: str = None,
        storage_used: int = None,
        tag_set: List[main_models.DescribeDBInstanceViaEndpointResponseBodyDBInstanceTagSet] = None,
        type: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        self.cn_node_class_code = cn_node_class_code
        self.cn_node_count = cn_node_count
        self.commodity_code = commodity_code
        self.conn_addrs = conn_addrs
        self.connection_string = connection_string
        self.create_time = create_time
        self.dbinstance_type = dbinstance_type
        self.dbnode_class = dbnode_class
        self.dbnode_count = dbnode_count
        self.dbnodes = dbnodes
        self.dbtype = dbtype
        self.dbversion = dbversion
        self.description = description
        self.dn_node_class_code = dn_node_class_code
        self.dn_node_count = dn_node_count
        self.engine = engine
        self.expire_date = expire_date
        self.expired = expired
        self.id = id
        self.kind_code = kind_code
        # This parameter is required.
        self.ltsversions = ltsversions
        self.latest_minor_version = latest_minor_version
        self.lock_mode = lock_mode
        self.maintain_end_time = maintain_end_time
        self.maintain_start_time = maintain_start_time
        self.minor_version = minor_version
        self.network = network
        self.pay_type = pay_type
        self.port = port
        self.read_dbinstances = read_dbinstances
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.rights_separation_enabled = rights_separation_enabled
        self.rights_separation_status = rights_separation_status
        self.series = series
        self.status = status
        self.storage_used = storage_used
        self.tag_set = tag_set
        self.type = type
        # VPC ID。
        self.vpcid = vpcid
        self.v_switch_id = v_switch_id
        self.zone_id = zone_id

    def validate(self):
        if self.conn_addrs:
            for v1 in self.conn_addrs:
                 if v1:
                    v1.validate()
        if self.dbnodes:
            for v1 in self.dbnodes:
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
        if self.cn_node_class_code is not None:
            result['CnNodeClassCode'] = self.cn_node_class_code

        if self.cn_node_count is not None:
            result['CnNodeCount'] = self.cn_node_count

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        result['ConnAddrs'] = []
        if self.conn_addrs is not None:
            for k1 in self.conn_addrs:
                result['ConnAddrs'].append(k1.to_map() if k1 else None)

        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dbinstance_type is not None:
            result['DBInstanceType'] = self.dbinstance_type

        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class

        if self.dbnode_count is not None:
            result['DBNodeCount'] = self.dbnode_count

        result['DBNodes'] = []
        if self.dbnodes is not None:
            for k1 in self.dbnodes:
                result['DBNodes'].append(k1.to_map() if k1 else None)

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

        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date

        if self.expired is not None:
            result['Expired'] = self.expired

        if self.id is not None:
            result['Id'] = self.id

        if self.kind_code is not None:
            result['KindCode'] = self.kind_code

        if self.ltsversions is not None:
            result['LTSVersions'] = self.ltsversions

        if self.latest_minor_version is not None:
            result['LatestMinorVersion'] = self.latest_minor_version

        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode

        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time

        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time

        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version

        if self.network is not None:
            result['Network'] = self.network

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.port is not None:
            result['Port'] = self.port

        if self.read_dbinstances is not None:
            result['ReadDBInstances'] = self.read_dbinstances

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.rights_separation_enabled is not None:
            result['RightsSeparationEnabled'] = self.rights_separation_enabled

        if self.rights_separation_status is not None:
            result['RightsSeparationStatus'] = self.rights_separation_status

        if self.series is not None:
            result['Series'] = self.series

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_used is not None:
            result['StorageUsed'] = self.storage_used

        result['TagSet'] = []
        if self.tag_set is not None:
            for k1 in self.tag_set:
                result['TagSet'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CnNodeClassCode') is not None:
            self.cn_node_class_code = m.get('CnNodeClassCode')

        if m.get('CnNodeCount') is not None:
            self.cn_node_count = m.get('CnNodeCount')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        self.conn_addrs = []
        if m.get('ConnAddrs') is not None:
            for k1 in m.get('ConnAddrs'):
                temp_model = main_models.DescribeDBInstanceViaEndpointResponseBodyDBInstanceConnAddrs()
                self.conn_addrs.append(temp_model.from_map(k1))

        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DBInstanceType') is not None:
            self.dbinstance_type = m.get('DBInstanceType')

        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')

        if m.get('DBNodeCount') is not None:
            self.dbnode_count = m.get('DBNodeCount')

        self.dbnodes = []
        if m.get('DBNodes') is not None:
            for k1 in m.get('DBNodes'):
                temp_model = main_models.DescribeDBInstanceViaEndpointResponseBodyDBInstanceDBNodes()
                self.dbnodes.append(temp_model.from_map(k1))

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

        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')

        if m.get('Expired') is not None:
            self.expired = m.get('Expired')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('KindCode') is not None:
            self.kind_code = m.get('KindCode')

        if m.get('LTSVersions') is not None:
            self.ltsversions = m.get('LTSVersions')

        if m.get('LatestMinorVersion') is not None:
            self.latest_minor_version = m.get('LatestMinorVersion')

        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')

        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')

        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')

        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')

        if m.get('Network') is not None:
            self.network = m.get('Network')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('ReadDBInstances') is not None:
            self.read_dbinstances = m.get('ReadDBInstances')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RightsSeparationEnabled') is not None:
            self.rights_separation_enabled = m.get('RightsSeparationEnabled')

        if m.get('RightsSeparationStatus') is not None:
            self.rights_separation_status = m.get('RightsSeparationStatus')

        if m.get('Series') is not None:
            self.series = m.get('Series')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageUsed') is not None:
            self.storage_used = m.get('StorageUsed')

        self.tag_set = []
        if m.get('TagSet') is not None:
            for k1 in m.get('TagSet'):
                temp_model = main_models.DescribeDBInstanceViaEndpointResponseBodyDBInstanceTagSet()
                self.tag_set.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeDBInstanceViaEndpointResponseBodyDBInstanceTagSet(DaraModel):
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

class DescribeDBInstanceViaEndpointResponseBodyDBInstanceDBNodes(DaraModel):
    def __init__(
        self,
        compute_node_id: str = None,
        data_node_id: str = None,
        id: str = None,
        node_class: str = None,
        region_id: str = None,
        zone_id: str = None,
    ):
        self.compute_node_id = compute_node_id
        self.data_node_id = data_node_id
        self.id = id
        self.node_class = node_class
        self.region_id = region_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compute_node_id is not None:
            result['ComputeNodeId'] = self.compute_node_id

        if self.data_node_id is not None:
            result['DataNodeId'] = self.data_node_id

        if self.id is not None:
            result['Id'] = self.id

        if self.node_class is not None:
            result['NodeClass'] = self.node_class

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputeNodeId') is not None:
            self.compute_node_id = m.get('ComputeNodeId')

        if m.get('DataNodeId') is not None:
            self.data_node_id = m.get('DataNodeId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('NodeClass') is not None:
            self.node_class = m.get('NodeClass')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeDBInstanceViaEndpointResponseBodyDBInstanceConnAddrs(DaraModel):
    def __init__(
        self,
        connection_string: str = None,
        port: int = None,
        type: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        vpc_instance_id: str = None,
    ):
        self.connection_string = connection_string
        self.port = port
        self.type = type
        # VPC ID。
        self.vpcid = vpcid
        self.v_switch_id = v_switch_id
        self.vpc_instance_id = vpc_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.port is not None:
            result['Port'] = self.port

        if self.type is not None:
            result['Type'] = self.type

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_instance_id is not None:
            result['VpcInstanceId'] = self.vpc_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcInstanceId') is not None:
            self.vpc_instance_id = m.get('VpcInstanceId')

        return self

