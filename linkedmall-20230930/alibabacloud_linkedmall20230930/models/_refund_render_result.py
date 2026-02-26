# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_linkedmall20230930 import models as main_models
from darabonba.model import DaraModel

class RefundRenderResult(DaraModel):
    def __init__(
        self,
        biz_claim_type: int = None,
        max_refund_fee_data: main_models.DistributionMaxRefundFee = None,
        order_line_id: str = None,
        refund_reason_list: List[main_models.RefundReason] = None,
        request_id: str = None,
    ):
        self.biz_claim_type = biz_claim_type
        self.max_refund_fee_data = max_refund_fee_data
        self.order_line_id = order_line_id
        self.refund_reason_list = refund_reason_list
        self.request_id = request_id

    def validate(self):
        if self.max_refund_fee_data:
            self.max_refund_fee_data.validate()
        if self.refund_reason_list:
            for v1 in self.refund_reason_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_claim_type is not None:
            result['bizClaimType'] = self.biz_claim_type

        if self.max_refund_fee_data is not None:
            result['maxRefundFeeData'] = self.max_refund_fee_data.to_map()

        if self.order_line_id is not None:
            result['orderLineId'] = self.order_line_id

        result['refundReasonList'] = []
        if self.refund_reason_list is not None:
            for k1 in self.refund_reason_list:
                result['refundReasonList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizClaimType') is not None:
            self.biz_claim_type = m.get('bizClaimType')

        if m.get('maxRefundFeeData') is not None:
            temp_model = main_models.DistributionMaxRefundFee()
            self.max_refund_fee_data = temp_model.from_map(m.get('maxRefundFeeData'))

        if m.get('orderLineId') is not None:
            self.order_line_id = m.get('orderLineId')

        self.refund_reason_list = []
        if m.get('refundReasonList') is not None:
            for k1 in m.get('refundReasonList'):
                temp_model = main_models.RefundReason()
                self.refund_reason_list.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

