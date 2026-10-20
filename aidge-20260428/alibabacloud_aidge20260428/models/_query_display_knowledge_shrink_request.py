# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryDisplayKnowledgeShrinkRequest(DaraModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        rag_id: str = None,
        sku_id: str = None,
        sku_name: str = None,
        statuses_shrink: str = None,
    ):
        # The page number. Default value: 1.
        self.page_num = page_num
        # The number of entries per page. Default value: 20. Maximum value: 100.
        self.page_size = page_size
        # The knowledge base ID.
        # 
        # This parameter is required.
        self.rag_id = rag_id
        # The SKU ID for exact match.
        self.sku_id = sku_id
        # The keyword in the SKU name.
        self.sku_name = sku_name
        # The list of record statuses. Valid values: UPDATING, EMBEDDED, and FAILED.
        self.statuses_shrink = statuses_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.rag_id is not None:
            result['RagId'] = self.rag_id

        if self.sku_id is not None:
            result['SkuId'] = self.sku_id

        if self.sku_name is not None:
            result['SkuName'] = self.sku_name

        if self.statuses_shrink is not None:
            result['Statuses'] = self.statuses_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RagId') is not None:
            self.rag_id = m.get('RagId')

        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')

        if m.get('SkuName') is not None:
            self.sku_name = m.get('SkuName')

        if m.get('Statuses') is not None:
            self.statuses_shrink = m.get('Statuses')

        return self

