# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class GetFundAccountCanTransferAmountResponseBody(DaraModel):
    def __init__(
        self,
        available_amount: str = None,
        cash_amount: str = None,
        currency: str = None,
        fund_account_ecid: str = None,
        fund_account_id: int = None,
        fund_account_name: str = None,
        fund_account_owner_account_id: int = None,
        max_transferable_amount: str = None,
        metadata: Any = None,
        nbid: str = None,
        request_id: str = None,
        site: str = None,
        transfer_amount: str = None,
    ):
        # The available amount.
        self.available_amount = available_amount
        # The cash ledger balance.
        self.cash_amount = cash_amount
        # The currency.
        self.currency = currency
        # The enterprise entity ID of the fund account owner.
        self.fund_account_ecid = fund_account_ecid
        # The fund account ID.
        self.fund_account_id = fund_account_id
        # The fund account name.
        self.fund_account_name = fund_account_name
        # The Alibaba Cloud account ID of the fund account owner.
        self.fund_account_owner_account_id = fund_account_owner_account_id
        # The maximum transferable amount.
        self.max_transferable_amount = max_transferable_amount
        # The metadata of the response structure.
        self.metadata = metadata
        # The primary sales site.
        self.nbid = nbid
        # The request ID.
        self.request_id = request_id
        # The site.
        self.site = site
        # The transfer ledger balance.
        self.transfer_amount = transfer_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_amount is not None:
            result['AvailableAmount'] = self.available_amount

        if self.cash_amount is not None:
            result['CashAmount'] = self.cash_amount

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.fund_account_ecid is not None:
            result['FundAccountEcid'] = self.fund_account_ecid

        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id

        if self.fund_account_name is not None:
            result['FundAccountName'] = self.fund_account_name

        if self.fund_account_owner_account_id is not None:
            result['FundAccountOwnerAccountId'] = self.fund_account_owner_account_id

        if self.max_transferable_amount is not None:
            result['MaxTransferableAmount'] = self.max_transferable_amount

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.nbid is not None:
            result['Nbid'] = self.nbid

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.site is not None:
            result['Site'] = self.site

        if self.transfer_amount is not None:
            result['TransferAmount'] = self.transfer_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableAmount') is not None:
            self.available_amount = m.get('AvailableAmount')

        if m.get('CashAmount') is not None:
            self.cash_amount = m.get('CashAmount')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('FundAccountEcid') is not None:
            self.fund_account_ecid = m.get('FundAccountEcid')

        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')

        if m.get('FundAccountName') is not None:
            self.fund_account_name = m.get('FundAccountName')

        if m.get('FundAccountOwnerAccountId') is not None:
            self.fund_account_owner_account_id = m.get('FundAccountOwnerAccountId')

        if m.get('MaxTransferableAmount') is not None:
            self.max_transferable_amount = m.get('MaxTransferableAmount')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Site') is not None:
            self.site = m.get('Site')

        if m.get('TransferAmount') is not None:
            self.transfer_amount = m.get('TransferAmount')

        return self

