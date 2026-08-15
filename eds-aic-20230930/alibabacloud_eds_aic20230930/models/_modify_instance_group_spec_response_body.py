# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class ModifyInstanceGroupSpecResponseBody(DaraModel):
    def __init__(
        self,
        order_info: List[main_models.ModifyInstanceGroupSpecResponseBodyOrderInfo] = None,
        order_task_id: str = None,
        request_id: str = None,
    ):
        # The order information.
        self.order_info = order_info
        # The order task ID that is returned when specifications of more than 10 instance groups are changed in a batch. You can call the **DescribeOrderTasks** operation to query the information about each order.
        self.order_task_id = order_task_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.order_info:
            for v1 in self.order_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['OrderInfo'] = []
        if self.order_info is not None:
            for k1 in self.order_info:
                result['OrderInfo'].append(k1.to_map() if k1 else None)

        if self.order_task_id is not None:
            result['OrderTaskId'] = self.order_task_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.order_info = []
        if m.get('OrderInfo') is not None:
            for k1 in m.get('OrderInfo'):
                temp_model = main_models.ModifyInstanceGroupSpecResponseBodyOrderInfo()
                self.order_info.append(temp_model.from_map(k1))

        if m.get('OrderTaskId') is not None:
            self.order_task_id = m.get('OrderTaskId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ModifyInstanceGroupSpecResponseBodyOrderInfo(DaraModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        order_id: str = None,
    ):
        # The list of instance IDs.
        self.instance_ids = instance_ids
        # The order ID.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        return self

