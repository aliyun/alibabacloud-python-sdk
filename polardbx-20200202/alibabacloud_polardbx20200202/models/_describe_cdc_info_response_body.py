# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeCdcInfoResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeCdcInfoResponseBodyData = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        # This parameter is required.
        self.http_status_code = http_status_code
        # Id of the request
        self.request_id = request_id
        # This parameter is required.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeCdcInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeCdcInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        binlog_persist_time: int = None,
        binlog_size: int = None,
        cdc_new_version: str = None,
        check_sum_switch: str = None,
        enable_cyclic_replication: bool = None,
        instance_topology_list: List[main_models.DescribeCdcInfoResponseBodyDataInstanceTopologyList] = None,
        server_id: int = None,
        version_support_multi_cdc: bool = None,
    ):
        self.binlog_persist_time = binlog_persist_time
        # This parameter is required.
        self.binlog_size = binlog_size
        # This parameter is required.
        self.cdc_new_version = cdc_new_version
        self.check_sum_switch = check_sum_switch
        self.enable_cyclic_replication = enable_cyclic_replication
        self.instance_topology_list = instance_topology_list
        # server id
        # 
        # This parameter is required.
        self.server_id = server_id
        self.version_support_multi_cdc = version_support_multi_cdc

    def validate(self):
        if self.instance_topology_list:
            for v1 in self.instance_topology_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.binlog_persist_time is not None:
            result['BinlogPersistTime'] = self.binlog_persist_time

        if self.binlog_size is not None:
            result['BinlogSize'] = self.binlog_size

        if self.cdc_new_version is not None:
            result['CdcNewVersion'] = self.cdc_new_version

        if self.check_sum_switch is not None:
            result['CheckSumSwitch'] = self.check_sum_switch

        if self.enable_cyclic_replication is not None:
            result['EnableCyclicReplication'] = self.enable_cyclic_replication

        result['InstanceTopologyList'] = []
        if self.instance_topology_list is not None:
            for k1 in self.instance_topology_list:
                result['InstanceTopologyList'].append(k1.to_map() if k1 else None)

        if self.server_id is not None:
            result['ServerId'] = self.server_id

        if self.version_support_multi_cdc is not None:
            result['VersionSupportMultiCdc'] = self.version_support_multi_cdc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BinlogPersistTime') is not None:
            self.binlog_persist_time = m.get('BinlogPersistTime')

        if m.get('BinlogSize') is not None:
            self.binlog_size = m.get('BinlogSize')

        if m.get('CdcNewVersion') is not None:
            self.cdc_new_version = m.get('CdcNewVersion')

        if m.get('CheckSumSwitch') is not None:
            self.check_sum_switch = m.get('CheckSumSwitch')

        if m.get('EnableCyclicReplication') is not None:
            self.enable_cyclic_replication = m.get('EnableCyclicReplication')

        self.instance_topology_list = []
        if m.get('InstanceTopologyList') is not None:
            for k1 in m.get('InstanceTopologyList'):
                temp_model = main_models.DescribeCdcInfoResponseBodyDataInstanceTopologyList()
                self.instance_topology_list.append(temp_model.from_map(k1))

        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')

        if m.get('VersionSupportMultiCdc') is not None:
            self.version_support_multi_cdc = m.get('VersionSupportMultiCdc')

        return self

class DescribeCdcInfoResponseBodyDataInstanceTopologyList(DaraModel):
    def __init__(
        self,
        cluster_type: str = None,
        comment: str = None,
        group_name: str = None,
        hash_level: str = None,
        instance_name: str = None,
        physical_nodes: List[main_models.DescribeCdcInfoResponseBodyDataInstanceTopologyListPhysicalNodes] = None,
        stream_num: int = None,
    ):
        self.cluster_type = cluster_type
        self.comment = comment
        self.group_name = group_name
        self.hash_level = hash_level
        self.instance_name = instance_name
        self.physical_nodes = physical_nodes
        self.stream_num = stream_num

    def validate(self):
        if self.physical_nodes:
            for v1 in self.physical_nodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.hash_level is not None:
            result['HashLevel'] = self.hash_level

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        result['PhysicalNodes'] = []
        if self.physical_nodes is not None:
            for k1 in self.physical_nodes:
                result['PhysicalNodes'].append(k1.to_map() if k1 else None)

        if self.stream_num is not None:
            result['StreamNum'] = self.stream_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('HashLevel') is not None:
            self.hash_level = m.get('HashLevel')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        self.physical_nodes = []
        if m.get('PhysicalNodes') is not None:
            for k1 in m.get('PhysicalNodes'):
                temp_model = main_models.DescribeCdcInfoResponseBodyDataInstanceTopologyListPhysicalNodes()
                self.physical_nodes.append(temp_model.from_map(k1))

        if m.get('StreamNum') is not None:
            self.stream_num = m.get('StreamNum')

        return self

class DescribeCdcInfoResponseBodyDataInstanceTopologyListPhysicalNodes(DaraModel):
    def __init__(
        self,
        azone: str = None,
        disk: int = None,
        node_class: str = None,
        node_id: str = None,
        node_name: str = None,
        status: str = None,
        version: str = None,
    ):
        self.azone = azone
        self.disk = disk
        self.node_class = node_class
        self.node_id = node_id
        self.node_name = node_name
        self.status = status
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.azone is not None:
            result['AZone'] = self.azone

        if self.disk is not None:
            result['Disk'] = self.disk

        if self.node_class is not None:
            result['NodeClass'] = self.node_class

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.status is not None:
            result['Status'] = self.status

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AZone') is not None:
            self.azone = m.get('AZone')

        if m.get('Disk') is not None:
            self.disk = m.get('Disk')

        if m.get('NodeClass') is not None:
            self.node_class = m.get('NodeClass')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

