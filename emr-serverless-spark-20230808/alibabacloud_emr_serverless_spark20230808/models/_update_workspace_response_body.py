# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class UpdateWorkspaceResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.UpdateWorkspaceResponseBodyData = None,
        order_id: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.order_id = order_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.order_id is not None:
            result['orderId'] = self.order_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.UpdateWorkspaceResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class UpdateWorkspaceResponseBodyData(DaraModel):
    def __init__(
        self,
        order_id: str = None,
    ):
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_id is not None:
            result['orderId'] = self.order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')

        return self

