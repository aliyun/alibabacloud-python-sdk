# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class GetBizTraceResponseBody(DaraModel):
    def __init__(
        self,
        item: main_models.BizTraceConfig = None,
        request_id: str = None,
    ):
        self.item = item
        self.request_id = request_id

    def validate(self):
        if self.item:
            self.item.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.item is not None:
            result['item'] = self.item.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('item') is not None:
            temp_model = main_models.BizTraceConfig()
            self.item = temp_model.from_map(m.get('item'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

