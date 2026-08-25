# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCustomResourceStatsRequest(DaraModel):
    def __init__(
        self,
        main_biz_type: str = None,
    ):
        # The business type. Default value: enterprise.
        self.main_biz_type = main_biz_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.main_biz_type is not None:
            result['MainBizType'] = self.main_biz_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MainBizType') is not None:
            self.main_biz_type = m.get('MainBizType')

        return self

