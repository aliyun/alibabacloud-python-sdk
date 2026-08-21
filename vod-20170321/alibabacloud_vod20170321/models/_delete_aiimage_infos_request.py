# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAIImageInfosRequest(DaraModel):
    def __init__(
        self,
        aiimage_info_ids: str = None,
    ):
        # The IDs of AI image information. This parameter consists of one or more AIImageInfoId values. The AIImageInfoId is the value of the AIImageInfoId response parameter returned by the [ListAIImageInfo](https://help.aliyun.com/document_detail/186924.html) operation.
        # - A maximum of 10 IDs are supported.
        # - Separate multiple IDs with commas (,).
        # 
        # This parameter is required.
        self.aiimage_info_ids = aiimage_info_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aiimage_info_ids is not None:
            result['AIImageInfoIds'] = self.aiimage_info_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AIImageInfoIds') is not None:
            self.aiimage_info_ids = m.get('AIImageInfoIds')

        return self

