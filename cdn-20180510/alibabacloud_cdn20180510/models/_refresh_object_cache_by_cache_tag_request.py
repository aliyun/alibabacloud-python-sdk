# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RefreshObjectCacheByCacheTagRequest(DaraModel):
    def __init__(
        self,
        cache_tag: str = None,
        domain_name: str = None,
        force: bool = None,
    ):
        # The tags of Cache. If multiple tags are returned, the tags are separated by commas (,).
        # 
        # This parameter is required.
        self.cache_tag = cache_tag
        # The accelerated domain name.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # Specifies whether to purge all resources that you submit if the requested content is one of the resources that you submit to purge. Default value: false.
        # 
        # *   **true**: The nearest POP fetches all resources from the origin server, delivers them to the client, and updates the cache with the new version.
        # *   **false**: The nearest POP checks the Last-Modified parameter of the resource on the origin server. If the parameter value is the same as that of the cached resource, the POP serves the cached resource. If the parameter value is not the same as that of the cached resource, the POP fetches the latest version from the origin server, delivers it to the client, and updates the cache with the new version.
        self.force = force

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cache_tag is not None:
            result['CacheTag'] = self.cache_tag

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.force is not None:
            result['Force'] = self.force

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheTag') is not None:
            self.cache_tag = m.get('CacheTag')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Force') is not None:
            self.force = m.get('Force')

        return self

