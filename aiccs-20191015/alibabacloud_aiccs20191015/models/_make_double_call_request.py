# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MakeDoubleCallRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        biz_data: str = None,
        instance_id: str = None,
        member_phone: str = None,
        outbound_call_number: str = None,
        servicer_phone: str = None,
    ):
        # This parameter is required.
        self.account_name = account_name
        self.biz_data = biz_data
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.member_phone = member_phone
        # This parameter is required.
        self.outbound_call_number = outbound_call_number
        self.servicer_phone = servicer_phone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.biz_data is not None:
            result['BizData'] = self.biz_data

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.member_phone is not None:
            result['MemberPhone'] = self.member_phone

        if self.outbound_call_number is not None:
            result['OutboundCallNumber'] = self.outbound_call_number

        if self.servicer_phone is not None:
            result['ServicerPhone'] = self.servicer_phone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('BizData') is not None:
            self.biz_data = m.get('BizData')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MemberPhone') is not None:
            self.member_phone = m.get('MemberPhone')

        if m.get('OutboundCallNumber') is not None:
            self.outbound_call_number = m.get('OutboundCallNumber')

        if m.get('ServicerPhone') is not None:
            self.servicer_phone = m.get('ServicerPhone')

        return self

