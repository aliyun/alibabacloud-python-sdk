# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCustomAttributesRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        display_name: str = None,
        entity_types: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        sort_by: str = None,
    ):
        # The comment on the custom attribute. The service performs a fuzzy search based on this parameter\\"s value.
        self.comment = comment
        # The display name of the custom attribute. The service performs a partial match based on this parameter\\"s value.
        self.display_name = display_name
        # The entity types to which the custom attribute applies. To specify multiple entity types, separate them with commas (,), for example, `*-table,*-column`. This parameter supports specific entity types, such as `hms-table` and `emr-table`, and wildcard types, such as `*-table` and `*-column`.
        self.entity_types = entity_types
        # The sort order. Valid values: Asc and Desc.
        self.order = order
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The field to sort by. Valid values: CreateTime and ModifyTime.
        self.sort_by = sort_by

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.entity_types is not None:
            result['EntityTypes'] = self.entity_types

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('EntityTypes') is not None:
            self.entity_types = m.get('EntityTypes')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        return self

