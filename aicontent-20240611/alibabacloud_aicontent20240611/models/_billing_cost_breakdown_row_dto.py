# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aicontent20240611 import models as main_models
from darabonba.model import DaraModel

class BillingCostBreakdownRowDTO(DaraModel):
    def __init__(
        self,
        billing_type: str = None,
        client_id: int = None,
        client_name: str = None,
        dim_values: str = None,
        model_code: str = None,
        model_id: int = None,
        model_name: str = None,
        model_type: str = None,
        payable_amount: float = None,
        summary_time: int = None,
        tiers: List[main_models.BillingBillTierDTO] = None,
        values: str = None,
    ):
        self.billing_type = billing_type
        self.client_id = client_id
        self.client_name = client_name
        self.dim_values = dim_values
        self.model_code = model_code
        self.model_id = model_id
        self.model_name = model_name
        self.model_type = model_type
        self.payable_amount = payable_amount
        self.summary_time = summary_time
        self.tiers = tiers
        self.values = values

    def validate(self):
        if self.tiers:
            for v1 in self.tiers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.billing_type is not None:
            result['billingType'] = self.billing_type

        if self.client_id is not None:
            result['clientId'] = self.client_id

        if self.client_name is not None:
            result['clientName'] = self.client_name

        if self.dim_values is not None:
            result['dimValues'] = self.dim_values

        if self.model_code is not None:
            result['modelCode'] = self.model_code

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.model_name is not None:
            result['modelName'] = self.model_name

        if self.model_type is not None:
            result['modelType'] = self.model_type

        if self.payable_amount is not None:
            result['payableAmount'] = self.payable_amount

        if self.summary_time is not None:
            result['summaryTime'] = self.summary_time

        result['tiers'] = []
        if self.tiers is not None:
            for k1 in self.tiers:
                result['tiers'].append(k1.to_map() if k1 else None)

        if self.values is not None:
            result['values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingType') is not None:
            self.billing_type = m.get('billingType')

        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')

        if m.get('clientName') is not None:
            self.client_name = m.get('clientName')

        if m.get('dimValues') is not None:
            self.dim_values = m.get('dimValues')

        if m.get('modelCode') is not None:
            self.model_code = m.get('modelCode')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')

        if m.get('modelType') is not None:
            self.model_type = m.get('modelType')

        if m.get('payableAmount') is not None:
            self.payable_amount = m.get('payableAmount')

        if m.get('summaryTime') is not None:
            self.summary_time = m.get('summaryTime')

        self.tiers = []
        if m.get('tiers') is not None:
            for k1 in m.get('tiers'):
                temp_model = main_models.BillingBillTierDTO()
                self.tiers.append(temp_model.from_map(k1))

        if m.get('values') is not None:
            self.values = m.get('values')

        return self

