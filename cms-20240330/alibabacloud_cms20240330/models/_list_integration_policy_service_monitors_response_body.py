# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ListIntegrationPolicyServiceMonitorsResponseBody(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        policy_id: str = None,
        request_id: str = None,
        service_monitors: List[main_models.ListIntegrationPolicyServiceMonitorsResponseBodyServiceMonitors] = None,
    ):
        self.cluster_id = cluster_id
        self.policy_id = policy_id
        self.request_id = request_id
        self.service_monitors = service_monitors

    def validate(self):
        if self.service_monitors:
            for v1 in self.service_monitors:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id

        if self.policy_id is not None:
            result['policyId'] = self.policy_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['serviceMonitors'] = []
        if self.service_monitors is not None:
            for k1 in self.service_monitors:
                result['serviceMonitors'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')

        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.service_monitors = []
        if m.get('serviceMonitors') is not None:
            for k1 in m.get('serviceMonitors'):
                temp_model = main_models.ListIntegrationPolicyServiceMonitorsResponseBodyServiceMonitors()
                self.service_monitors.append(temp_model.from_map(k1))

        return self

class ListIntegrationPolicyServiceMonitorsResponseBodyServiceMonitors(DaraModel):
    def __init__(
        self,
        addon_name: str = None,
        addon_release_name: str = None,
        addon_version: str = None,
        config_yaml: str = None,
        enable_status: str = None,
        encrypt_yaml: bool = None,
        endpoints: List[main_models.ListIntegrationPolicyServiceMonitorsResponseBodyServiceMonitorsEndpoints] = None,
        matched_service_count: int = None,
        name: str = None,
        namespace: str = None,
    ):
        self.addon_name = addon_name
        self.addon_release_name = addon_release_name
        self.addon_version = addon_version
        self.config_yaml = config_yaml
        self.enable_status = enable_status
        self.encrypt_yaml = encrypt_yaml
        self.endpoints = endpoints
        self.matched_service_count = matched_service_count
        self.name = name
        self.namespace = namespace

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
            result['addonName'] = self.addon_name

        if self.addon_release_name is not None:
            result['addonReleaseName'] = self.addon_release_name

        if self.addon_version is not None:
            result['addonVersion'] = self.addon_version

        if self.config_yaml is not None:
            result['configYaml'] = self.config_yaml

        if self.enable_status is not None:
            result['enableStatus'] = self.enable_status

        if self.encrypt_yaml is not None:
            result['encryptYaml'] = self.encrypt_yaml

        result['endpoints'] = []
        if self.endpoints is not None:
            for k1 in self.endpoints:
                result['endpoints'].append(k1.to_map() if k1 else None)

        if self.matched_service_count is not None:
            result['matchedServiceCount'] = self.matched_service_count

        if self.name is not None:
            result['name'] = self.name

        if self.namespace is not None:
            result['namespace'] = self.namespace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('addonName') is not None:
            self.addon_name = m.get('addonName')

        if m.get('addonReleaseName') is not None:
            self.addon_release_name = m.get('addonReleaseName')

        if m.get('addonVersion') is not None:
            self.addon_version = m.get('addonVersion')

        if m.get('configYaml') is not None:
            self.config_yaml = m.get('configYaml')

        if m.get('enableStatus') is not None:
            self.enable_status = m.get('enableStatus')

        if m.get('encryptYaml') is not None:
            self.encrypt_yaml = m.get('encryptYaml')

        self.endpoints = []
        if m.get('endpoints') is not None:
            for k1 in m.get('endpoints'):
                temp_model = main_models.ListIntegrationPolicyServiceMonitorsResponseBodyServiceMonitorsEndpoints()
                self.endpoints.append(temp_model.from_map(k1))

        if m.get('matchedServiceCount') is not None:
            self.matched_service_count = m.get('matchedServiceCount')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        return self

class ListIntegrationPolicyServiceMonitorsResponseBodyServiceMonitorsEndpoints(DaraModel):
    def __init__(
        self,
        interval: str = None,
        matched_target_count: int = None,
        path: str = None,
        port: str = None,
        target_port: str = None,
    ):
        self.interval = interval
        self.matched_target_count = matched_target_count
        self.path = path
        self.port = port
        self.target_port = target_port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.interval is not None:
            result['interval'] = self.interval

        if self.matched_target_count is not None:
            result['matchedTargetCount'] = self.matched_target_count

        if self.path is not None:
            result['path'] = self.path

        if self.port is not None:
            result['port'] = self.port

        if self.target_port is not None:
            result['targetPort'] = self.target_port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('interval') is not None:
            self.interval = m.get('interval')

        if m.get('matchedTargetCount') is not None:
            self.matched_target_count = m.get('matchedTargetCount')

        if m.get('path') is not None:
            self.path = m.get('path')

        if m.get('port') is not None:
            self.port = m.get('port')

        if m.get('targetPort') is not None:
            self.target_port = m.get('targetPort')

        return self

