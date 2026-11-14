# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sandbox20260820 import models as main_models
from darabonba.model import DaraModel

class UpdateWarmPoolResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        warm_pool: main_models.PublicWarmPoolConfig = None,
    ):
        # The response business code.
        self.code = code
        # The response message.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # The warm pool configuration or current status.
        self.warm_pool = warm_pool

    def validate(self):
        if self.warm_pool:
            self.warm_pool.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.warm_pool is not None:
            result['warmPool'] = self.warm_pool.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('warmPool') is not None:
            temp_model = main_models.PublicWarmPoolConfig()
            self.warm_pool = temp_model.from_map(m.get('warmPool'))

        return self

