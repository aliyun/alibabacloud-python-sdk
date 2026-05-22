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
        # Content to be refreshed.
        self.content = content
        # Used for refreshing cached resources in edge computing, such as allowing the refresh of content cached using the CacheAPI interface of an edge function.
        self.edge_compute_purge = edge_compute_purge
        # Indicates whether to refresh all resources under the directory when the content from the origin and the source resource are inconsistent. The default is false.
        # - **true**: Refreshes all resources under the specified directory.
        # - **false**: Refreshes only the changed resources under the specified directory.
        # 
        # > 
        # >  Applies to: Directory refresh, cachetag refresh, ignoreParams refresh, hostname refresh, and purge all cache of the site.
        self.force = force
        # Site ID, which can be obtained by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) interface.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The type of refresh task. Possible values:
        # - **file** (default): File refresh.
        # - **cachekey**: Cachekey refresh.
        # - **cachetag**: Cachetag refresh.
        # - **directory**: Directory refresh.
        # - **ignoreParams**: Ignore parameters refresh. Ignoring parameters means removing the ? and everything after it in the request URL. When performing an ignore parameters refresh, the user first submits the URL without parameters through the interface. The submitted URLs to be refreshed will then be matched against the cached resource URLs with the parameters removed. If the cached resource URL, after removing the parameters, matches the URL to be refreshed, the CDN node will refresh the cached resources.
        # - **hostname**: Hostname refresh.
        # - **purgeall**: Purge all cache under the site.
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
        # List of cachekeys to be refreshed, required when the type is cachekey.
        self.cache_keys = cache_keys
        # List of cachetags to be refreshed, required when the type is cachetag.
        self.cache_tags = cache_tags
        # List of directories to be refreshed, required when the type is directory.
        self.directories = directories
        # List of files to be refreshed, required when the type is file.
        self.files = files
        # List of hostnames to be refreshed, required when the type is hostname.
        self.hostnames = hostnames
        # List of files with ignored parameters, required when the type is ignoreParams.
        self.ignore_params = ignore_params
        # Flag for purging all content. Default is false, set to true when the type is purgeall.
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
        # When refreshing, specify the header information corresponding to the cache key. When the custom cache key feature switch is enabled, the cache key will be generated based on the specified header for refreshing.
        # 
        # **UserGeo: Country/Region**
        # - Country/region codes follow the ISO 3166-2 standard.
        # 
        # **UserDeviceType: Device Type, currently there are three enum values**
        # - desktop
        #  - tablet
        #  - mobile
        # 
        # **UserLanguage: Language**
        # - Language codes follow the ISO 639-1 or BCP47 standards. For example, input \\"zh\\" to refresh content in Chinese.
        self.headers = headers
        # URL address to be refreshed.
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

