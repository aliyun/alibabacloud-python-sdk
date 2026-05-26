# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentretailvision20260506 import models as main_models
from darabonba.model import DaraModel

class QueryRecognitionResultResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryRecognitionResultResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QueryRecognitionResultResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryRecognitionResultResponseBodyData(DaraModel):
    def __init__(
        self,
        order_unique_id: str = None,
        result: main_models.QueryRecognitionResultResponseBodyDataResult = None,
        task_id: str = None,
        task_status: str = None,
    ):
        self.order_unique_id = order_unique_id
        self.result = result
        self.task_id = task_id
        self.task_status = task_status

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_unique_id is not None:
            result['OrderUniqueId'] = self.order_unique_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderUniqueId') is not None:
            self.order_unique_id = m.get('OrderUniqueId')

        if m.get('Result') is not None:
            temp_model = main_models.QueryRecognitionResultResponseBodyDataResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        return self

class QueryRecognitionResultResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        checkout_info: main_models.QueryRecognitionResultResponseBodyDataResultCheckoutInfo = None,
        items: List[main_models.QueryRecognitionResultResponseBodyDataResultItems] = None,
    ):
        self.checkout_info = checkout_info
        self.items = items

    def validate(self):
        if self.checkout_info:
            self.checkout_info.validate()
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.checkout_info is not None:
            result['CheckoutInfo'] = self.checkout_info.to_map()

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckoutInfo') is not None:
            temp_model = main_models.QueryRecognitionResultResponseBodyDataResultCheckoutInfo()
            self.checkout_info = temp_model.from_map(m.get('CheckoutInfo'))

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.QueryRecognitionResultResponseBodyDataResultItems()
                self.items.append(temp_model.from_map(k1))

        return self

class QueryRecognitionResultResponseBodyDataResultItems(DaraModel):
    def __init__(
        self,
        item_unique_id: str = None,
        platform_item_id: str = None,
        quantity: int = None,
    ):
        self.item_unique_id = item_unique_id
        self.platform_item_id = platform_item_id
        self.quantity = quantity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.item_unique_id is not None:
            result['ItemUniqueId'] = self.item_unique_id

        if self.platform_item_id is not None:
            result['PlatformItemId'] = self.platform_item_id

        if self.quantity is not None:
            result['Quantity'] = self.quantity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemUniqueId') is not None:
            self.item_unique_id = m.get('ItemUniqueId')

        if m.get('PlatformItemId') is not None:
            self.platform_item_id = m.get('PlatformItemId')

        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')

        return self

class QueryRecognitionResultResponseBodyDataResultCheckoutInfo(DaraModel):
    def __init__(
        self,
        checkout_status: str = None,
    ):
        self.checkout_status = checkout_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.checkout_status is not None:
            result['CheckoutStatus'] = self.checkout_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckoutStatus') is not None:
            self.checkout_status = m.get('CheckoutStatus')

        return self

