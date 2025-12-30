# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchRecallPushShrinkRequest(DaraModel):
    def __init__(
        self,
        out_biz_ids_shrink: str = None,
    ):
        # This parameter is required.
        self.out_biz_ids_shrink = out_biz_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.out_biz_ids_shrink is not None:
            result['OutBizIds'] = self.out_biz_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutBizIds') is not None:
            self.out_biz_ids_shrink = m.get('OutBizIds')

        return self

