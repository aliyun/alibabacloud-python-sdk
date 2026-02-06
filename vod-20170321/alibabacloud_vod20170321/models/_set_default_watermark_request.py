# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetDefaultWatermarkRequest(DaraModel):
    def __init__(
        self,
        watermark_id: str = None,
    ):
        # The ID of the watermark template. You can specify only one watermark template ID. You can obtain the ID by using one of the following methods:
        # 
        # *   Obtain the watermark template ID from the response to the [AddWatermark](~~AddWatermark~~) operation that you call to create a watermark template.
        # *   Obtain the watermark template ID from the response to the [ListWatermark](~~ListWatermark~~) operation that you call to query all watermark templates within your account.
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

