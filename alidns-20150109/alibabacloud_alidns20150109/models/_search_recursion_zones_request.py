# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class SearchRecursionZonesRequest(DaraModel):
    def __init__(
        self,
        direction: str = None,
        effective_scopes: List[main_models.SearchRecursionZonesRequestEffectiveScopes] = None,
        max_results: int = None,
        next_token: str = None,
        order_by: str = None,
        page_number: int = None,
        page_size: int = None,
        remark: str = None,
        zone_name: str = None,
    ):
        self.direction = direction
        self.effective_scopes = effective_scopes
        self.max_results = max_results
        self.next_token = next_token
        self.order_by = order_by
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size
        self.remark = remark
        self.zone_name = zone_name

    def validate(self):
        if self.effective_scopes:
            for v1 in self.effective_scopes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.direction is not None:
            result['Direction'] = self.direction

        result['EffectiveScopes'] = []
        if self.effective_scopes is not None:
            for k1 in self.effective_scopes:
                result['EffectiveScopes'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        self.effective_scopes = []
        if m.get('EffectiveScopes') is not None:
            for k1 in m.get('EffectiveScopes'):
                temp_model = main_models.SearchRecursionZonesRequestEffectiveScopes()
                self.effective_scopes.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')

        return self

class SearchRecursionZonesRequestEffectiveScopes(DaraModel):
    def __init__(
        self,
        effective_type: str = None,
        scope: List[str] = None,
    ):
        self.effective_type = effective_type
        self.scope = scope

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.effective_type is not None:
            result['EffectiveType'] = self.effective_type

        if self.scope is not None:
            result['Scope'] = self.scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EffectiveType') is not None:
            self.effective_type = m.get('EffectiveType')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        return self

