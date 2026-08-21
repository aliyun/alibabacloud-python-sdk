# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteWatermarkRequest(DaraModel):
    def __init__(
        self,
        watermark_id: str = None,
    ):
        # The ID of the watermark template to delete. Only a single watermark template ID can be specified. You can obtain the ID by using the following methods:
        # - The ID is returned after you call the [AddWatermark](~~AddWatermark~~) operation to add a watermark template.
        # - The ID is returned after you call the [ListWatermark](~~ListWatermark~~) operation to query the list of watermark templates.
        # 
        # This parameter is required.
        self.watermark_id = watermark_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.watermark_id is not None:
            result['WatermarkId'] = self.watermark_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WatermarkId') is not None:
            self.watermark_id = m.get('WatermarkId')

        return self

