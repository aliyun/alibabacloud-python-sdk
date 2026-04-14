# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class CacheCluster(DaraModel):
    def __init__(
        self,
        binded_workspaces: List[str] = None,
        cachesets: List[main_models.CacheClusterCachesets] = None,
        cluster_id: str = None,
        configuration: str = None,
        configurations: List[main_models.CacheClusterConfigurations] = None,
        creator: str = None,
        gmt_created: int = None,
        gmt_modified: int = None,
        modifier: str = None,
        name: str = None,
        payment_type: str = None,
        region_id: str = None,
        resource_spec: main_models.CacheClusterResourceSpec = None,
        state: str = None,
        used_resource_spec: main_models.CacheClusterUsedResourceSpec = None,
    ):
        self.binded_workspaces = binded_workspaces
        self.cachesets = cachesets
        self.cluster_id = cluster_id
        self.configuration = configuration
        self.configurations = configurations
        self.creator = creator
        self.gmt_created = gmt_created
        self.gmt_modified = gmt_modified
        self.modifier = modifier
        self.name = name
        self.payment_type = payment_type
        self.region_id = region_id
        self.resource_spec = resource_spec
        self.state = state
        self.used_resource_spec = used_resource_spec

    def validate(self):
        if self.cachesets:
            for v1 in self.cachesets:
                 if v1:
                    v1.validate()
        if self.configurations:
            for v1 in self.configurations:
                 if v1:
                    v1.validate()
        if self.resource_spec:
            self.resource_spec.validate()
        if self.used_resource_spec:
            self.used_resource_spec.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.binded_workspaces is not None:
            result['bindedWorkspaces'] = self.binded_workspaces

        result['cachesets'] = []
        if self.cachesets is not None:
            for k1 in self.cachesets:
                result['cachesets'].append(k1.to_map() if k1 else None)

        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id

        if self.configuration is not None:
            result['configuration'] = self.configuration

        result['configurations'] = []
        if self.configurations is not None:
            for k1 in self.configurations:
                result['configurations'].append(k1.to_map() if k1 else None)

        if self.creator is not None:
            result['creator'] = self.creator

        if self.gmt_created is not None:
            result['gmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.modifier is not None:
            result['modifier'] = self.modifier

        if self.name is not None:
            result['name'] = self.name

        if self.payment_type is not None:
            result['paymentType'] = self.payment_type

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.resource_spec is not None:
            result['resourceSpec'] = self.resource_spec.to_map()

        if self.state is not None:
            result['state'] = self.state

        if self.used_resource_spec is not None:
            result['usedResourceSpec'] = self.used_resource_spec.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bindedWorkspaces') is not None:
            self.binded_workspaces = m.get('bindedWorkspaces')

        self.cachesets = []
        if m.get('cachesets') is not None:
            for k1 in m.get('cachesets'):
                temp_model = main_models.CacheClusterCachesets()
                self.cachesets.append(temp_model.from_map(k1))

        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')

        if m.get('configuration') is not None:
            self.configuration = m.get('configuration')

        self.configurations = []
        if m.get('configurations') is not None:
            for k1 in m.get('configurations'):
                temp_model = main_models.CacheClusterConfigurations()
                self.configurations.append(temp_model.from_map(k1))

        if m.get('creator') is not None:
            self.creator = m.get('creator')

        if m.get('gmtCreated') is not None:
            self.gmt_created = m.get('gmtCreated')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('resourceSpec') is not None:
            temp_model = main_models.CacheClusterResourceSpec()
            self.resource_spec = temp_model.from_map(m.get('resourceSpec'))

        if m.get('state') is not None:
            self.state = m.get('state')

        if m.get('usedResourceSpec') is not None:
            temp_model = main_models.CacheClusterUsedResourceSpec()
            self.used_resource_spec = temp_model.from_map(m.get('usedResourceSpec'))

        return self

class CacheClusterUsedResourceSpec(DaraModel):
    def __init__(
        self,
        band_width: int = None,
        storage: int = None,
    ):
        self.band_width = band_width
        self.storage = storage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.band_width is not None:
            result['bandWidth'] = self.band_width

        if self.storage is not None:
            result['storage'] = self.storage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bandWidth') is not None:
            self.band_width = m.get('bandWidth')

        if m.get('storage') is not None:
            self.storage = m.get('storage')

        return self

class CacheClusterResourceSpec(DaraModel):
    def __init__(
        self,
        band_width: int = None,
        storage: int = None,
    ):
        self.band_width = band_width
        self.storage = storage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.band_width is not None:
            result['bandWidth'] = self.band_width

        if self.storage is not None:
            result['storage'] = self.storage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bandWidth') is not None:
            self.band_width = m.get('bandWidth')

        if m.get('storage') is not None:
            self.storage = m.get('storage')

        return self

class CacheClusterConfigurations(DaraModel):
    def __init__(
        self,
        content: str = None,
        name: str = None,
    ):
        self.content = content
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self



class CacheClusterCachesets(DaraModel):
    def __init__(
        self,
        name: str = None,
        path: str = None,
    ):
        self.name = name
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.path is not None:
            result['path'] = self.path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('path') is not None:
            self.path = m.get('path')

        return self

