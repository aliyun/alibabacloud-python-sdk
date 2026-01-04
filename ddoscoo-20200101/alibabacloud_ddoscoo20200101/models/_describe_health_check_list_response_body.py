# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeHealthCheckListResponseBody(DaraModel):
    def __init__(
        self,
        health_check_list: List[main_models.DescribeHealthCheckListResponseBodyHealthCheckList] = None,
        request_id: str = None,
    ):
        # An array that consists of information about the health check configuration.
        self.health_check_list = health_check_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.health_check_list:
            for v1 in self.health_check_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['HealthCheckList'] = []
        if self.health_check_list is not None:
            for k1 in self.health_check_list:
                result['HealthCheckList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.health_check_list = []
        if m.get('HealthCheckList') is not None:
            for k1 in m.get('HealthCheckList'):
                temp_model = main_models.DescribeHealthCheckListResponseBodyHealthCheckList()
                self.health_check_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeHealthCheckListResponseBodyHealthCheckList(DaraModel):
    def __init__(
        self,
        frontend_port: int = None,
        health_check: main_models.DescribeHealthCheckListResponseBodyHealthCheckListHealthCheck = None,
        instance_id: str = None,
        protocol: str = None,
    ):
        # The forwarding port.
        self.frontend_port = frontend_port
        # The health check configuration.
        self.health_check = health_check
        # The ID of the instance.
        self.instance_id = instance_id
        # The forwarding protocol. Valid values:
        # 
        # *   **tcp**
        # *   **udp**
        self.protocol = protocol

    def validate(self):
        if self.health_check:
            self.health_check.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port

        if self.health_check is not None:
            result['HealthCheck'] = self.health_check.to_map()

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')

        if m.get('HealthCheck') is not None:
            temp_model = main_models.DescribeHealthCheckListResponseBodyHealthCheckListHealthCheck()
            self.health_check = temp_model.from_map(m.get('HealthCheck'))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        return self

class DescribeHealthCheckListResponseBodyHealthCheckListHealthCheck(DaraModel):
    def __init__(
        self,
        domain: str = None,
        down: int = None,
        interval: int = None,
        port: int = None,
        timeout: int = None,
        type: str = None,
        up: int = None,
        uri: str = None,
    ):
        # The domain name.
        # 
        # >  This parameter is returned only when the Layer 7 health check configuration is queried.
        self.domain = domain
        # The number of consecutive failed health checks that must occur before a port is declared unhealthy. Valid values: **1** to **10**.
        self.down = down
        # The interval at which checks are performed. Valid values: **1** to **30**. Unit: seconds.
        self.interval = interval
        # The port that was checked.
        self.port = port
        # The response timeout period. Valid values: **1** to **30**. Unit: seconds.
        self.timeout = timeout
        # The type of the protocol. Valid values:
        # 
        # *   **tcp**: The Layer 4 health check configuration was queried.
        # *   **http**: The Layer 7 health check configuration was queried.
        self.type = type
        # The number of consecutive successful health checks that must occur before a port is declared healthy. Valid values: **1** to **10**.
        self.up = up
        # The check path.
        # 
        # >  This parameter is returned only when the Layer 7 health check configuration is queried.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.down is not None:
            result['Down'] = self.down

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.port is not None:
            result['Port'] = self.port

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.type is not None:
            result['Type'] = self.type

        if self.up is not None:
            result['Up'] = self.up

        if self.uri is not None:
            result['Uri'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Down') is not None:
            self.down = m.get('Down')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Up') is not None:
            self.up = m.get('Up')

        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        return self

