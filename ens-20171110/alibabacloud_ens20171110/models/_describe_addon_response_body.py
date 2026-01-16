# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeAddonResponseBody(DaraModel):
    def __init__(
        self,
        addons: List[main_models.DescribeAddonResponseBodyAddons] = None,
        request_id: str = None,
    ):
        self.addons = addons
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.addons:
            for v1 in self.addons:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Addons'] = []
        if self.addons is not None:
            for k1 in self.addons:
                result['Addons'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.addons = []
        if m.get('Addons') is not None:
            for k1 in m.get('Addons'):
                temp_model = main_models.DescribeAddonResponseBodyAddons()
                self.addons.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAddonResponseBodyAddons(DaraModel):
    def __init__(
        self,
        cleanup_cloud_resources: str = None,
        config_schema: List[main_models.DescribeAddonResponseBodyAddonsConfigSchema] = None,
        name: str = None,
        version: str = None,
    ):
        self.cleanup_cloud_resources = cleanup_cloud_resources
        self.config_schema = config_schema
        self.name = name
        self.version = version

    def validate(self):
        if self.config_schema:
            for v1 in self.config_schema:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cleanup_cloud_resources is not None:
            result['CleanupCloudResources'] = self.cleanup_cloud_resources

        result['ConfigSchema'] = []
        if self.config_schema is not None:
            for k1 in self.config_schema:
                result['ConfigSchema'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CleanupCloudResources') is not None:
            self.cleanup_cloud_resources = m.get('CleanupCloudResources')

        self.config_schema = []
        if m.get('ConfigSchema') is not None:
            for k1 in m.get('ConfigSchema'):
                temp_model = main_models.DescribeAddonResponseBodyAddonsConfigSchema()
                self.config_schema.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class DescribeAddonResponseBodyAddonsConfigSchema(DaraModel):
    def __init__(
        self,
        app_version: str = None,
        config_version: str = None,
        name: str = None,
        params: Any = None,
    ):
        self.app_version = app_version
        self.config_version = config_version
        self.name = name
        self.params = params

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_version is not None:
            result['AppVersion'] = self.app_version

        if self.config_version is not None:
            result['ConfigVersion'] = self.config_version

        if self.name is not None:
            result['Name'] = self.name

        if self.params is not None:
            result['Params'] = self.params

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')

        if m.get('ConfigVersion') is not None:
            self.config_version = m.get('ConfigVersion')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        return self

