# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RefreshDcdnObjectCacheByCacheTagRequest(DaraModel):
    def __init__(
        self,
        cache_tag: str = None,
        domain_name: str = None,
        force: bool = None,
    ):
        # This parameter is required.
        self.cache_tag = cache_tag
        # This parameter is required.
        self.domain_name = domain_name
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

