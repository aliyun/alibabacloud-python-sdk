# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class ListPrometheusMonitoringResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.ListPrometheusMonitoringResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code. The status code 200 indicates that the request was successful.
        self.code = code
        # The returned struct.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListPrometheusMonitoringResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListPrometheusMonitoringResponseBodyData(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        config_yaml: str = None,
        monitoring_name: str = None,
        status: str = None,
        type: str = None,
    ):
        # The ID of the Prometheus instance.
        self.cluster_id = cluster_id
        # The monitoring configuration. The value is a YAML string.
        self.config_yaml = config_yaml
        # The name of the monitoring configuration.
        self.monitoring_name = monitoring_name
        # The status of the monitoring configuration.
        self.status = status
        # The type of the monitoring configuration.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.config_yaml is not None:
            result['ConfigYaml'] = self.config_yaml

        if self.monitoring_name is not None:
            result['MonitoringName'] = self.monitoring_name

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ConfigYaml') is not None:
            self.config_yaml = m.get('ConfigYaml')

        if m.get('MonitoringName') is not None:
            self.monitoring_name = m.get('MonitoringName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

