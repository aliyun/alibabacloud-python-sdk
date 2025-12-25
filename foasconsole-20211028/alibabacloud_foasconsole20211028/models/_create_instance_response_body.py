# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_foasconsole20211028 import models as main_models
from darabonba.model import DaraModel

class CreateInstanceResponseBody(DaraModel):
    def __init__(
        self,
        order_info: main_models.CreateInstanceResponseBodyOrderInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.order_info = order_info
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.order_info:
            self.order_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_info is not None:
            result['OrderInfo'] = self.order_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderInfo') is not None:
            temp_model = main_models.CreateInstanceResponseBodyOrderInfo()
            self.order_info = temp_model.from_map(m.get('OrderInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreateInstanceResponseBodyOrderInfo(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        order_id: int = None,
        storage_instance_id: str = None,
        storage_order_id: int = None,
    ):
        self.instance_id = instance_id
        self.order_id = order_id
        self.storage_instance_id = storage_instance_id
        self.storage_order_id = storage_order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.storage_instance_id is not None:
            result['StorageInstanceId'] = self.storage_instance_id

        if self.storage_order_id is not None:
            result['StorageOrderId'] = self.storage_order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('StorageInstanceId') is not None:
            self.storage_instance_id = m.get('StorageInstanceId')

        if m.get('StorageOrderId') is not None:
            self.storage_order_id = m.get('StorageOrderId')

        return self

