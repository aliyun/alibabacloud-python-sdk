# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceMonitorDataResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        monitor_data: main_models.DescribeInstanceMonitorDataResponseBodyMonitorData = None,
        request_id: str = None,
    ):
        # The returned service code. A value of 0 indicates that the operation was successful.
        self.code = code
        # The set of InstanceMonitorDataType data.
        self.monitor_data = monitor_data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.monitor_data:
            self.monitor_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.monitor_data is not None:
            result['MonitorData'] = self.monitor_data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('MonitorData') is not None:
            temp_model = main_models.DescribeInstanceMonitorDataResponseBodyMonitorData()
            self.monitor_data = temp_model.from_map(m.get('MonitorData'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeInstanceMonitorDataResponseBodyMonitorData(DaraModel):
    def __init__(
        self,
        instance_monitor_data: List[main_models.DescribeInstanceMonitorDataResponseBodyMonitorDataInstanceMonitorData] = None,
    ):
        self.instance_monitor_data = instance_monitor_data

    def validate(self):
        if self.instance_monitor_data:
            for v1 in self.instance_monitor_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceMonitorData'] = []
        if self.instance_monitor_data is not None:
            for k1 in self.instance_monitor_data:
                result['InstanceMonitorData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_monitor_data = []
        if m.get('InstanceMonitorData') is not None:
            for k1 in m.get('InstanceMonitorData'):
                temp_model = main_models.DescribeInstanceMonitorDataResponseBodyMonitorDataInstanceMonitorData()
                self.instance_monitor_data.append(temp_model.from_map(k1))

        return self

class DescribeInstanceMonitorDataResponseBodyMonitorDataInstanceMonitorData(DaraModel):
    def __init__(
        self,
        cpu: str = None,
        instance_id: str = None,
        memory: str = None,
    ):
        # The vCPU usage of the instance, which is raw data. For example, a value of 0.02 indicates that the usage is 2%.
        self.cpu = cpu
        # The ID of the instance.
        self.instance_id = instance_id
        # This parameter is not yet supported.
        self.memory = memory

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['CPU'] = self.cpu

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.memory is not None:
            result['Memory'] = self.memory

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        return self

