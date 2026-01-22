# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeColumnarInfoResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeColumnarInfoResponseBodyData = None,
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
            temp_model = main_models.DescribeColumnarInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeColumnarInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        binlog_persist_time: int = None,
        binlog_size: int = None,
        check_sum_switch: str = None,
        class_code: str = None,
        columnar_new_version: str = None,
        columnar_version: str = None,
        instance_topology_list: List[main_models.DescribeColumnarInfoResponseBodyDataInstanceTopologyList] = None,
        server_id: int = None,
    ):
        self.binlog_persist_time = binlog_persist_time
        # This parameter is required.
        self.binlog_size = binlog_size
        self.check_sum_switch = check_sum_switch
        self.class_code = class_code
        # This parameter is required.
        self.columnar_new_version = columnar_new_version
        self.columnar_version = columnar_version
        self.instance_topology_list = instance_topology_list
        # server id
        # 
        # This parameter is required.
        self.server_id = server_id

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

        if self.check_sum_switch is not None:
            result['CheckSumSwitch'] = self.check_sum_switch

        if self.class_code is not None:
            result['ClassCode'] = self.class_code

        if self.columnar_new_version is not None:
            result['ColumnarNewVersion'] = self.columnar_new_version

        if self.columnar_version is not None:
            result['ColumnarVersion'] = self.columnar_version

        result['InstanceTopologyList'] = []
        if self.instance_topology_list is not None:
            for k1 in self.instance_topology_list:
                result['InstanceTopologyList'].append(k1.to_map() if k1 else None)

        if self.server_id is not None:
            result['ServerId'] = self.server_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BinlogPersistTime') is not None:
            self.binlog_persist_time = m.get('BinlogPersistTime')

        if m.get('BinlogSize') is not None:
            self.binlog_size = m.get('BinlogSize')

        if m.get('CheckSumSwitch') is not None:
            self.check_sum_switch = m.get('CheckSumSwitch')

        if m.get('ClassCode') is not None:
            self.class_code = m.get('ClassCode')

        if m.get('ColumnarNewVersion') is not None:
            self.columnar_new_version = m.get('ColumnarNewVersion')

        if m.get('ColumnarVersion') is not None:
            self.columnar_version = m.get('ColumnarVersion')

        self.instance_topology_list = []
        if m.get('InstanceTopologyList') is not None:
            for k1 in m.get('InstanceTopologyList'):
                temp_model = main_models.DescribeColumnarInfoResponseBodyDataInstanceTopologyList()
                self.instance_topology_list.append(temp_model.from_map(k1))

        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')

        return self

class DescribeColumnarInfoResponseBodyDataInstanceTopologyList(DaraModel):
    def __init__(
        self,
        comment: str = None,
        instance_name: str = None,
        physical_nodes: List[main_models.DescribeColumnarInfoResponseBodyDataInstanceTopologyListPhysicalNodes] = None,
    ):
        self.comment = comment
        self.instance_name = instance_name
        self.physical_nodes = physical_nodes

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
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        result['PhysicalNodes'] = []
        if self.physical_nodes is not None:
            for k1 in self.physical_nodes:
                result['PhysicalNodes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        self.physical_nodes = []
        if m.get('PhysicalNodes') is not None:
            for k1 in m.get('PhysicalNodes'):
                temp_model = main_models.DescribeColumnarInfoResponseBodyDataInstanceTopologyListPhysicalNodes()
                self.physical_nodes.append(temp_model.from_map(k1))

        return self

class DescribeColumnarInfoResponseBodyDataInstanceTopologyListPhysicalNodes(DaraModel):
    def __init__(
        self,
        azone: str = None,
        disk: int = None,
        node_class: str = None,
        node_id: str = None,
        status: str = None,
        version: str = None,
    ):
        self.azone = azone
        self.disk = disk
        self.node_class = node_class
        self.node_id = node_id
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

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

