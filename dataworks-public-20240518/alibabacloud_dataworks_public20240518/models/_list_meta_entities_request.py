# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListMetaEntitiesRequest(DaraModel):
    def __init__(
        self,
        attribute_filters: List[main_models.ListMetaEntitiesRequestAttributeFilters] = None,
        comment: str = None,
        custom_attribute_filters: List[main_models.ListMetaEntitiesRequestCustomAttributeFilters] = None,
        entity_type: str = None,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        order: str = None,
        sort_by: str = None,
    ):
        # Conditions for filtering entities by entity attributes. The `AND` operator is used between different filters, and the `OR` operator is used for multiple values within a single filter.
        self.attribute_filters = attribute_filters
        # Filters entities by comment. This is a token-based match.
        self.comment = comment
        # Conditions for filtering entities by custom attributes. The `AND` operator is used between different filters, and the `OR` operator is used for multiple values within a single filter. This parameter supports only `ENUM` custom attributes.
        self.custom_attribute_filters = custom_attribute_filters
        # The type of the entity to list.
        # 
        # This parameter is required.
        self.entity_type = entity_type
        # The maximum number of results to return per page. Default value: 10. Maximum value: 100.
        self.max_results = max_results
        # Filters entities by name. This is a containment match.
        self.name = name
        # The pagination token that specifies the next page of results. To retrieve the first page, do not specify this parameter. To retrieve subsequent pages, set this parameter to the `NextToken` value from the previous response.
        self.next_token = next_token
        # The sort order. Valid values: `Asc` and `Desc`.
        self.order = order
        # The field to use for sorting the results.
        self.sort_by = sort_by

    def validate(self):
        if self.attribute_filters:
            for v1 in self.attribute_filters:
                 if v1:
                    v1.validate()
        if self.custom_attribute_filters:
            for v1 in self.custom_attribute_filters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AttributeFilters'] = []
        if self.attribute_filters is not None:
            for k1 in self.attribute_filters:
                result['AttributeFilters'].append(k1.to_map() if k1 else None)

        if self.comment is not None:
            result['Comment'] = self.comment

        result['CustomAttributeFilters'] = []
        if self.custom_attribute_filters is not None:
            for k1 in self.custom_attribute_filters:
                result['CustomAttributeFilters'].append(k1.to_map() if k1 else None)

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.name is not None:
            result['Name'] = self.name

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.order is not None:
            result['Order'] = self.order

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attribute_filters = []
        if m.get('AttributeFilters') is not None:
            for k1 in m.get('AttributeFilters'):
                temp_model = main_models.ListMetaEntitiesRequestAttributeFilters()
                self.attribute_filters.append(temp_model.from_map(k1))

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        self.custom_attribute_filters = []
        if m.get('CustomAttributeFilters') is not None:
            for k1 in m.get('CustomAttributeFilters'):
                temp_model = main_models.ListMetaEntitiesRequestCustomAttributeFilters()
                self.custom_attribute_filters.append(temp_model.from_map(k1))

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        return self

class ListMetaEntitiesRequestCustomAttributeFilters(DaraModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        # The key of the custom attribute to filter by.
        # 
        # This parameter is required.
        self.key = key
        # A list of values for the specified custom attribute.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

class ListMetaEntitiesRequestAttributeFilters(DaraModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        # The key of the entity attribute to filter by.
        # 
        # This parameter is required.
        self.key = key
        # A list of values for the specified entity attribute.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

