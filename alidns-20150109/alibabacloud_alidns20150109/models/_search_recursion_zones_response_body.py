# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class SearchRecursionZonesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_items: int = None,
        total_pages: int = None,
        zones: main_models.SearchRecursionZonesResponseBodyZones = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_items = total_items
        self.total_pages = total_pages
        self.zones = zones

    def validate(self):
        if self.zones:
            self.zones.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_items is not None:
            result['TotalItems'] = self.total_items

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        if self.zones is not None:
            result['Zones'] = self.zones.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        if m.get('Zones') is not None:
            temp_model = main_models.SearchRecursionZonesResponseBodyZones()
            self.zones = temp_model.from_map(m.get('Zones'))

        return self

class SearchRecursionZonesResponseBodyZones(DaraModel):
    def __init__(
        self,
        zone: List[main_models.SearchRecursionZonesResponseBodyZonesZone] = None,
    ):
        self.zone = zone

    def validate(self):
        if self.zone:
            for v1 in self.zone:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Zone'] = []
        if self.zone is not None:
            for k1 in self.zone:
                result['Zone'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.zone = []
        if m.get('Zone') is not None:
            for k1 in m.get('Zone'):
                temp_model = main_models.SearchRecursionZonesResponseBodyZonesZone()
                self.zone.append(temp_model.from_map(k1))

        return self

class SearchRecursionZonesResponseBodyZonesZone(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        create_timestamp: int = None,
        creator: str = None,
        creator_sub_type: str = None,
        creator_type: str = None,
        effective_scopes: main_models.SearchRecursionZonesResponseBodyZonesZoneEffectiveScopes = None,
        proxy_pattern: str = None,
        record_count: int = None,
        remark: str = None,
        update_time: str = None,
        update_timestamp: int = None,
        zone_id: str = None,
        zone_name: str = None,
    ):
        self.create_time = create_time
        self.create_timestamp = create_timestamp
        self.creator = creator
        self.creator_sub_type = creator_sub_type
        self.creator_type = creator_type
        self.effective_scopes = effective_scopes
        self.proxy_pattern = proxy_pattern
        self.record_count = record_count
        self.remark = remark
        self.update_time = update_time
        self.update_timestamp = update_timestamp
        self.zone_id = zone_id
        self.zone_name = zone_name

    def validate(self):
        if self.effective_scopes:
            self.effective_scopes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.creator_sub_type is not None:
            result['CreatorSubType'] = self.creator_sub_type

        if self.creator_type is not None:
            result['CreatorType'] = self.creator_type

        if self.effective_scopes is not None:
            result['EffectiveScopes'] = self.effective_scopes.to_map()

        if self.proxy_pattern is not None:
            result['ProxyPattern'] = self.proxy_pattern

        if self.record_count is not None:
            result['RecordCount'] = self.record_count

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('CreatorSubType') is not None:
            self.creator_sub_type = m.get('CreatorSubType')

        if m.get('CreatorType') is not None:
            self.creator_type = m.get('CreatorType')

        if m.get('EffectiveScopes') is not None:
            temp_model = main_models.SearchRecursionZonesResponseBodyZonesZoneEffectiveScopes()
            self.effective_scopes = temp_model.from_map(m.get('EffectiveScopes'))

        if m.get('ProxyPattern') is not None:
            self.proxy_pattern = m.get('ProxyPattern')

        if m.get('RecordCount') is not None:
            self.record_count = m.get('RecordCount')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')

        return self

class SearchRecursionZonesResponseBodyZonesZoneEffectiveScopes(DaraModel):
    def __init__(
        self,
        effective_scope: List[main_models.SearchRecursionZonesResponseBodyZonesZoneEffectiveScopesEffectiveScope] = None,
    ):
        self.effective_scope = effective_scope

    def validate(self):
        if self.effective_scope:
            for v1 in self.effective_scope:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EffectiveScope'] = []
        if self.effective_scope is not None:
            for k1 in self.effective_scope:
                result['EffectiveScope'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.effective_scope = []
        if m.get('EffectiveScope') is not None:
            for k1 in m.get('EffectiveScope'):
                temp_model = main_models.SearchRecursionZonesResponseBodyZonesZoneEffectiveScopesEffectiveScope()
                self.effective_scope.append(temp_model.from_map(k1))

        return self

class SearchRecursionZonesResponseBodyZonesZoneEffectiveScopesEffectiveScope(DaraModel):
    def __init__(
        self,
        effective_type: str = None,
        scopes: main_models.SearchRecursionZonesResponseBodyZonesZoneEffectiveScopesEffectiveScopeScopes = None,
    ):
        self.effective_type = effective_type
        self.scopes = scopes

    def validate(self):
        if self.scopes:
            self.scopes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.effective_type is not None:
            result['EffectiveType'] = self.effective_type

        if self.scopes is not None:
            result['Scopes'] = self.scopes.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EffectiveType') is not None:
            self.effective_type = m.get('EffectiveType')

        if m.get('Scopes') is not None:
            temp_model = main_models.SearchRecursionZonesResponseBodyZonesZoneEffectiveScopesEffectiveScopeScopes()
            self.scopes = temp_model.from_map(m.get('Scopes'))

        return self

class SearchRecursionZonesResponseBodyZonesZoneEffectiveScopesEffectiveScopeScopes(DaraModel):
    def __init__(
        self,
        scope: List[str] = None,
    ):
        self.scope = scope

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scope is not None:
            result['Scope'] = self.scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        return self

