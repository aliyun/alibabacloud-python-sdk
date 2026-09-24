# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DiduiAreaDeductionProRequest(DaraModel):
    def __init__(
        self,
        image_url: str = None,
        rag_id: str = None,
    ):
        # The HTTP(S) URL of the overall floor display image.
        # 
        # This parameter is required.
        self.image_url = image_url
        # The ID of the SKU asset knowledge base.
        # 
        # This parameter is required.
        self.rag_id = rag_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.rag_id is not None:
            result['RagId'] = self.rag_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('RagId') is not None:
            self.rag_id = m.get('RagId')

        return self

