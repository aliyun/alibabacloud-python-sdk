# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class GetFundAccountCanAllocateCreditAmountResponseBody(DaraModel):
    def __init__(
        self,
        ecid: str = None,
        ecid_allocated_credit_amount: str = None,
        ecid_credit_amount: str = None,
        fund_account_ecid: str = None,
        fund_account_id: int = None,
        fund_account_name: str = None,
        fund_account_owner_account_id: int = None,
        max_can_allocate_credit_amount: str = None,
        metadata: Any = None,
        min_can_allocate_credit_amount: str = None,
        nbid: str = None,
        request_id: str = None,
        site: str = None,
    ):
        self.ecid = ecid
        self.ecid_allocated_credit_amount = ecid_allocated_credit_amount
        self.ecid_credit_amount = ecid_credit_amount
        self.fund_account_ecid = fund_account_ecid
        self.fund_account_id = fund_account_id
        self.fund_account_name = fund_account_name
        self.fund_account_owner_account_id = fund_account_owner_account_id
        self.max_can_allocate_credit_amount = max_can_allocate_credit_amount
        self.metadata = metadata
        self.min_can_allocate_credit_amount = min_can_allocate_credit_amount
        self.nbid = nbid
        self.request_id = request_id
        self.site = site

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ecid is not None:
            result['Ecid'] = self.ecid

        if self.ecid_allocated_credit_amount is not None:
            result['EcidAllocatedCreditAmount'] = self.ecid_allocated_credit_amount

        if self.ecid_credit_amount is not None:
            result['EcidCreditAmount'] = self.ecid_credit_amount

        if self.fund_account_ecid is not None:
            result['FundAccountEcid'] = self.fund_account_ecid

        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id

        if self.fund_account_name is not None:
            result['FundAccountName'] = self.fund_account_name

        if self.fund_account_owner_account_id is not None:
            result['FundAccountOwnerAccountId'] = self.fund_account_owner_account_id

        if self.max_can_allocate_credit_amount is not None:
            result['MaxCanAllocateCreditAmount'] = self.max_can_allocate_credit_amount

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.min_can_allocate_credit_amount is not None:
            result['MinCanAllocateCreditAmount'] = self.min_can_allocate_credit_amount

        if self.nbid is not None:
            result['Nbid'] = self.nbid

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.site is not None:
            result['Site'] = self.site

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ecid') is not None:
            self.ecid = m.get('Ecid')

        if m.get('EcidAllocatedCreditAmount') is not None:
            self.ecid_allocated_credit_amount = m.get('EcidAllocatedCreditAmount')

        if m.get('EcidCreditAmount') is not None:
            self.ecid_credit_amount = m.get('EcidCreditAmount')

        if m.get('FundAccountEcid') is not None:
            self.fund_account_ecid = m.get('FundAccountEcid')

        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')

        if m.get('FundAccountName') is not None:
            self.fund_account_name = m.get('FundAccountName')

        if m.get('FundAccountOwnerAccountId') is not None:
            self.fund_account_owner_account_id = m.get('FundAccountOwnerAccountId')

        if m.get('MaxCanAllocateCreditAmount') is not None:
            self.max_can_allocate_credit_amount = m.get('MaxCanAllocateCreditAmount')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('MinCanAllocateCreditAmount') is not None:
            self.min_can_allocate_credit_amount = m.get('MinCanAllocateCreditAmount')

        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Site') is not None:
            self.site = m.get('Site')

        return self

