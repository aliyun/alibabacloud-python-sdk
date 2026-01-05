# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDatabasesRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        name: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        parent_meta_entity_id: str = None,
        sort_by: str = None,
    ):
        # The comment. Supports fuzzy match.
        self.comment = comment
        # The name. Supports fuzzy match.
        self.name = name
        # The sort order. Default value: Asc. Valid values:
        # 
        # *   Asc: ascending.
        # *   Desc: descending.
        self.order = order
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of records per page. Default: 10. Maximum: 100.
        self.page_size = page_size
        # The parent entity ID. For more information, see [Concepts related to metadata entities](https://help.aliyun.com/document_detail/2880092.html).
        # 
        # You can refer to the ListCrawlerTypes operation for the parent entity type.
        # 
        # *   If the parent entity is a catalog, the format of `ParentMetaEntityId` follows the response of the ListCatalogs API.
        # *   If the parent entity is a metadata crawler, the format of `ParentMetaEntityId` is `${CrawlerType}:${Instance ID or encoded URL}`.
        # 
        # ParentMetaEntityId format examples
        # 
        # *   `dlf-catalog::catalog_id`
        # *   `holo:instance_id`
        # *   `mysql:(instance_id|encoded_jdbc_url)`
        # 
        # > 
        # 
        # *   `catalog_id`: The ID of the DLF catalog.
        # *   `instance_id`: The instance ID. Required when the data source is registered in instance mode.
        # *   `encoded_jdbc_url`: The URL-encoded JDBC connection string. Required when the data source is registered by connection string.
        # 
        # This parameter is required.
        self.parent_meta_entity_id = parent_meta_entity_id
        # The sort field. Default value: CreateTime. Valid values:
        # 
        # *   CreateTime
        # *   ModifyTime
        # *   Name
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

        if self.name is not None:
            result['Name'] = self.name

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.parent_meta_entity_id is not None:
            result['ParentMetaEntityId'] = self.parent_meta_entity_id

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ParentMetaEntityId') is not None:
            self.parent_meta_entity_id = m.get('ParentMetaEntityId')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        return self

