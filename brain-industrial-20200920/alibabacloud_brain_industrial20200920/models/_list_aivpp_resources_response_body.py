# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_brain_industrial20200920 import models as main_models
from darabonba.model import DaraModel

class ListAivppResourcesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListAivppResourcesResponseBodyData] = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: str = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.message is not None:
            result['Message'] = self.message

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListAivppResourcesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAivppResourcesResponseBodyData(DaraModel):
    def __init__(
        self,
        connect_num: int = None,
        console_url: str = None,
        detail: str = None,
        expire_time: str = None,
        instance_id: str = None,
        instance_type: str = None,
        left_quantity: str = None,
        message_tps: int = None,
        order_id: str = None,
        quantity: str = None,
        specification: str = None,
        start_time: str = None,
        status: str = None,
        user_id: str = None,
    ):
        self.connect_num = connect_num
        self.console_url = console_url
        self.detail = detail
        self.expire_time = expire_time
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.left_quantity = left_quantity
        self.message_tps = message_tps
        self.order_id = order_id
        self.quantity = quantity
        self.specification = specification
        self.start_time = start_time
        self.status = status
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connect_num is not None:
            result['ConnectNum'] = self.connect_num

        if self.console_url is not None:
            result['ConsoleUrl'] = self.console_url

        if self.detail is not None:
            result['Detail'] = self.detail

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.left_quantity is not None:
            result['LeftQuantity'] = self.left_quantity

        if self.message_tps is not None:
            result['MessageTps'] = self.message_tps

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.quantity is not None:
            result['Quantity'] = self.quantity

        if self.specification is not None:
            result['Specification'] = self.specification

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectNum') is not None:
            self.connect_num = m.get('ConnectNum')

        if m.get('ConsoleUrl') is not None:
            self.console_url = m.get('ConsoleUrl')

        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('LeftQuantity') is not None:
            self.left_quantity = m.get('LeftQuantity')

        if m.get('MessageTps') is not None:
            self.message_tps = m.get('MessageTps')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')

        if m.get('Specification') is not None:
            self.specification = m.get('Specification')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

