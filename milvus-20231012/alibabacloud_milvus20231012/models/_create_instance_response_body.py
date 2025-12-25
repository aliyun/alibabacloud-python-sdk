# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_milvus20231012 import models as main_models
from darabonba.model import DaraModel

class CreateInstanceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        data: main_models.CreateInstanceResponseBodyData = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('data') is not None:
            temp_model = main_models.CreateInstanceResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class CreateInstanceResponseBodyData(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        order_id: str = None,
    ):
        self.instance_id = instance_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.order_id is not None:
            result['orderId'] = self.order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')

        return self

