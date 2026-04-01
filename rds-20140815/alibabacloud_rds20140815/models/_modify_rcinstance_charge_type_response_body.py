# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class ModifyRCInstanceChargeTypeResponseBody(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        expired_time: List[str] = None,
        fee_of_instances: List[main_models.ModifyRCInstanceChargeTypeResponseBodyFeeOfInstances] = None,
        instance_ids: List[str] = None,
        order_id: str = None,
        request_id: str = None,
    ):
        # The billing method.
        # *   **POSTPAY**: pay-as-you-go.
        # *   **PREPAY**: subscription.
        self.charge_type = charge_type
        # The time when the instance expires.
        # >  If you change the billing method from subscription to pay-as-you-go, this parameter is not returned.
        self.expired_time = expired_time
        # The reserved parameter. This parameter is not supported.
        self.fee_of_instances = fee_of_instances
        # The list of instance IDs.
        self.instance_ids = instance_ids
        # The order ID.
        self.order_id = order_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.fee_of_instances:
            for v1 in self.fee_of_instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        result['FeeOfInstances'] = []
        if self.fee_of_instances is not None:
            for k1 in self.fee_of_instances:
                result['FeeOfInstances'].append(k1.to_map() if k1 else None)

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        self.fee_of_instances = []
        if m.get('FeeOfInstances') is not None:
            for k1 in m.get('FeeOfInstances'):
                temp_model = main_models.ModifyRCInstanceChargeTypeResponseBodyFeeOfInstances()
                self.fee_of_instances.append(temp_model.from_map(k1))

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ModifyRCInstanceChargeTypeResponseBodyFeeOfInstances(DaraModel):
    def __init__(
        self,
        currency: str = None,
        fee: str = None,
        instance_id: str = None,
    ):
        # The reserved parameter. This parameter is not supported.
        self.currency = currency
        # The reserved parameter. This parameter is not supported.
        self.fee = fee
        # The reserved parameter. This parameter is not supported.
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

