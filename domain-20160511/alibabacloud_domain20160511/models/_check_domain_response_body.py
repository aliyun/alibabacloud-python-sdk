# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckDomainResponseBody(DaraModel):
    def __init__(
        self,
        avail: int = None,
        fee_command: str = None,
        fee_currency: str = None,
        fee_fee: str = None,
        fee_period: int = None,
        name: str = None,
        reason: str = None,
        request_id: str = None,
        rmb_fee: str = None,
    ):
        self.avail = avail
        self.fee_command = fee_command
        self.fee_currency = fee_currency
        self.fee_fee = fee_fee
        self.fee_period = fee_period
        self.name = name
        self.reason = reason
        self.request_id = request_id
        self.rmb_fee = rmb_fee

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avail is not None:
            result['Avail'] = self.avail

        if self.fee_command is not None:
            result['FeeCommand'] = self.fee_command

        if self.fee_currency is not None:
            result['FeeCurrency'] = self.fee_currency

        if self.fee_fee is not None:
            result['FeeFee'] = self.fee_fee

        if self.fee_period is not None:
            result['FeePeriod'] = self.fee_period

        if self.name is not None:
            result['Name'] = self.name

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.rmb_fee is not None:
            result['RmbFee'] = self.rmb_fee

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Avail') is not None:
            self.avail = m.get('Avail')

        if m.get('FeeCommand') is not None:
            self.fee_command = m.get('FeeCommand')

        if m.get('FeeCurrency') is not None:
            self.fee_currency = m.get('FeeCurrency')

        if m.get('FeeFee') is not None:
            self.fee_fee = m.get('FeeFee')

        if m.get('FeePeriod') is not None:
            self.fee_period = m.get('FeePeriod')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RmbFee') is not None:
            self.rmb_fee = m.get('RmbFee')

        return self

