# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenest20210601 import models as main_models
from darabonba.model import DaraModel

class ListPublicSkillsRequest(DaraModel):
    def __init__(
        self,
        filter: List[main_models.ListPublicSkillsRequestFilter] = None,
        max_results: int = None,
        need_download_url: bool = None,
        next_token: str = None,
    ):
        # A list of filters.
        self.filter = filter
        # The maximum number of entries to return on each page.
        self.max_results = max_results
        # Specifies whether to return the download link for the skill package.
        self.need_download_url = need_download_url
        # The token to retrieve the next page of results.
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

        if self.need_download_url is not None:
            result['NeedDownloadUrl'] = self.need_download_url

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k1 in m.get('Filter'):
                temp_model = main_models.ListPublicSkillsRequestFilter()
                self.filter.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NeedDownloadUrl') is not None:
            self.need_download_url = m.get('NeedDownloadUrl')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

class ListPublicSkillsRequestFilter(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: List[str] = None,
    ):
        # The filter criterion. Valid values:
        # 
        # - `SkillId`: The ID of the skill. An exact match is performed.
        # 
        # - `SkillName`: The name of the skill.
        # 
        # - `MatchType`: The match type for the `SkillName` filter. Valid values: `exact` (exact match), `prefix` (prefix match), and `fuzzy` (fuzzy match).
        # 
        # - `Keyword`: The keyword used for a fuzzy match on the skill name or skill description.
        # 
        # - `SkillLabels`: The skill labels. A fuzzy match is performed.
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

