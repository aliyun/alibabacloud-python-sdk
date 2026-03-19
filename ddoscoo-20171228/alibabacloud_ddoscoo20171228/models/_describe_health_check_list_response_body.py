# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20171228 import models as main_models
from darabonba.model import DaraModel

class DescribeHealthCheckListResponseBody(DaraModel):
    def __init__(
        self,
        listeners: List[main_models.DescribeHealthCheckListResponseBodyListeners] = None,
        request_id: str = None,
    ):
        self.listeners = listeners
        self.request_id = request_id

    def validate(self):
        if self.listeners:
            for v1 in self.listeners:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Listeners'] = []
        if self.listeners is not None:
            for k1 in self.listeners:
                result['Listeners'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.listeners = []
        if m.get('Listeners') is not None:
            for k1 in m.get('Listeners'):
                temp_model = main_models.DescribeHealthCheckListResponseBodyListeners()
                self.listeners.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeHealthCheckListResponseBodyListeners(DaraModel):
    def __init__(
        self,
        frontend_port: int = None,
        health_check: main_models.DescribeHealthCheckListResponseBodyListenersHealthCheck = None,
        instance_id: str = None,
        protocol: str = None,
    ):
        self.frontend_port = frontend_port
        self.health_check = health_check
        self.instance_id = instance_id
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
            temp_model = main_models.DescribeHealthCheckListResponseBodyListenersHealthCheck()
            self.health_check = temp_model.from_map(m.get('HealthCheck'))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        return self

class DescribeHealthCheckListResponseBodyListenersHealthCheck(DaraModel):
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
        self.domain = domain
        self.down = down
        self.interval = interval
        self.port = port
        self.timeout = timeout
        self.type = type
        self.up = up
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

