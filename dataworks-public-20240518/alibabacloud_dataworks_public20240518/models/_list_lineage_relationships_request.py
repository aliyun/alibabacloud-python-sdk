# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListLineageRelationshipsRequest(DaraModel):
    def __init__(
        self,
        dst_entity_id: str = None,
        dst_entity_name: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        sort_by: str = None,
        src_entity_id: str = None,
        src_entity_name: str = None,
    ):
        # The ID of the destination entity. You can refer to the table or field ID returned by the ListTables or ListColumns operation, or use a custom entity ID.
        # 
        # This parameter is required.
        self.dst_entity_id = dst_entity_id
        # The name of the destination entity. Fuzzy match is supported.
        self.dst_entity_name = dst_entity_name
        # The sort order. Default value: Asc. Valid values:
        # 
        # - Asc: ascending order.
        # - Desc: descending order.
        self.order = order
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The field used for sorting. Default value: Name.
        self.sort_by = sort_by
        # The ID of the source entity. You can refer to the table or field ID returned by the ListTables or ListColumns operation, or use a custom entity ID.
        # 
        # To obtain the entity ID of a table or field, first call ListCrawlers to obtain the MetaEntityId of the metadata crawler. For types that include a data catalog hierarchy, such as DLF and StarRocks, call ListCatalogs to obtain the catalog ID. Then, call ListDatabases to obtain the database ID, and call ListSchemas to obtain the schema ID if necessary. Finally, call ListTables or ListColumns to obtain the table or field ID.
        # 
        # This parameter is required.
        self.src_entity_id = src_entity_id
        # The name of the source entity. Fuzzy match is supported.
        self.src_entity_name = src_entity_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dst_entity_id is not None:
            result['DstEntityId'] = self.dst_entity_id

        if self.dst_entity_name is not None:
            result['DstEntityName'] = self.dst_entity_name

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.src_entity_id is not None:
            result['SrcEntityId'] = self.src_entity_id

        if self.src_entity_name is not None:
            result['SrcEntityName'] = self.src_entity_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DstEntityId') is not None:
            self.dst_entity_id = m.get('DstEntityId')

        if m.get('DstEntityName') is not None:
            self.dst_entity_name = m.get('DstEntityName')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('SrcEntityId') is not None:
            self.src_entity_id = m.get('SrcEntityId')

        if m.get('SrcEntityName') is not None:
            self.src_entity_name = m.get('SrcEntityName')

        return self

