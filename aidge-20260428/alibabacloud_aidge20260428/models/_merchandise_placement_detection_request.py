# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MerchandisePlacementDetectionRequest(DaraModel):
    def __init__(
        self,
        api_id: str = None,
        image_url: str = None,
        rag_id: str = None,
        rule: str = None,
        type: str = None,
    ):
        # Specifies the ID of a custom API. Pass this parameter if you need to specify a custom version of the API. If you created a custom API during the trial phase, you can query the ApiId of the corresponding feature in the product console by choosing Intelligent Inspection > API Management > My APIs.
        self.api_id = api_id
        # The URL of the original shelf or floor display image to be recognized. The URL must be accessible over the Internet or from OSS.
        # 
        # This parameter is required.
        self.image_url = image_url
        # The ID of the customer-specific SKU vector database. This parameter determines which database is used for retrieval. The database must be created through the database creation process in advance.
        self.rag_id = rag_id
        # The custom rule. You can enter a detection prompt, which is passed as the rule input parameter to the workflow. If this parameter is specified, the type parameter is not required, and the independent rule branch is used. If this parameter is left empty, you must specify the type parameter to start detection.
        self.rule = rule
        # The business type. This parameter is reserved for future routing based on business lines. Currently, only skincare products are supported.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.rag_id is not None:
            result['RagId'] = self.rag_id

        if self.rule is not None:
            result['Rule'] = self.rule

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('RagId') is not None:
            self.rag_id = m.get('RagId')

        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

