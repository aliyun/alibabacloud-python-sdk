# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListEntitiesInMetaCollectionRequest(DaraModel):
    def __init__(
        self,
        entity_description: str = None,
        entity_name: str = None,
        entity_type: str = None,
        id: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        sort_by: str = None,
    ):
        # The description specified when the entity was added to the collection. Supports fuzzy matching. Valid only for the album type.
        self.entity_description = entity_description
        # The entity name. Supports fuzzy matching.
        self.entity_name = entity_name
        # The entity type.
        self.entity_type = entity_type
        # The collection ID.
        # 
        # This parameter is required.
        self.id = id
        # The sort order. Valid values:
        # 
        # *   Asc (default): ascending order.
        # *   Desc
        self.order = order
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of records per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The sort field. Valid values:
        # 
        # *   Name (default)
        # *   CreateTime
        self.sort_by = sort_by

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity_description is not None:
            result['EntityDescription'] = self.entity_description

        if self.entity_name is not None:
            result['EntityName'] = self.entity_name

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.id is not None:
            result['Id'] = self.id

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
        if m.get('EntityDescription') is not None:
            self.entity_description = m.get('EntityDescription')

        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        return self

