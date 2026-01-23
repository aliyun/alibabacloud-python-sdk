# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agency20221216 import models as main_models
from darabonba.model import DaraModel

class InviteSubAccountRequest(DaraModel):
    def __init__(
        self,
        account_info_list: List[main_models.InviteSubAccountRequestAccountInfoList] = None,
    ):
        # List of invited account information,  less than 5 accounts at a time.</br>
        # `Sub-levels <= 5`
        # 
        # This parameter is required.
        self.account_info_list = account_info_list

    def validate(self):
        if self.account_info_list:
            for v1 in self.account_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AccountInfoList'] = []
        if self.account_info_list is not None:
            for k1 in self.account_info_list:
                result['AccountInfoList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.account_info_list = []
        if m.get('AccountInfoList') is not None:
            for k1 in m.get('AccountInfoList'):
                temp_model = main_models.InviteSubAccountRequestAccountInfoList()
                self.account_info_list.append(temp_model.from_map(k1))

        return self

class InviteSubAccountRequestAccountInfoList(DaraModel):
    def __init__(
        self,
        account_nickname: str = None,
        credit_line: str = None,
        customer_bd: str = None,
        customer_id: str = None,
        email_address: str = None,
        new_buy_status: str = None,
        remark: str = None,
        sub_account_type: str = None,
        zero_credit_shutdown_policy: str = None,
    ):
        # The name of Sub Account:</br>
        # 1. Use the official name of Company, if Sub Account is an enterprise.</br>
        # 2. Use the official name of Partner, if Sub Account is a T2 reseller.</br>
        # 
        # This parameter is required.
        self.account_nickname = account_nickname
        # The total budget Credit of Sub Account that distributed by Partner.
        # 
        # This parameter is required.
        self.credit_line = credit_line
        self.customer_bd = customer_bd
        # Customer ID, Returning ID from CreateCustomer API.
        # 
        # This parameter is required.
        self.customer_id = customer_id
        # The email address of End User,  which will receive the invitation email.
        # 
        # This parameter is required.
        self.email_address = email_address
        # Initial Order Status</br>
        # 1. ban：Ban the new purchase action--After End User finish registration and authorization, they can\\"t issue Cloud Resource order immediately. Partner should manually update the "Order Control" settings as "Normal" to enable new order.</br>
        # 2. normal：Normal--After End User finished registration and authorization, they can issue Cloud Resource order immediately.</br>
        # 
        # This parameter is required.
        self.new_buy_status = new_buy_status
        # Description of Sub Account.
        self.remark = remark
        # The type of Sub Account</br>
        # 
        # 1 Agency\\"s End User</br>
        # 2 Reseller\\"s End user</br>
        # 5 Reseller\\"s T2 Partner</br>
        # 
        # This parameter is required.
        self.sub_account_type = sub_account_type
        # Partner\\"s Shutdown Policy Management for Sub Account.</br>
        # 1: delayStop. The account have Shutdown-delay Privilege,  After Shutdown-delay Credit is ran out, Alibaba Cloud will take over resources and keep the instance for 15 days. In addition, the instance will be released if Sub Account failed to pay the bill within these 15 days.</br>
        # 2: noStop. Partner will manually manage Shutdown Status for Sub Account. Meanwhile, System would not manage the resource\\"s life-circle of Sub Account.</br>
        # 3: immediatelyStop. Once valid quota of Sub Account falls below 0 and be identified as defaulting account, it will trigger the instance shutdown immediately.</br>
        # 
        # This parameter is required.
        self.zero_credit_shutdown_policy = zero_credit_shutdown_policy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_nickname is not None:
            result['AccountNickname'] = self.account_nickname

        if self.credit_line is not None:
            result['CreditLine'] = self.credit_line

        if self.customer_bd is not None:
            result['CustomerBd'] = self.customer_bd

        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id

        if self.email_address is not None:
            result['EmailAddress'] = self.email_address

        if self.new_buy_status is not None:
            result['NewBuyStatus'] = self.new_buy_status

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.sub_account_type is not None:
            result['SubAccountType'] = self.sub_account_type

        if self.zero_credit_shutdown_policy is not None:
            result['ZeroCreditShutdownPolicy'] = self.zero_credit_shutdown_policy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountNickname') is not None:
            self.account_nickname = m.get('AccountNickname')

        if m.get('CreditLine') is not None:
            self.credit_line = m.get('CreditLine')

        if m.get('CustomerBd') is not None:
            self.customer_bd = m.get('CustomerBd')

        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')

        if m.get('EmailAddress') is not None:
            self.email_address = m.get('EmailAddress')

        if m.get('NewBuyStatus') is not None:
            self.new_buy_status = m.get('NewBuyStatus')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('SubAccountType') is not None:
            self.sub_account_type = m.get('SubAccountType')

        if m.get('ZeroCreditShutdownPolicy') is not None:
            self.zero_credit_shutdown_policy = m.get('ZeroCreditShutdownPolicy')

        return self

