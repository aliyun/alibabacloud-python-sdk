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
        cache_cluster_id: str = None,
        cache_cluster_name: str = None,
        cachesets: List[main_models.CacheClusterCachesets] = None,
        cluster_id: str = None,
        configuration: str = None,
        configurations: List[main_models.CacheClusterConfigurations] = None,
        create_time: str = None,
        creator: str = None,
        extra: str = None,
        gmt_created: int = None,
        gmt_modified: int = None,
        modifier: str = None,
        name: str = None,
        payment_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_spec: main_models.CacheClusterResourceSpec = None,
        state: str = None,
        tables: List[main_models.CacheClusterTables] = None,
        tags: List[main_models.CacheClusterTags] = None,
        used_resource_spec: main_models.CacheClusterUsedResourceSpec = None,
        version: str = None,
    ):
        # The associated workspaces.
        self.binded_workspaces = binded_workspaces
        # The cache cluster ID.
        self.cache_cluster_id = cache_cluster_id
        # The cache cluster name.
        self.cache_cluster_name = cache_cluster_name
        # The list of cache sets associated with the cache cluster.
        self.cachesets = cachesets
        # The cache cluster ID.
        self.cluster_id = cluster_id
        self.configuration = configuration
        # The list of configuration files for the cache cluster.
        self.configurations = configurations
        # The creation time.
        self.create_time = create_time
        # The creator UID.
        self.creator = creator
        self.extra = extra
        # The creation time. The value is a UNIX timestamp in milliseconds.
        self.gmt_created = gmt_created
        # The modification time. The value is a UNIX timestamp in milliseconds.
        self.gmt_modified = gmt_modified
        # The modifier UID.
        self.modifier = modifier
        # The cache cluster name.
        self.name = name
        # The billing method.
        self.payment_type = payment_type
        # The region ID.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The cache cluster specifications.
        self.resource_spec = resource_spec
        # The cache cluster status.
        self.state = state
        # The list of data tables associated with the cache cluster.
        self.tables = tables
        # The list of tags for the cache cluster.
        self.tags = tags
        # The resource specifications used by the cache cluster.
        self.used_resource_spec = used_resource_spec
        # The cache cluster version.
        self.version = version

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
        if self.tables:
            for v1 in self.tables:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
        if self.used_resource_spec:
            self.used_resource_spec.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.binded_workspaces is not None:
            result['bindedWorkspaces'] = self.binded_workspaces

        if self.cache_cluster_id is not None:
            result['cacheClusterId'] = self.cache_cluster_id

        if self.cache_cluster_name is not None:
            result['cacheClusterName'] = self.cache_cluster_name

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

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.creator is not None:
            result['creator'] = self.creator

        if self.extra is not None:
            result['extra'] = self.extra

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

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.resource_spec is not None:
            result['resourceSpec'] = self.resource_spec.to_map()

        if self.state is not None:
            result['state'] = self.state

        result['tables'] = []
        if self.tables is not None:
            for k1 in self.tables:
                result['tables'].append(k1.to_map() if k1 else None)

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.used_resource_spec is not None:
            result['usedResourceSpec'] = self.used_resource_spec.to_map()

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bindedWorkspaces') is not None:
            self.binded_workspaces = m.get('bindedWorkspaces')

        if m.get('cacheClusterId') is not None:
            self.cache_cluster_id = m.get('cacheClusterId')

        if m.get('cacheClusterName') is not None:
            self.cache_cluster_name = m.get('cacheClusterName')

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

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('creator') is not None:
            self.creator = m.get('creator')

        if m.get('extra') is not None:
            self.extra = m.get('extra')

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

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('resourceSpec') is not None:
            temp_model = main_models.CacheClusterResourceSpec()
            self.resource_spec = temp_model.from_map(m.get('resourceSpec'))

        if m.get('state') is not None:
            self.state = m.get('state')

        self.tables = []
        if m.get('tables') is not None:
            for k1 in m.get('tables'):
                temp_model = main_models.CacheClusterTables()
                self.tables.append(temp_model.from_map(k1))

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.CacheClusterTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('usedResourceSpec') is not None:
            temp_model = main_models.CacheClusterUsedResourceSpec()
            self.used_resource_spec = temp_model.from_map(m.get('usedResourceSpec'))

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class CacheClusterUsedResourceSpec(DaraModel):
    def __init__(
        self,
        band_width: int = None,
        storage: int = None,
    ):
        # The used bandwidth.
        self.band_width = band_width
        # The used storage capacity.
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

class CacheClusterTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

class CacheClusterTables(DaraModel):
    def __init__(
        self,
        catalog_id: str = None,
        catalog_provider: str = None,
        database: str = None,
        table: str = None,
        workspace_id: str = None,
    ):
        # The data catalog ID.
        self.catalog_id = catalog_id
        # The data catalog provider.
        self.catalog_provider = catalog_provider
        # The database name.
        self.database = database
        # The data table name.
        self.table = table
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_id is not None:
            result['catalogId'] = self.catalog_id

        if self.catalog_provider is not None:
            result['catalogProvider'] = self.catalog_provider

        if self.database is not None:
            result['database'] = self.database

        if self.table is not None:
            result['table'] = self.table

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('catalogId') is not None:
            self.catalog_id = m.get('catalogId')

        if m.get('catalogProvider') is not None:
            self.catalog_provider = m.get('catalogProvider')

        if m.get('database') is not None:
            self.database = m.get('database')

        if m.get('table') is not None:
            self.table = m.get('table')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class CacheClusterResourceSpec(DaraModel):
    def __init__(
        self,
        band_width: int = None,
        ha: bool = None,
        storage: int = None,
    ):
        # The bandwidth.
        self.band_width = band_width
        # Specifies whether high availability is enabled.
        self.ha = ha
        # The physical storage.
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

        if self.ha is not None:
            result['ha'] = self.ha

        if self.storage is not None:
            result['storage'] = self.storage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bandWidth') is not None:
            self.band_width = m.get('bandWidth')

        if m.get('ha') is not None:
            self.ha = m.get('ha')

        if m.get('storage') is not None:
            self.storage = m.get('storage')

        return self

class CacheClusterConfigurations(DaraModel):
    def __init__(
        self,
        content: str = None,
        name: str = None,
    ):
        # The content of the configuration file.
        self.content = content
        # The name of the configuration file.
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
        # The name of the cache set.
        self.name = name
        # The path of the cache set.
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

