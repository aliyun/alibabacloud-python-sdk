# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20171228 import models as main_models
from darabonba.model import DaraModel

class DescribeHealthCheckStatusListResponseBody(DaraModel):
    def __init__(
        self,
        health_check_status_list: List[main_models.DescribeHealthCheckStatusListResponseBodyHealthCheckStatusList] = None,
        request_id: str = None,
    ):
        self.health_check_status_list = health_check_status_list
        self.request_id = request_id

    def validate(self):
        if self.health_check_status_list:
            for v1 in self.health_check_status_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['HealthCheckStatusList'] = []
        if self.health_check_status_list is not None:
            for k1 in self.health_check_status_list:
                result['HealthCheckStatusList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.health_check_status_list = []
        if m.get('HealthCheckStatusList') is not None:
            for k1 in m.get('HealthCheckStatusList'):
                temp_model = main_models.DescribeHealthCheckStatusListResponseBodyHealthCheckStatusList()
                self.health_check_status_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeHealthCheckStatusListResponseBodyHealthCheckStatusList(DaraModel):
    def __init__(
        self,
        frontend_port: int = None,
        instance_id: str = None,
        protocol: str = None,
        real_server_status_list: List[main_models.DescribeHealthCheckStatusListResponseBodyHealthCheckStatusListRealServerStatusList] = None,
        status: str = None,
    ):
        self.frontend_port = frontend_port
        self.instance_id = instance_id
        self.protocol = protocol
        self.real_server_status_list = real_server_status_list
        self.status = status

    def validate(self):
        if self.real_server_status_list:
            for v1 in self.real_server_status_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        result['RealServerStatusList'] = []
        if self.real_server_status_list is not None:
            for k1 in self.real_server_status_list:
                result['RealServerStatusList'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        self.real_server_status_list = []
        if m.get('RealServerStatusList') is not None:
            for k1 in m.get('RealServerStatusList'):
                temp_model = main_models.DescribeHealthCheckStatusListResponseBodyHealthCheckStatusListRealServerStatusList()
                self.real_server_status_list.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeHealthCheckStatusListResponseBodyHealthCheckStatusListRealServerStatusList(DaraModel):
    def __init__(
        self,
        address: str = None,
        status: str = None,
    ):
        self.address = address
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

