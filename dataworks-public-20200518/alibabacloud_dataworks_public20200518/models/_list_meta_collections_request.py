# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMetaCollectionsRequest(DaraModel):
    def __init__(
        self,
        administrator: str = None,
        collection_type: str = None,
        creator: str = None,
        follower: str = None,
        keyword: str = None,
        next_token: str = None,
        order_by: str = None,
        page_size: int = None,
        parent_qualified_name: str = None,
    ):
        # The ID of the collection administrator.
        self.administrator = administrator
        # - ALBUM: data album 
        # - ALBUM_CATEGORY: category in a data album
        # 
        # This parameter is required.
        self.collection_type = collection_type
        # The ID of the collection creator.
        self.creator = creator
        # The ID of the collection follower.
        self.follower = follower
        # The keyword.
        self.keyword = keyword
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The name of the sorting field.
        self.order_by = order_by
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The unique identifier of the parent collection.
        self.parent_qualified_name = parent_qualified_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.administrator is not None:
            result['Administrator'] = self.administrator

        if self.collection_type is not None:
            result['CollectionType'] = self.collection_type

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.follower is not None:
            result['Follower'] = self.follower

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.parent_qualified_name is not None:
            result['ParentQualifiedName'] = self.parent_qualified_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Administrator') is not None:
            self.administrator = m.get('Administrator')

        if m.get('CollectionType') is not None:
            self.collection_type = m.get('CollectionType')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('Follower') is not None:
            self.follower = m.get('Follower')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ParentQualifiedName') is not None:
            self.parent_qualified_name = m.get('ParentQualifiedName')

        return self

