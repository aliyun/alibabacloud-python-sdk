# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListSchemasRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        name: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        parent_meta_entity_id: str = None,
        sort_by: str = None,
        types: List[str] = None,
    ):
        # The comment. Fuzzy match is supported.
        self.comment = comment
        # The name. Fuzzy match is supported.
        self.name = name
        # The order in which schemas are sorted. Default value: Asc. Valid values:
        # 
        # *   Asc: ascending order
        # *   Desc: descending order
        self.order = order
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The parent entity ID. For more information, see [Concepts related to metadata entities](https://help.aliyun.com/document_detail/2880092.html). For the Hologres metadata crawler type, you can call the ListDatabases operation to query the settings of the `ParentMetaEntityId` parameter.
        # 
        # Configure the `ParentMetaEntityId` parameter in the `${EntityType}:${Instance ID or escaped URL}:${Catalog identifier}:${Database name}` format. If a level does not exist, leave the level empty.
        # 
        # >  If you want to query the information about a MaxCompute schema, specify an empty string at the Instance ID level as a placeholder and a MaxCompute project name at the Database name level. Make sure that the schema feature is enabled for the MaxCompute project.
        # 
        # This parameter is required.
        self.parent_meta_entity_id = parent_meta_entity_id
        # The field used for sorting. Default value: CreateTime. Valid values:
        # 
        # *   CreateTime
        # *   ModifyTime
        # *   Name
        # *   Type
        self.sort_by = sort_by
        # The types. Exact match is supported. If this parameter is left empty, all types are queried.
        self.types = types

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

        if self.types is not None:
            result['Types'] = self.types

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

        if m.get('Types') is not None:
            self.types = m.get('Types')

        return self

