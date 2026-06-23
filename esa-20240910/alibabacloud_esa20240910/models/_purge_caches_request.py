# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any, Dict

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class PurgeCachesRequest(DaraModel):
    def __init__(
        self,
        content: main_models.PurgeCachesRequestContent = None,
        edge_compute_purge: bool = None,
        force: bool = None,
        site_id: int = None,
        type: str = None,
    ):
        # The refresh content.
        self.content = content
        # Specifies whether to refresh edge computing cached resources. For example, this allows you to refresh content cached by the Edge Routine CacheAPI API operation using the edge function.
        self.edge_compute_purge = edge_compute_purge
        # Specifies whether to refresh all resources under the corresponding directory when the back-to-origin content is inconsistent with the origin server resources. Default value: false.
        # - **true**: Refreshes all resources under the corresponding directory.
        # - **false**: Refreshes only the changed resources under the corresponding directory.
        # 
        # > 
        # >  This parameter takes effect for directory refresh, cache tag refresh, parameter-ignored refresh, hostname refresh, and full site refresh.
        self.force = force
        # The site ID, which can be obtained by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The type of the refresh node. Valid values:
        # - **file** (default): file refresh.
        # - **cachekey**: cache key refresh.
        # - **cachetag**: cache label refresh.
        # - **directory**: folder refresh.
        # - **ignoreParams**: parameter-ignored refresh. This refers to removing the question mark (?) and all parameters after it from the request URL. When you commit a parameter-stripped URL through this API operation, the committed URL is matched against cached resource URLs after their parameters are also stripped. If a cached resource URL matches the committed URL after parameter stripping, the point of presence executes the refresh on the cached resource.
        # - **hostname**: hostname refresh.
        # - **purgeall**: refreshes all cached content under the site.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content.to_map()

        if self.edge_compute_purge is not None:
            result['EdgeComputePurge'] = self.edge_compute_purge

        if self.force is not None:
            result['Force'] = self.force

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            temp_model = main_models.PurgeCachesRequestContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('EdgeComputePurge') is not None:
            self.edge_compute_purge = m.get('EdgeComputePurge')

        if m.get('Force') is not None:
            self.force = m.get('Force')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class PurgeCachesRequestContent(DaraModel):
    def __init__(
        self,
        cache_keys: List[main_models.PurgeCachesRequestContentCacheKeys] = None,
        cache_tags: List[str] = None,
        directories: List[str] = None,
        files: List[Any] = None,
        hostnames: List[str] = None,
        ignore_params: List[str] = None,
        purge_all: bool = None,
    ):
        # The list of cache keys to refresh. This parameter is required when Type is set to cachekey.
        self.cache_keys = cache_keys
        # The list of cache tags to refresh. This parameter is required when Type is set to cachetag.
        self.cache_tags = cache_tags
        # The list of directories to refresh. This parameter is required when Type is set to directory.
        self.directories = directories
        # The list of files to refresh. This parameter is required when Type is set to file.
        self.files = files
        # The list of hostnames to refresh. This parameter is required when Type is set to hostname.
        self.hostnames = hostnames
        # The list of files with parameters ignored. This parameter is required when Type is set to ignoreParams.
        self.ignore_params = ignore_params
        # Specifies whether to refresh the entire site. Default value: false. Set this parameter to true when Type is set to purgeall.
        self.purge_all = purge_all

    def validate(self):
        if self.cache_keys:
            for v1 in self.cache_keys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CacheKeys'] = []
        if self.cache_keys is not None:
            for k1 in self.cache_keys:
                result['CacheKeys'].append(k1.to_map() if k1 else None)

        if self.cache_tags is not None:
            result['CacheTags'] = self.cache_tags

        if self.directories is not None:
            result['Directories'] = self.directories

        if self.files is not None:
            result['Files'] = self.files

        if self.hostnames is not None:
            result['Hostnames'] = self.hostnames

        if self.ignore_params is not None:
            result['IgnoreParams'] = self.ignore_params

        if self.purge_all is not None:
            result['PurgeAll'] = self.purge_all

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cache_keys = []
        if m.get('CacheKeys') is not None:
            for k1 in m.get('CacheKeys'):
                temp_model = main_models.PurgeCachesRequestContentCacheKeys()
                self.cache_keys.append(temp_model.from_map(k1))

        if m.get('CacheTags') is not None:
            self.cache_tags = m.get('CacheTags')

        if m.get('Directories') is not None:
            self.directories = m.get('Directories')

        if m.get('Files') is not None:
            self.files = m.get('Files')

        if m.get('Hostnames') is not None:
            self.hostnames = m.get('Hostnames')

        if m.get('IgnoreParams') is not None:
            self.ignore_params = m.get('IgnoreParams')

        if m.get('PurgeAll') is not None:
            self.purge_all = m.get('PurgeAll')

        return self

class PurgeCachesRequestContentCacheKeys(DaraModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        url: str = None,
    ):
        # The header information corresponding to the cache key specified during the refresh. When the custom cache key feature is enabled, the cache key is generated based on the specified headers for the refresh.
        # 
        # **UserGeo: country/region**
        # 
        # - Country/region codes follow the ISO 3166-2 standard.
        # 
        # **UserDeviceType: device type. Valid values:**
        # 
        # - desktop
        # 
        # - tablet
        # 
        # - mobile
        # 
        # **UserLanguage: language**
        # 
        # - Language codes follow the ISO 639-1 or BCP 47 standard. For example, set this to zh to refresh content in Chinese.
        self.headers = headers
        # The URL to refresh.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.headers is not None:
            result['Headers'] = self.headers

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Headers') is not None:
            self.headers = m.get('Headers')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

