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
        # Specify this parameter to use a custom API version. If you created a custom API during the trial phase, you can find the corresponding ApiId in the product console under Intelligent Inspection > API Management > My API.
        self.api_id = api_id
        # The URL of the original shelf or floor stack image to be recognized (accessible over the Internet or through OSS).
        # 
        # This parameter is required.
        self.image_url = image_url
        # The ID of the customer-specific SKU vector library, which determines which library is used for retrieval. The library must be created in advance through the library creation process.
        self.rag_id = rag_id
        # The custom rule. Enter a detection prompt as the workflow input parameter rule. When this parameter is specified, the type parameter is not required (a dedicated rule branch is used). If Rule is empty, you must specify Type to start detection.
        self.rule = rule
        # The business type (reserved for future routing by business line). The current release supports skincare & lotion.
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

