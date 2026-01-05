# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListMetaCollectionsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListMetaCollectionsResponseBodyData = None,
        request_id: str = None,
    ):
        # Pagination information.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListMetaCollectionsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListMetaCollectionsResponseBodyData(DaraModel):
    def __init__(
        self,
        meta_collections: List[main_models.ListMetaCollectionsResponseBodyDataMetaCollections] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The list of collections.
        self.meta_collections = meta_collections
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.meta_collections:
            for v1 in self.meta_collections:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MetaCollections'] = []
        if self.meta_collections is not None:
            for k1 in self.meta_collections:
                result['MetaCollections'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.meta_collections = []
        if m.get('MetaCollections') is not None:
            for k1 in m.get('MetaCollections'):
                temp_model = main_models.ListMetaCollectionsResponseBodyDataMetaCollections()
                self.meta_collections.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListMetaCollectionsResponseBodyDataMetaCollections(DaraModel):
    def __init__(
        self,
        administrators: List[str] = None,
        create_time: int = None,
        create_user: str = None,
        description: str = None,
        id: str = None,
        modify_time: int = None,
        name: str = None,
        parent_id: str = None,
        type: str = None,
    ):
        # The list of administrator IDs. Supported only for album types. Administrators must be users within the same tenant. Multiple administrators can be specified.
        self.administrators = administrators
        # The creation time in milliseconds (timestamp).
        self.create_time = create_time
        # The creator user ID.
        self.create_user = create_user
        # The collection description.
        self.description = description
        # The collection name.
        self.id = id
        # The modification time in milliseconds (timestamp).
        self.modify_time = modify_time
        # The collection name.
        self.name = name
        # The ID of the parent collection. Can be empty.
        self.parent_id = parent_id
        # The collection type. Valid values:
        # 
        # *   Category
        # *   Album
        # *   AlbumCategory: Album subcategory
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.administrators is not None:
            result['Administrators'] = self.administrators

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user is not None:
            result['CreateUser'] = self.create_user

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Administrators') is not None:
            self.administrators = m.get('Administrators')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

