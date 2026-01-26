# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class DescribeEnvServiceMonitorResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.DescribeEnvServiceMonitorResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed.
        self.code = code
        # The returned struct.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeEnvServiceMonitorResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeEnvServiceMonitorResponseBodyData(DaraModel):
    def __init__(
        self,
        config_yaml: str = None,
        environment_id: str = None,
        namespace: str = None,
        region_id: str = None,
        service_monitor_name: str = None,
        status: str = None,
    ):
        # The YAML configuration file of the ServiceMonitor.
        self.config_yaml = config_yaml
        # The ID of the environment instance.
        self.environment_id = environment_id
        # The namespace.
        self.namespace = namespace
        # The region ID.
        self.region_id = region_id
        # The name of the ServiceMonitor.
        self.service_monitor_name = service_monitor_name
        # The status. Valid values:
        # 
        # *   run
        # *   stop
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_yaml is not None:
            result['ConfigYaml'] = self.config_yaml

        if self.environment_id is not None:
            result['EnvironmentId'] = self.environment_id

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_monitor_name is not None:
            result['ServiceMonitorName'] = self.service_monitor_name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigYaml') is not None:
            self.config_yaml = m.get('ConfigYaml')

        if m.get('EnvironmentId') is not None:
            self.environment_id = m.get('EnvironmentId')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceMonitorName') is not None:
            self.service_monitor_name = m.get('ServiceMonitorName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

