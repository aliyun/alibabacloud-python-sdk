# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeCustomEndpointListResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeCustomEndpointListResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
        self.request_id = request_id

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeCustomEndpointListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCustomEndpointListResponseBodyData(DaraModel):
    def __init__(
        self,
        can_delete_count: int = None,
        endpoints: List[main_models.DescribeCustomEndpointListResponseBodyDataEndpoints] = None,
    ):
        self.can_delete_count = can_delete_count
        self.endpoints = endpoints

    def validate(self):
        if self.endpoints:
            for v1 in self.endpoints:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_delete_count is not None:
            result['CanDeleteCount'] = self.can_delete_count

        result['Endpoints'] = []
        if self.endpoints is not None:
            for k1 in self.endpoints:
                result['Endpoints'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanDeleteCount') is not None:
            self.can_delete_count = m.get('CanDeleteCount')

        self.endpoints = []
        if m.get('Endpoints') is not None:
            for k1 in m.get('Endpoints'):
                temp_model = main_models.DescribeCustomEndpointListResponseBodyDataEndpoints()
                self.endpoints.append(temp_model.from_map(k1))

        return self

class DescribeCustomEndpointListResponseBodyDataEndpoints(DaraModel):
    def __init__(
        self,
        cn_names: List[str] = None,
        connection_string: str = None,
        custom_endpoint_id: str = None,
        dbinstance_name: str = None,
        name: str = None,
        node_auto_enter: str = None,
        node_role: str = None,
        port: int = None,
        status: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # [\\"pxc-i-vb1sqa7llp\\",\\"pxc-i-bemprx50ad\\"]
        self.cn_names = cn_names
        self.connection_string = connection_string
        self.custom_endpoint_id = custom_endpoint_id
        self.dbinstance_name = dbinstance_name
        self.name = name
        self.node_auto_enter = node_auto_enter
        self.node_role = node_role
        self.port = port
        self.status = status
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cn_names is not None:
            result['CnNames'] = self.cn_names

        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.custom_endpoint_id is not None:
            result['CustomEndpointId'] = self.custom_endpoint_id

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.name is not None:
            result['Name'] = self.name

        if self.node_auto_enter is not None:
            result['NodeAutoEnter'] = self.node_auto_enter

        if self.node_role is not None:
            result['NodeRole'] = self.node_role

        if self.port is not None:
            result['Port'] = self.port

        if self.status is not None:
            result['Status'] = self.status

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CnNames') is not None:
            self.cn_names = m.get('CnNames')

        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('CustomEndpointId') is not None:
            self.custom_endpoint_id = m.get('CustomEndpointId')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NodeAutoEnter') is not None:
            self.node_auto_enter = m.get('NodeAutoEnter')

        if m.get('NodeRole') is not None:
            self.node_role = m.get('NodeRole')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

