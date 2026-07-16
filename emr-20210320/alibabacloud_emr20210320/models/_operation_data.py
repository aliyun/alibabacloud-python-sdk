# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class OperationData(DaraModel):
    def __init__(
        self,
        actual_delivered_amounts: int = None,
        failed_refund_instance_ids: List[str] = None,
        to_be_delivered_amounts: int = None,
    ):
        # The number of units actually delivered.
        self.actual_delivered_amounts = actual_delivered_amounts
        # The IDs of instances that could not be refunded.
        self.failed_refund_instance_ids = failed_refund_instance_ids
        # The number of units requested.
        self.to_be_delivered_amounts = to_be_delivered_amounts

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actual_delivered_amounts is not None:
            result['actualDeliveredAmounts'] = self.actual_delivered_amounts

        if self.failed_refund_instance_ids is not None:
            result['failedRefundInstanceIds'] = self.failed_refund_instance_ids

        if self.to_be_delivered_amounts is not None:
            result['toBeDeliveredAmounts'] = self.to_be_delivered_amounts

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actualDeliveredAmounts') is not None:
            self.actual_delivered_amounts = m.get('actualDeliveredAmounts')

        if m.get('failedRefundInstanceIds') is not None:
            self.failed_refund_instance_ids = m.get('failedRefundInstanceIds')

        if m.get('toBeDeliveredAmounts') is not None:
            self.to_be_delivered_amounts = m.get('toBeDeliveredAmounts')

        return self

