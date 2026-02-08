# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyMaterialFileStatusShrinkRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        file_ids_shrink: str = None,
        status: str = None,
    ):
        # This parameter is required.
        self.biz_id = biz_id
        # This parameter is required.
        self.file_ids_shrink = file_ids_shrink
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.file_ids_shrink is not None:
            result['FileIds'] = self.file_ids_shrink

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('FileIds') is not None:
            self.file_ids_shrink = m.get('FileIds')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

