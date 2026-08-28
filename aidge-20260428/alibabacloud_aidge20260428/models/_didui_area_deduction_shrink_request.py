# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DiduiAreaDeductionShrinkRequest(DaraModel):
    def __init__(
        self,
        products_shrink: str = None,
        rag_id: str = None,
        req_id: str = None,
        target_image_url: str = None,
    ):
        # The list of products and their detection boxes.
        # 
        # This parameter is required.
        self.products_shrink = products_shrink
        # The ID of the customer-specific SKU vector store that determines which store is used for retrieval. The store must be created in advance through the store creation process.
        self.rag_id = rag_id
        # The optional business request ID used for Tracing Analysis.
        self.req_id = req_id
        # The HTTPS URL of the overall floor display image.
        # 
        # This parameter is required.
        self.target_image_url = target_image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.products_shrink is not None:
            result['Products'] = self.products_shrink

        if self.rag_id is not None:
            result['RagId'] = self.rag_id

        if self.req_id is not None:
            result['ReqId'] = self.req_id

        if self.target_image_url is not None:
            result['TargetImageUrl'] = self.target_image_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Products') is not None:
            self.products_shrink = m.get('Products')

        if m.get('RagId') is not None:
            self.rag_id = m.get('RagId')

        if m.get('ReqId') is not None:
            self.req_id = m.get('ReqId')

        if m.get('TargetImageUrl') is not None:
            self.target_image_url = m.get('TargetImageUrl')

        return self

