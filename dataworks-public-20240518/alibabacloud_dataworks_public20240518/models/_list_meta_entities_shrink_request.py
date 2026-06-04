# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMetaEntitiesShrinkRequest(DaraModel):
    def __init__(
        self,
        attribute_filters_shrink: str = None,
        comment: str = None,
        custom_attribute_filters_shrink: str = None,
        entity_type: str = None,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        order: str = None,
        sort_by: str = None,
    ):
        self.attribute_filters_shrink = attribute_filters_shrink
        self.comment = comment
        self.custom_attribute_filters_shrink = custom_attribute_filters_shrink
        # This parameter is required.
        self.entity_type = entity_type
        self.max_results = max_results
        self.name = name
        self.next_token = next_token
        self.order = order
        self.sort_by = sort_by

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute_filters_shrink is not None:
            result['AttributeFilters'] = self.attribute_filters_shrink

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.custom_attribute_filters_shrink is not None:
            result['CustomAttributeFilters'] = self.custom_attribute_filters_shrink

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
        if m.get('AttributeFilters') is not None:
            self.attribute_filters_shrink = m.get('AttributeFilters')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CustomAttributeFilters') is not None:
            self.custom_attribute_filters_shrink = m.get('CustomAttributeFilters')

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

