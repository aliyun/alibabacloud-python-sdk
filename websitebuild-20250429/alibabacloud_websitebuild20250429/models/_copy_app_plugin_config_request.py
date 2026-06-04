# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CopyAppPluginConfigRequest(DaraModel):
    def __init__(
        self,
        source_biz_id: str = None,
        target_biz_id: str = None,
    ):
        self.source_biz_id = source_biz_id
        self.target_biz_id = target_biz_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source_biz_id is not None:
            result['SourceBizId'] = self.source_biz_id

        if self.target_biz_id is not None:
            result['TargetBizId'] = self.target_biz_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceBizId') is not None:
            self.source_biz_id = m.get('SourceBizId')

        if m.get('TargetBizId') is not None:
            self.target_biz_id = m.get('TargetBizId')

        return self

