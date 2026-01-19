# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveRTCStatsV2Request(DaraModel):
    def __init__(
        self,
        call_id: str = None,
        general_info: str = None,
        goog_address: str = None,
        instance_id: str = None,
        receiver_report: str = None,
        sender_report: str = None,
    ):
        # This parameter is required.
        self.call_id = call_id
        # This parameter is required.
        self.general_info = general_info
        # This parameter is required.
        self.goog_address = goog_address
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.receiver_report = receiver_report
        # This parameter is required.
        self.sender_report = sender_report

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_id is not None:
            result['CallId'] = self.call_id

        if self.general_info is not None:
            result['GeneralInfo'] = self.general_info

        if self.goog_address is not None:
            result['GoogAddress'] = self.goog_address

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.receiver_report is not None:
            result['ReceiverReport'] = self.receiver_report

        if self.sender_report is not None:
            result['SenderReport'] = self.sender_report

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')

        if m.get('GeneralInfo') is not None:
            self.general_info = m.get('GeneralInfo')

        if m.get('GoogAddress') is not None:
            self.goog_address = m.get('GoogAddress')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ReceiverReport') is not None:
            self.receiver_report = m.get('ReceiverReport')

        if m.get('SenderReport') is not None:
            self.sender_report = m.get('SenderReport')

        return self

