# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any, List

from alibabacloud_bssopenapi20230930 import models as main_models
from darabonba.model import DaraModel

class GetFundAccountCanRecycleAmountResponseBody(DaraModel):
    def __init__(
        self,
        available_amount: str = None,
        currency: str = None,
        metadata: Any = None,
        recycle_from_fund_account_id: str = None,
        recycle_to_fund_account_list: List[main_models.GetFundAccountCanRecycleAmountResponseBodyRecycleToFundAccountList] = None,
        request_id: str = None,
        transfer_amount: str = None,
    ):
        self.available_amount = available_amount
        self.currency = currency
        self.metadata = metadata
        self.recycle_from_fund_account_id = recycle_from_fund_account_id
        self.recycle_to_fund_account_list = recycle_to_fund_account_list
        self.request_id = request_id
        self.transfer_amount = transfer_amount

    def validate(self):
        if self.recycle_to_fund_account_list:
            for v1 in self.recycle_to_fund_account_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_amount is not None:
            result['AvailableAmount'] = self.available_amount

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.recycle_from_fund_account_id is not None:
            result['RecycleFromFundAccountId'] = self.recycle_from_fund_account_id

        result['RecycleToFundAccountList'] = []
        if self.recycle_to_fund_account_list is not None:
            for k1 in self.recycle_to_fund_account_list:
                result['RecycleToFundAccountList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.transfer_amount is not None:
            result['TransferAmount'] = self.transfer_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableAmount') is not None:
            self.available_amount = m.get('AvailableAmount')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('RecycleFromFundAccountId') is not None:
            self.recycle_from_fund_account_id = m.get('RecycleFromFundAccountId')

        self.recycle_to_fund_account_list = []
        if m.get('RecycleToFundAccountList') is not None:
            for k1 in m.get('RecycleToFundAccountList'):
                temp_model = main_models.GetFundAccountCanRecycleAmountResponseBodyRecycleToFundAccountList()
                self.recycle_to_fund_account_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TransferAmount') is not None:
            self.transfer_amount = m.get('TransferAmount')

        return self

class GetFundAccountCanRecycleAmountResponseBodyRecycleToFundAccountList(DaraModel):
    def __init__(
        self,
        fund_account_id: str = None,
        fund_account_name: str = None,
        fund_account_owner_account_id: str = None,
        max_recyclable_amount: str = None,
        original_transfer_remain_amount: str = None,
    ):
        self.fund_account_id = fund_account_id
        self.fund_account_name = fund_account_name
        self.fund_account_owner_account_id = fund_account_owner_account_id
        self.max_recyclable_amount = max_recyclable_amount
        self.original_transfer_remain_amount = original_transfer_remain_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id

        if self.fund_account_name is not None:
            result['FundAccountName'] = self.fund_account_name

        if self.fund_account_owner_account_id is not None:
            result['FundAccountOwnerAccountId'] = self.fund_account_owner_account_id

        if self.max_recyclable_amount is not None:
            result['MaxRecyclableAmount'] = self.max_recyclable_amount

        if self.original_transfer_remain_amount is not None:
            result['OriginalTransferRemainAmount'] = self.original_transfer_remain_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')

        if m.get('FundAccountName') is not None:
            self.fund_account_name = m.get('FundAccountName')

        if m.get('FundAccountOwnerAccountId') is not None:
            self.fund_account_owner_account_id = m.get('FundAccountOwnerAccountId')

        if m.get('MaxRecyclableAmount') is not None:
            self.max_recyclable_amount = m.get('MaxRecyclableAmount')

        if m.get('OriginalTransferRemainAmount') is not None:
            self.original_transfer_remain_amount = m.get('OriginalTransferRemainAmount')

        return self

