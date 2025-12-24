# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class ModifyDedicatedHostsChargeTypeResponseBody(DaraModel):
    def __init__(
        self,
        fee_of_instances: main_models.ModifyDedicatedHostsChargeTypeResponseBodyFeeOfInstances = None,
        order_id: str = None,
        request_id: str = None,
    ):
        # Details about the charges for the order.
        self.fee_of_instances = fee_of_instances
        # The ID of the order. This is returned only when the payment method is changed to subscription.
        self.order_id = order_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.fee_of_instances:
            self.fee_of_instances.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fee_of_instances is not None:
            result['FeeOfInstances'] = self.fee_of_instances.to_map()

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeeOfInstances') is not None:
            temp_model = main_models.ModifyDedicatedHostsChargeTypeResponseBodyFeeOfInstances()
            self.fee_of_instances = temp_model.from_map(m.get('FeeOfInstances'))

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ModifyDedicatedHostsChargeTypeResponseBodyFeeOfInstances(DaraModel):
    def __init__(
        self,
        fee_of_instance: List[main_models.ModifyDedicatedHostsChargeTypeResponseBodyFeeOfInstancesFeeOfInstance] = None,
    ):
        self.fee_of_instance = fee_of_instance

    def validate(self):
        if self.fee_of_instance:
            for v1 in self.fee_of_instance:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FeeOfInstance'] = []
        if self.fee_of_instance is not None:
            for k1 in self.fee_of_instance:
                result['FeeOfInstance'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fee_of_instance = []
        if m.get('FeeOfInstance') is not None:
            for k1 in m.get('FeeOfInstance'):
                temp_model = main_models.ModifyDedicatedHostsChargeTypeResponseBodyFeeOfInstancesFeeOfInstance()
                self.fee_of_instance.append(temp_model.from_map(k1))

        return self

class ModifyDedicatedHostsChargeTypeResponseBodyFeeOfInstancesFeeOfInstance(DaraModel):
    def __init__(
        self,
        currency: str = None,
        fee: str = None,
        instance_id: str = None,
    ):
        # The unit of currency for the bill.
        # 
        # Alibaba Cloud China site (aliyun.com): CNY
        # 
        # Alibaba Cloud International site (alibabacloud.com): USD
        self.currency = currency
        # The charged amount.
        self.fee = fee
        # The IDs of the dedicated hosts.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.currency is not None:
            result['Currency'] = self.currency

        if self.fee is not None:
            result['Fee'] = self.fee

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('Fee') is not None:
            self.fee = m.get('Fee')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

