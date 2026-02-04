# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDataStorageTtlRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        log_store_cold_ttl: str = None,
        log_store_hot_ttl: str = None,
        log_store_name: str = None,
        log_store_ttl: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.lang = lang
        self.log_store_cold_ttl = log_store_cold_ttl
        self.log_store_hot_ttl = log_store_hot_ttl
        self.log_store_name = log_store_name
        self.log_store_ttl = log_store_ttl
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.log_store_cold_ttl is not None:
            result['LogStoreColdTtl'] = self.log_store_cold_ttl

        if self.log_store_hot_ttl is not None:
            result['LogStoreHotTtl'] = self.log_store_hot_ttl

        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name

        if self.log_store_ttl is not None:
            result['LogStoreTtl'] = self.log_store_ttl

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('LogStoreColdTtl') is not None:
            self.log_store_cold_ttl = m.get('LogStoreColdTtl')

        if m.get('LogStoreHotTtl') is not None:
            self.log_store_hot_ttl = m.get('LogStoreHotTtl')

        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')

        if m.get('LogStoreTtl') is not None:
            self.log_store_ttl = m.get('LogStoreTtl')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        return self

