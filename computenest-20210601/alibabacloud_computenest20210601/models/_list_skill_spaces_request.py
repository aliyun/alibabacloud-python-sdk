# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenest20210601 import models as main_models
from darabonba.model import DaraModel

class ListSkillSpacesRequest(DaraModel):
    def __init__(
        self,
        filter: List[main_models.ListSkillSpacesRequestFilter] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The query filters.
        self.filter = filter
        # The number of entries to return per page. Maximum value: 100. Default value: 20.
        self.max_results = max_results
        # The token for the next page of results. To retrieve the next page, set this parameter to the `NextToken` value from the previous response.
        self.next_token = next_token

    def validate(self):
        if self.filter:
            for v1 in self.filter:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Filter'] = []
        if self.filter is not None:
            for k1 in self.filter:
                result['Filter'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k1 in m.get('Filter'):
                temp_model = main_models.ListSkillSpacesRequestFilter()
                self.filter.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

class ListSkillSpacesRequestFilter(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: List[str] = None,
    ):
        # The filter name. You can specify one or more filter names. Valid values:
        # 
        # - `SkillSpaceId`: The SkillSpace ID. This filter performs an exact match.
        # 
        # - `SkillSpaceName`: The SkillSpace name.
        # 
        # - `MatchType`: The match type for the `SkillSpaceName` filter. Valid values: `exact`, `prefix`, and `fuzzy`.
        self.name = name
        # The filter values. You can specify 1 to 10 values.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

