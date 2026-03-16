# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenest20210601 import models as main_models
from darabonba.model import DaraModel

class ListServicesRequest(DaraModel):
    def __init__(
        self,
        filter: List[main_models.ListServicesRequestFilter] = None,
        fuzzy_keyword: str = None,
        in_used: bool = None,
        max_results: int = None,
        next_token: str = None,
        order_by_type: str = None,
        region_id: str = None,
        service_access_type: str = None,
        tag: List[main_models.ListServicesRequestTag] = None,
    ):
        # The filter.
        self.filter = filter
        # Keyword fuzzy query.
        self.fuzzy_keyword = fuzzy_keyword
        # Whether it is used. Optional values:
        # 
        # 
        # 
        # - false: not being used.
        # 
        # 
        # 
        # - true: already in use.
        self.in_used = in_used
        # The number of entries page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # Service ordering type.
        self.order_by_type = order_by_type
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Service access type.
        self.service_access_type = service_access_type
        # The tags.
        self.tag = tag

    def validate(self):
        if self.filter:
            for v1 in self.filter:
                 if v1:
                    v1.validate()
        if self.tag:
            for v1 in self.tag:
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

        if self.fuzzy_keyword is not None:
            result['FuzzyKeyword'] = self.fuzzy_keyword

        if self.in_used is not None:
            result['InUsed'] = self.in_used

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.order_by_type is not None:
            result['OrderByType'] = self.order_by_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_access_type is not None:
            result['ServiceAccessType'] = self.service_access_type

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k1 in m.get('Filter'):
                temp_model = main_models.ListServicesRequestFilter()
                self.filter.append(temp_model.from_map(k1))

        if m.get('FuzzyKeyword') is not None:
            self.fuzzy_keyword = m.get('FuzzyKeyword')

        if m.get('InUsed') is not None:
            self.in_used = m.get('InUsed')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OrderByType') is not None:
            self.order_by_type = m.get('OrderByType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceAccessType') is not None:
            self.service_access_type = m.get('ServiceAccessType')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListServicesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class ListServicesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListServicesRequestFilter(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: List[str] = None,
    ):
        # The parameter name of the filter. You can specify one or more parameter names to query services. Valid values:
        # 
        # *   ServiceId: the ID of the service.
        # *   Name: the name of the service.
        # *   Status: the state of the service.
        # *   SupplierName: the name of the service provider.
        self.name = name
        # A value of the filter condition.
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

