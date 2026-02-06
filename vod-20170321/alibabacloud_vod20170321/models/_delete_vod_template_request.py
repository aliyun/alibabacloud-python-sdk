# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteVodTemplateRequest(DaraModel):
    def __init__(
        self,
        vod_template_id: str = None,
    ):
        # The ID of the snapshot template.
        # 
        # This parameter is required.
        self.vod_template_id = vod_template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.vod_template_id is not None:
            result['VodTemplateId'] = self.vod_template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VodTemplateId') is not None:
            self.vod_template_id = m.get('VodTemplateId')

        return self

