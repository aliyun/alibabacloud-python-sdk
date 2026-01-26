# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class ListEnvServiceMonitorsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.ListEnvServiceMonitorsResponseBodyData] = None,
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
                temp_model = main_models.ListEnvServiceMonitorsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListEnvServiceMonitorsResponseBodyData(DaraModel):
    def __init__(
        self,
        addon_name: str = None,
        addon_release_name: str = None,
        addon_version: str = None,
        config_yaml: str = None,
        creation_timestamp: str = None,
        endpoints: List[main_models.ListEnvServiceMonitorsResponseBodyDataEndpoints] = None,
        environment_id: str = None,
        matched_service_count: int = None,
        namespace: str = None,
        region_id: str = None,
        service_monitor_name: str = None,
        status: str = None,
    ):
        # The name of the add-on to which the ServiceMonitor belongs.
        self.addon_name = addon_name
        # The instance name of the add-on.
        self.addon_release_name = addon_release_name
        # The version of the add-on.
        self.addon_version = addon_version
        # The YAML configuration string.
        self.config_yaml = config_yaml
        # The time when the ServiceMonitor was created. The value of this parameter is a timestamp.
        self.creation_timestamp = creation_timestamp
        # The endpoints of the ServiceMonitor.
        self.endpoints = endpoints
        # The environment ID.
        self.environment_id = environment_id
        # The number of matched services.
        self.matched_service_count = matched_service_count
        # The namespace.
        self.namespace = namespace
        # The region ID.
        self.region_id = region_id
        # The name of the ServiceMonitor.
        self.service_monitor_name = service_monitor_name
        # The status of the ServiceMonitor.
        self.status = status

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
        if self.addon_name is not None:
            result['AddonName'] = self.addon_name

        if self.addon_release_name is not None:
            result['AddonReleaseName'] = self.addon_release_name

        if self.addon_version is not None:
            result['AddonVersion'] = self.addon_version

        if self.config_yaml is not None:
            result['ConfigYaml'] = self.config_yaml

        if self.creation_timestamp is not None:
            result['CreationTimestamp'] = self.creation_timestamp

        result['Endpoints'] = []
        if self.endpoints is not None:
            for k1 in self.endpoints:
                result['Endpoints'].append(k1.to_map() if k1 else None)

        if self.environment_id is not None:
            result['EnvironmentId'] = self.environment_id

        if self.matched_service_count is not None:
            result['MatchedServiceCount'] = self.matched_service_count

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
        if m.get('AddonName') is not None:
            self.addon_name = m.get('AddonName')

        if m.get('AddonReleaseName') is not None:
            self.addon_release_name = m.get('AddonReleaseName')

        if m.get('AddonVersion') is not None:
            self.addon_version = m.get('AddonVersion')

        if m.get('ConfigYaml') is not None:
            self.config_yaml = m.get('ConfigYaml')

        if m.get('CreationTimestamp') is not None:
            self.creation_timestamp = m.get('CreationTimestamp')

        self.endpoints = []
        if m.get('Endpoints') is not None:
            for k1 in m.get('Endpoints'):
                temp_model = main_models.ListEnvServiceMonitorsResponseBodyDataEndpoints()
                self.endpoints.append(temp_model.from_map(k1))

        if m.get('EnvironmentId') is not None:
            self.environment_id = m.get('EnvironmentId')

        if m.get('MatchedServiceCount') is not None:
            self.matched_service_count = m.get('MatchedServiceCount')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceMonitorName') is not None:
            self.service_monitor_name = m.get('ServiceMonitorName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListEnvServiceMonitorsResponseBodyDataEndpoints(DaraModel):
    def __init__(
        self,
        interval: str = None,
        matched_target_count: int = None,
        path: str = None,
        port: str = None,
        target_port: int = None,
    ):
        # The collection interval.
        self.interval = interval
        # The number of pods that match the ServiceMonitor endpoint.
        self.matched_target_count = matched_target_count
        # The collection path.
        self.path = path
        # The external port.
        self.port = port
        # The destination port.
        self.target_port = target_port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.interval is not None:
            result['Interval'] = self.interval

        if self.matched_target_count is not None:
            result['MatchedTargetCount'] = self.matched_target_count

        if self.path is not None:
            result['Path'] = self.path

        if self.port is not None:
            result['Port'] = self.port

        if self.target_port is not None:
            result['TargetPort'] = self.target_port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('MatchedTargetCount') is not None:
            self.matched_target_count = m.get('MatchedTargetCount')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('TargetPort') is not None:
            self.target_port = m.get('TargetPort')

        return self

