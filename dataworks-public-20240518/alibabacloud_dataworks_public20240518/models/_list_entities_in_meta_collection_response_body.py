# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListEntitiesInMetaCollectionResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.ListEntitiesInMetaCollectionResponseBodyPagingInfo = None,
        request_id: str = None,
    ):
        # The pagination result.
        self.paging_info = paging_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = main_models.ListEntitiesInMetaCollectionResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListEntitiesInMetaCollectionResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        entities: List[main_models.ListEntitiesInMetaCollectionResponseBodyPagingInfoEntities] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The list of entities in the collection.
        self.entities = entities
        # The current page number.
        self.page_number = page_number
        # The number of records per page.
        self.page_size = page_size
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.entities:
            for v1 in self.entities:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Entities'] = []
        if self.entities is not None:
            for k1 in self.entities:
                result['Entities'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.entities = []
        if m.get('Entities') is not None:
            for k1 in m.get('Entities'):
                temp_model = main_models.ListEntitiesInMetaCollectionResponseBodyPagingInfoEntities()
                self.entities.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListEntitiesInMetaCollectionResponseBodyPagingInfoEntities(DaraModel):
    def __init__(
        self,
        comment: str = None,
        create_time: int = None,
        description: str = None,
        id: str = None,
        modify_time: int = None,
        name: str = None,
        type: str = None,
    ):
        # The entity comment.
        self.comment = comment
        # The creation time in milliseconds.
        self.create_time = create_time
        # The description specified when the entity was added to the collection. Valid only for albums.
        self.description = description
        # The ID of the entity. Currently, only the Table type is supported. If the entity is deleted, this field is empty.
        self.id = id
        # The last modified time in milliseconds.
        self.modify_time = modify_time
        # The entity name.
        self.name = name
        # The entity type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

