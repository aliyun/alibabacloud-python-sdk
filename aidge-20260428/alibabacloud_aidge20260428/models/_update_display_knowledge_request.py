# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aidge20260428 import models as main_models
from darabonba.model import DaraModel

class UpdateDisplayKnowledgeRequest(DaraModel):
    def __init__(
        self,
        rag_id: str = None,
        records: List[main_models.UpdateDisplayKnowledgeRequestRecords] = None,
    ):
        # The knowledge base ID.
        # 
        # This parameter is required.
        self.rag_id = rag_id
        # The records to update. A maximum of 500 records can be specified.
        # 
        # This parameter is required.
        self.records = records

    def validate(self):
        if self.records:
            for v1 in self.records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rag_id is not None:
            result['RagId'] = self.rag_id

        result['Records'] = []
        if self.records is not None:
            for k1 in self.records:
                result['Records'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RagId') is not None:
            self.rag_id = m.get('RagId')

        self.records = []
        if m.get('Records') is not None:
            for k1 in m.get('Records'):
                temp_model = main_models.UpdateDisplayKnowledgeRequestRecords()
                self.records.append(temp_model.from_map(k1))

        return self

class UpdateDisplayKnowledgeRequestRecords(DaraModel):
    def __init__(
        self,
        image_url: str = None,
        record_id: int = None,
        sku_id: str = None,
        sku_name: str = None,
    ):
        # The HTTP or HTTPS URL of the product image.
        self.image_url = image_url
        # The record ID.
        self.record_id = record_id
        # The SKU ID. If this parameter is not empty, the original value is overwritten.
        self.sku_id = sku_id
        # The SKU name.
        self.sku_name = sku_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        if self.sku_id is not None:
            result['SkuId'] = self.sku_id

        if self.sku_name is not None:
            result['SkuName'] = self.sku_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')

        if m.get('SkuName') is not None:
            self.sku_name = m.get('SkuName')

        return self

