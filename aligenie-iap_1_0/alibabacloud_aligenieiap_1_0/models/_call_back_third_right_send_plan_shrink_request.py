# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CallBackThirdRightSendPlanShrinkRequest(DaraModel):
    def __init__(
        self,
        biz_group: str = None,
        biz_type: str = None,
        card_type: int = None,
        error_msg: str = None,
        extend_info_shrink: str = None,
        genie_open_id: str = None,
        receive_status: int = None,
        sn: str = None,
        supplier_id: int = None,
    ):
        # device group
        self.biz_group = biz_group
        # device Type
        self.biz_type = biz_type
        # 1001 daily card, 1002 monthly card, 1003 quarterly card, 1004 annual card
        self.card_type = card_type
        # error message
        self.error_msg = error_msg
        # Extension fields
        self.extend_info_shrink = extend_info_shrink
        # Genie ID
        self.genie_open_id = genie_open_id
        # redemption status
        self.receive_status = receive_status
        # SN of the device
        self.sn = sn
        # Supplier ID
        self.supplier_id = supplier_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_group is not None:
            result['BizGroup'] = self.biz_group

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.card_type is not None:
            result['CardType'] = self.card_type

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.extend_info_shrink is not None:
            result['ExtendInfo'] = self.extend_info_shrink

        if self.genie_open_id is not None:
            result['GenieOpenId'] = self.genie_open_id

        if self.receive_status is not None:
            result['ReceiveStatus'] = self.receive_status

        if self.sn is not None:
            result['Sn'] = self.sn

        if self.supplier_id is not None:
            result['SupplierId'] = self.supplier_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizGroup') is not None:
            self.biz_group = m.get('BizGroup')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('CardType') is not None:
            self.card_type = m.get('CardType')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('ExtendInfo') is not None:
            self.extend_info_shrink = m.get('ExtendInfo')

        if m.get('GenieOpenId') is not None:
            self.genie_open_id = m.get('GenieOpenId')

        if m.get('ReceiveStatus') is not None:
            self.receive_status = m.get('ReceiveStatus')

        if m.get('Sn') is not None:
            self.sn = m.get('Sn')

        if m.get('SupplierId') is not None:
            self.supplier_id = m.get('SupplierId')

        return self

