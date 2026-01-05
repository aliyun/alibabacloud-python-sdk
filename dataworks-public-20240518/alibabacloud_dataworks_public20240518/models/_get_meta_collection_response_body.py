# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetMetaCollectionResponseBody(DaraModel):
    def __init__(
        self,
        meta_collection: main_models.GetMetaCollectionResponseBodyMetaCollection = None,
        request_id: str = None,
    ):
        # The collection details.
        self.meta_collection = meta_collection
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.meta_collection:
            self.meta_collection.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.meta_collection is not None:
            result['MetaCollection'] = self.meta_collection.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetaCollection') is not None:
            temp_model = main_models.GetMetaCollectionResponseBodyMetaCollection()
            self.meta_collection = temp_model.from_map(m.get('MetaCollection'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetMetaCollectionResponseBodyMetaCollection(DaraModel):
    def __init__(
        self,
        administrators: List[int] = None,
        create_time: int = None,
        create_user: str = None,
        description: str = None,
        id: str = None,
        modify_time: int = None,
        name: str = None,
        parent_id: str = None,
        type: str = None,
    ):
        # The list of administrator IDs. Valid only for the album type. The IDs must belong to users in the same tenant. Multiple IDs can be specified.
        self.administrators = administrators
        # The creation time in milliseconds.
        self.create_time = create_time
        # The ID of the creator.
        self.create_user = create_user
        # The collection description.
        self.description = description
        # The collection ID.
        self.id = id
        # The last modified time in milliseconds.
        self.modify_time = modify_time
        # The collection name.
        self.name = name
        # The parent collection ID. This parameter can be empty.
        self.parent_id = parent_id
        # The collection type. Valid values:
        # 
        # *   Category
        # *   Album
        # *   AlbumCategory: Album subcategory.
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

