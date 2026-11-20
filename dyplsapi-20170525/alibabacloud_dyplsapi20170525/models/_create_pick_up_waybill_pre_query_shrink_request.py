# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePickUpWaybillPreQueryShrinkRequest(DaraModel):
    def __init__(
        self,
        consignee_info_shrink: str = None,
        cp_code: str = None,
        order_channels: str = None,
        outer_order_code: str = None,
        pre_weight: str = None,
        sender_info_shrink: str = None,
    ):
        # The recipient information.
        # 
        # This parameter is required.
        self.consignee_info_shrink = consignee_info_shrink
        # The courier company code. If not specified, the system automatically assigns a courier company.
        self.cp_code = cp_code
        # The external channel source identifier. The value cannot contain underscores. The value is agreed upon with the system during integration.
        # 
        # This parameter is required.
        self.order_channels = order_channels
        # The order number in the caller\\"s system.
        self.outer_order_code = outer_order_code
        # The estimated weight, in grams.
        # 
        # > If you want to query the estimated price, this parameter is required.
        self.pre_weight = pre_weight
        # The sender information.
        # 
        # This parameter is required.
        self.sender_info_shrink = sender_info_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consignee_info_shrink is not None:
            result['ConsigneeInfo'] = self.consignee_info_shrink

        if self.cp_code is not None:
            result['CpCode'] = self.cp_code

        if self.order_channels is not None:
            result['OrderChannels'] = self.order_channels

        if self.outer_order_code is not None:
            result['OuterOrderCode'] = self.outer_order_code

        if self.pre_weight is not None:
            result['PreWeight'] = self.pre_weight

        if self.sender_info_shrink is not None:
            result['SenderInfo'] = self.sender_info_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsigneeInfo') is not None:
            self.consignee_info_shrink = m.get('ConsigneeInfo')

        if m.get('CpCode') is not None:
            self.cp_code = m.get('CpCode')

        if m.get('OrderChannels') is not None:
            self.order_channels = m.get('OrderChannels')

        if m.get('OuterOrderCode') is not None:
            self.outer_order_code = m.get('OuterOrderCode')

        if m.get('PreWeight') is not None:
            self.pre_weight = m.get('PreWeight')

        if m.get('SenderInfo') is not None:
            self.sender_info_shrink = m.get('SenderInfo')

        return self

