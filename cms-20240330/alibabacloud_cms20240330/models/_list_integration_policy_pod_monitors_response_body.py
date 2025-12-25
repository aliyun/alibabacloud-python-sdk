# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ListIntegrationPolicyPodMonitorsResponseBody(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        pod_monitors: List[main_models.ListIntegrationPolicyPodMonitorsResponseBodyPodMonitors] = None,
        policy_id: str = None,
        request_id: str = None,
    ):
        # Cluster ID.
        self.cluster_id = cluster_id
        # PodMonitor list
        self.pod_monitors = pod_monitors
        # Policy ID.
        self.policy_id = policy_id
        # ID of the request
        self.request_id = request_id

    def validate(self):
        if self.pod_monitors:
            for v1 in self.pod_monitors:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id

        result['podMonitors'] = []
        if self.pod_monitors is not None:
            for k1 in self.pod_monitors:
                result['podMonitors'].append(k1.to_map() if k1 else None)

        if self.policy_id is not None:
            result['policyId'] = self.policy_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')

        self.pod_monitors = []
        if m.get('podMonitors') is not None:
            for k1 in m.get('podMonitors'):
                temp_model = main_models.ListIntegrationPolicyPodMonitorsResponseBodyPodMonitors()
                self.pod_monitors.append(temp_model.from_map(k1))

        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListIntegrationPolicyPodMonitorsResponseBodyPodMonitors(DaraModel):
    def __init__(
        self,
        addon_name: str = None,
        addon_release_name: str = None,
        addon_version: str = None,
        config_yaml: str = None,
        enable_status: str = None,
        encrypt_yaml: bool = None,
        endpoints: List[main_models.ListIntegrationPolicyPodMonitorsResponseBodyPodMonitorsEndpoints] = None,
        matched_pod_count: int = None,
        name: str = None,
        namespace: str = None,
    ):
        # Addon name.
        self.addon_name = addon_name
        # Addon Release name.
        self.addon_release_name = addon_release_name
        # Addon version.
        self.addon_version = addon_version
        # Configuration yaml.
        self.config_yaml = config_yaml
        # Enable status.
        self.enable_status = enable_status
        # Encrypt yaml.
        self.encrypt_yaml = encrypt_yaml
        # Instance endpoints.
        self.endpoints = endpoints
        # Number of matched pods
        self.matched_pod_count = matched_pod_count
        # Collection name.
        self.name = name
        # Namespace
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

        if self.matched_pod_count is not None:
            result['matchedPodCount'] = self.matched_pod_count

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
                temp_model = main_models.ListIntegrationPolicyPodMonitorsResponseBodyPodMonitorsEndpoints()
                self.endpoints.append(temp_model.from_map(k1))

        if m.get('matchedPodCount') is not None:
            self.matched_pod_count = m.get('matchedPodCount')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        return self

class ListIntegrationPolicyPodMonitorsResponseBodyPodMonitorsEndpoints(DaraModel):
    def __init__(
        self,
        interval: str = None,
        matched_target_count: int = None,
        path: str = None,
        port: str = None,
        target_port: str = None,
    ):
        # Collection interval
        self.interval = interval
        # Number of matched targets
        self.matched_target_count = matched_target_count
        # Metric collection path
        self.path = path
        # Port number
        self.port = port
        # Target port
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

