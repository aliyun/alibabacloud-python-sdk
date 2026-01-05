# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMetaCollectionsRequest(DaraModel):
    def __init__(
        self,
        administrator: str = None,
        create_user: str = None,
        description: str = None,
        name: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        parent_id: str = None,
        sort_by: str = None,
        type: str = None,
    ):
        # The administrator ID. Valid only for album types. Default: The current user ID.
        self.administrator = administrator
        # The creator user ID. Valid only for album types. Default: The current user ID.
        self.create_user = create_user
        # The collection description. Supports fuzzy matching.
        self.description = description
        # The collection name. Supports fuzzy matching.
        self.name = name
        # The sort order. Valid values:
        # 
        # *   Asc (default): Ascending order
        # *   Desc
        self.order = order
        # The page number. Default: 1.
        self.page_number = page_number
        # The number of entries per page. Default: 10. Maximum: 100.
        self.page_size = page_size
        # The ID of the parent collection.
        self.parent_id = parent_id
        # The sort field. Valid values:
        # 
        # *   Id (default)
        # *   Name
        # *   CreateUser: Creator ID
        # *   CreateTime: Creation time
        # *   ModifyTime: Modification time
        self.sort_by = sort_by
        # The collection type. Valid values:
        # 
        # *   Category
        # *   Album
        # *   AlbumCategory: Album subcategory
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.administrator is not None:
            result['Administrator'] = self.administrator

        if self.create_user is not None:
            result['CreateUser'] = self.create_user

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Administrator') is not None:
            self.administrator = m.get('Administrator')

        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

