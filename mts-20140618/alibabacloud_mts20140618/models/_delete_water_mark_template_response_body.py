# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteWaterMarkTemplateResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        water_mark_template_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The ID of the deleted watermark template.
        self.water_mark_template_id = water_mark_template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.water_mark_template_id is not None:
            result['WaterMarkTemplateId'] = self.water_mark_template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('WaterMarkTemplateId') is not None:
            self.water_mark_template_id = m.get('WaterMarkTemplateId')

        return self

