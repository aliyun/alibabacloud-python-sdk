# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RefreshErObjectCachesByCacheTagRequest(DaraModel):
    def __init__(
        self,
        cache_tag: str = None,
        domain: str = None,
        force: bool = None,
        merge_domain_name: str = None,
    ):
        # This parameter is required.
        self.cache_tag = cache_tag
        # This parameter is required.
        self.domain = domain
        self.force = force
        self.merge_domain_name = merge_domain_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cache_tag is not None:
            result['CacheTag'] = self.cache_tag

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.force is not None:
            result['Force'] = self.force

        if self.merge_domain_name is not None:
            result['MergeDomainName'] = self.merge_domain_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheTag') is not None:
            self.cache_tag = m.get('CacheTag')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Force') is not None:
            self.force = m.get('Force')

        if m.get('MergeDomainName') is not None:
            self.merge_domain_name = m.get('MergeDomainName')

        return self

