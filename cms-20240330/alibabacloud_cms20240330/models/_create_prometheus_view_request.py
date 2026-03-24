# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class CreatePrometheusViewRequest(DaraModel):
    def __init__(
        self,
        auth_free_read_policy: str = None,
        enable_auth_free_read: bool = None,
        enable_auth_token: bool = None,
        prometheus_instances: List[main_models.CreatePrometheusViewRequestPrometheusInstances] = None,
        prometheus_view_name: str = None,
        resource_group_id: str = None,
        status: str = None,
        tags: List[main_models.CreatePrometheusViewRequestTags] = None,
        version: str = None,
        workspace: str = None,
    ):
        # This parameter is not in use.
        self.auth_free_read_policy = auth_free_read_policy
        # Specifies whether to enable password-free read access.
        self.enable_auth_free_read = enable_auth_free_read
        # Specifies whether to enable an authentication token.
        self.enable_auth_token = enable_auth_token
        # The list of Prometheus instances.
        # 
        # This parameter is required.
        self.prometheus_instances = prometheus_instances
        # The name of the Prometheus view.
        # 
        # This parameter is required.
        self.prometheus_view_name = prometheus_view_name
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # This parameter is not in use.
        self.status = status
        # Specifies the operation to execute.
        self.tags = tags
        # - V1: The old version.
        # 
        # - V2: The new version.
        # 
        # This parameter is required.
        self.version = version
        # The default value is default-cms-{userId}-{regionId}.
        self.workspace = workspace

    def validate(self):
        if self.prometheus_instances:
            for v1 in self.prometheus_instances:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_free_read_policy is not None:
            result['authFreeReadPolicy'] = self.auth_free_read_policy

        if self.enable_auth_free_read is not None:
            result['enableAuthFreeRead'] = self.enable_auth_free_read

        if self.enable_auth_token is not None:
            result['enableAuthToken'] = self.enable_auth_token

        result['prometheusInstances'] = []
        if self.prometheus_instances is not None:
            for k1 in self.prometheus_instances:
                result['prometheusInstances'].append(k1.to_map() if k1 else None)

        if self.prometheus_view_name is not None:
            result['prometheusViewName'] = self.prometheus_view_name

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['status'] = self.status

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.version is not None:
            result['version'] = self.version

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authFreeReadPolicy') is not None:
            self.auth_free_read_policy = m.get('authFreeReadPolicy')

        if m.get('enableAuthFreeRead') is not None:
            self.enable_auth_free_read = m.get('enableAuthFreeRead')

        if m.get('enableAuthToken') is not None:
            self.enable_auth_token = m.get('enableAuthToken')

        self.prometheus_instances = []
        if m.get('prometheusInstances') is not None:
            for k1 in m.get('prometheusInstances'):
                temp_model = main_models.CreatePrometheusViewRequestPrometheusInstances()
                self.prometheus_instances.append(temp_model.from_map(k1))

        if m.get('prometheusViewName') is not None:
            self.prometheus_view_name = m.get('prometheusViewName')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('status') is not None:
            self.status = m.get('status')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.CreatePrometheusViewRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

class CreatePrometheusViewRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class CreatePrometheusViewRequestPrometheusInstances(DaraModel):
    def __init__(
        self,
        prometheus_instance_id: str = None,
        region_id: str = None,
        user_id: str = None,
    ):
        # The instance ID.
        self.prometheus_instance_id = prometheus_instance_id
        # The region ID.
        self.region_id = region_id
        # The user ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.prometheus_instance_id is not None:
            result['prometheusInstanceId'] = self.prometheus_instance_id

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('prometheusInstanceId') is not None:
            self.prometheus_instance_id = m.get('prometheusInstanceId')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

