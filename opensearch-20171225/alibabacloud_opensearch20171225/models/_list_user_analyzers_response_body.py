# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class ListUserAnalyzersResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.ListUserAnalyzersResponseBodyResult] = None,
        total_count: int = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The custom analyzer.
        # 
        # For more information, see [UserAnalyzer](https://help.aliyun.com/document_detail/178934.html).
        self.result = result
        # The total number.
        self.total_count = total_count

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['result'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.result = []
        if m.get('result') is not None:
            for k1 in m.get('result'):
                temp_model = main_models.ListUserAnalyzersResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListUserAnalyzersResponseBodyResult(DaraModel):
    def __init__(
        self,
        available: bool = None,
        business: str = None,
        created: int = None,
        dicts: List[main_models.ListUserAnalyzersResponseBodyResultDicts] = None,
        id: str = None,
        name: str = None,
        updated: int = None,
    ):
        # Indicates whether the application is available.
        self.available = available
        # The basic analyzer. Valid values:
        # 
        # *   chn_standard: [a common analyzer in Chinese](https://help.aliyun.com/document_detail/179424.html)
        # *   chn_scene_name: an analyzer for person names in Chinese
        # *   chn_ecommerce: [an analyzer for E-commerce in Chinese](https://help.aliyun.com/document_detail/179424.html)
        # *   chn_it_content: [an analyzer for IT content in Chinese](https://help.aliyun.com/document_detail/179424.html)
        # *   en_min: a small-granularity analyzer in English
        # *   th_standard: a common analyzer in Thai
        # *   th_ecommerce: an analyzer for E-commerce in Thai
        # *   vn_standard: a common analyzer in Vietnamese
        # *   chn_community_it: an analyzer for IT community content in Chinese
        # *   chn_ecommerce_general: a common analyzer for the E-commerce industry in Chinese
        # *   chn_esports_general: a common analyzer for the gaming industry in Chinese
        # *   chn_edu_question: an analyzer for question search of the education industry in Chinese
        self.business = business
        # The timestamp when the application was created.
        self.created = created
        # The dictionaries that are used by the custom analyzer.
        # 
        # For more information, see [UserDict](https://help.aliyun.com/document_detail/178933.html).
        self.dicts = dicts
        # The ID of the custom analyzer.
        self.id = id
        # The name of the custom analyzer.
        self.name = name
        # The timestamp when the application was last updated.
        self.updated = updated

    def validate(self):
        if self.dicts:
            for v1 in self.dicts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available is not None:
            result['available'] = self.available

        if self.business is not None:
            result['business'] = self.business

        if self.created is not None:
            result['created'] = self.created

        result['dicts'] = []
        if self.dicts is not None:
            for k1 in self.dicts:
                result['dicts'].append(k1.to_map() if k1 else None)

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.updated is not None:
            result['updated'] = self.updated

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('available') is not None:
            self.available = m.get('available')

        if m.get('business') is not None:
            self.business = m.get('business')

        if m.get('created') is not None:
            self.created = m.get('created')

        self.dicts = []
        if m.get('dicts') is not None:
            for k1 in m.get('dicts'):
                temp_model = main_models.ListUserAnalyzersResponseBodyResultDicts()
                self.dicts.append(temp_model.from_map(k1))

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('updated') is not None:
            self.updated = m.get('updated')

        return self

class ListUserAnalyzersResponseBodyResultDicts(DaraModel):
    def __init__(
        self,
        available: bool = None,
        created: int = None,
        entries_count: int = None,
        entries_limit: int = None,
        id: str = None,
        type: str = None,
        updated: int = None,
    ):
        # Indicates whether the application is available.
        self.available = available
        # The timestamp when the application was created.
        self.created = created
        # The number of intervention entries.
        self.entries_count = entries_count
        # The maximum number of intervention entries that can be created in the dictionary.
        self.entries_limit = entries_limit
        # The ID of the dictionary.
        self.id = id
        # The type. Valid value:
        # 
        # *   segment
        self.type = type
        # The timestamp when the application was last updated.
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available is not None:
            result['available'] = self.available

        if self.created is not None:
            result['created'] = self.created

        if self.entries_count is not None:
            result['entriesCount'] = self.entries_count

        if self.entries_limit is not None:
            result['entriesLimit'] = self.entries_limit

        if self.id is not None:
            result['id'] = self.id

        if self.type is not None:
            result['type'] = self.type

        if self.updated is not None:
            result['updated'] = self.updated

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('available') is not None:
            self.available = m.get('available')

        if m.get('created') is not None:
            self.created = m.get('created')

        if m.get('entriesCount') is not None:
            self.entries_count = m.get('entriesCount')

        if m.get('entriesLimit') is not None:
            self.entries_limit = m.get('entriesLimit')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('updated') is not None:
            self.updated = m.get('updated')

        return self

