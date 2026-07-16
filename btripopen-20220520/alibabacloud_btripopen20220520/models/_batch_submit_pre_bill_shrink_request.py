# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchSubmitPreBillShrinkRequest(DaraModel):
    def __init__(
        self,
        app_ip: str = None,
        bill_batch: str = None,
        customer_decision: int = None,
        dimension: int = None,
        values_shrink: str = None,
    ):
        # A system parameter. You do not need to manually specify this parameter.
        self.app_ip = app_ip
        # The bill batch date in the format of yyyy-MM-dd, such as 2026-06-21.
        # 
        # This parameter is required.
        self.bill_batch = bill_batch
        # The customer decision. Valid values:
        # - 1: bill in the current period.
        # - 2: deferred billing.
        # - null: bill based on the current billing decision of the record.
        self.customer_decision = customer_decision
        # The dimension type. Valid values:
        # - 1: bill ID.
        # - 2: order number.
        # - 3: approval form.
        # - 4: invoice title.
        # 
        # This parameter is required.
        self.dimension = dimension
        # The values determined by the dimension parameter. For example, if dimension is set to 1, the values should be bill IDs.
        # 
        # This parameter is required.
        self.values_shrink = values_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_ip is not None:
            result['app_ip'] = self.app_ip

        if self.bill_batch is not None:
            result['bill_batch'] = self.bill_batch

        if self.customer_decision is not None:
            result['customer_decision'] = self.customer_decision

        if self.dimension is not None:
            result['dimension'] = self.dimension

        if self.values_shrink is not None:
            result['values'] = self.values_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('app_ip') is not None:
            self.app_ip = m.get('app_ip')

        if m.get('bill_batch') is not None:
            self.bill_batch = m.get('bill_batch')

        if m.get('customer_decision') is not None:
            self.customer_decision = m.get('customer_decision')

        if m.get('dimension') is not None:
            self.dimension = m.get('dimension')

        if m.get('values') is not None:
            self.values_shrink = m.get('values')

        return self

