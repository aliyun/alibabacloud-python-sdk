# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAIImageInfosRequest(DaraModel):
    def __init__(
        self,
        aiimage_info_ids: str = None,
    ):
        # The IDs of the images that are submitted for AI processing. You can obtain the value of AIImageInfoId from the response to the [ListAIImageInfo](~~ListAIImageInfo~~) operation.
        # 
        # - You can specify a maximum of 10 IDs.
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

