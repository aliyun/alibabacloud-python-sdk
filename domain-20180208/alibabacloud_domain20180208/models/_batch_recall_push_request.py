# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class BatchRecallPushRequest(DaraModel):
    def __init__(
        self,
        out_biz_ids: List[str] = None,
    ):
        # This parameter is required.
        self.out_biz_ids = out_biz_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.out_biz_ids is not None:
            result['OutBizIds'] = self.out_biz_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutBizIds') is not None:
            self.out_biz_ids = m.get('OutBizIds')

        return self

