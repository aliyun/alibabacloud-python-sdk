# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class DescribeEnvPodMonitorResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.DescribeEnvPodMonitorResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code. The status code 200 indicates that the request was successful.
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
            temp_model = main_models.DescribeEnvPodMonitorResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeEnvPodMonitorResponseBodyData(DaraModel):
    def __init__(
        self,
        config_yaml: str = None,
        environment_id: str = None,
        namespace: str = None,
        pod_monitor_name: str = None,
        region_id: str = None,
        status: str = None,
    ):
        # The YAML string of the PodMonitor.
        self.config_yaml = config_yaml
        # The ID of the environment instance.
        self.environment_id = environment_id
        # The namespace.
        self.namespace = namespace
        # The name of the PodMonitor.
        self.pod_monitor_name = pod_monitor_name
        # The region ID.
        self.region_id = region_id
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

        if self.pod_monitor_name is not None:
            result['PodMonitorName'] = self.pod_monitor_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

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

        if m.get('PodMonitorName') is not None:
            self.pod_monitor_name = m.get('PodMonitorName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

