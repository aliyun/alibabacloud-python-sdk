# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_linkedmall20230930 import models as main_models
from darabonba.model import DaraModel

class RefundOrderCmd(DaraModel):
    def __init__(
        self,
        apply_reason_text_id: int = None,
        apply_reason_tips: str = None,
        apply_refund_count: int = None,
        apply_refund_fee: int = None,
        biz_claim_type: int = None,
        goods_status: int = None,
        leave_message: str = None,
        leave_picture_lists: List[main_models.LeavePictureList] = None,
        order_line_id: str = None,
    ):
        # This parameter is required.
        self.apply_reason_text_id = apply_reason_text_id
        self.apply_reason_tips = apply_reason_tips
        # This parameter is required.
        self.apply_refund_count = apply_refund_count
        # This parameter is required.
        self.apply_refund_fee = apply_refund_fee
        # This parameter is required.
        self.biz_claim_type = biz_claim_type
        # This parameter is required.
        self.goods_status = goods_status
        self.leave_message = leave_message
        self.leave_picture_lists = leave_picture_lists
        # This parameter is required.
        self.order_line_id = order_line_id

    def validate(self):
        if self.leave_picture_lists:
            for v1 in self.leave_picture_lists:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_reason_text_id is not None:
            result['applyReasonTextId'] = self.apply_reason_text_id

        if self.apply_reason_tips is not None:
            result['applyReasonTips'] = self.apply_reason_tips

        if self.apply_refund_count is not None:
            result['applyRefundCount'] = self.apply_refund_count

        if self.apply_refund_fee is not None:
            result['applyRefundFee'] = self.apply_refund_fee

        if self.biz_claim_type is not None:
            result['bizClaimType'] = self.biz_claim_type

        if self.goods_status is not None:
            result['goodsStatus'] = self.goods_status

        if self.leave_message is not None:
            result['leaveMessage'] = self.leave_message

        result['leavePictureLists'] = []
        if self.leave_picture_lists is not None:
            for k1 in self.leave_picture_lists:
                result['leavePictureLists'].append(k1.to_map() if k1 else None)

        if self.order_line_id is not None:
            result['orderLineId'] = self.order_line_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applyReasonTextId') is not None:
            self.apply_reason_text_id = m.get('applyReasonTextId')

        if m.get('applyReasonTips') is not None:
            self.apply_reason_tips = m.get('applyReasonTips')

        if m.get('applyRefundCount') is not None:
            self.apply_refund_count = m.get('applyRefundCount')

        if m.get('applyRefundFee') is not None:
            self.apply_refund_fee = m.get('applyRefundFee')

        if m.get('bizClaimType') is not None:
            self.biz_claim_type = m.get('bizClaimType')

        if m.get('goodsStatus') is not None:
            self.goods_status = m.get('goodsStatus')

        if m.get('leaveMessage') is not None:
            self.leave_message = m.get('leaveMessage')

        self.leave_picture_lists = []
        if m.get('leavePictureLists') is not None:
            for k1 in m.get('leavePictureLists'):
                temp_model = main_models.LeavePictureList()
                self.leave_picture_lists.append(temp_model.from_map(k1))

        if m.get('orderLineId') is not None:
            self.order_line_id = m.get('orderLineId')

        return self

