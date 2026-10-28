# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agency20221216 import models as main_models
from darabonba.model import DaraModel

class InviteSubResellerRequest(DaraModel):
    def __init__(
        self,
        account_info_list: List[main_models.InviteSubResellerRequestAccountInfoList] = None,
    ):
        # The list of account information for the invitation. A maximum of five accounts can be specified at a time.
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
                temp_model = main_models.InviteSubResellerRequestAccountInfoList()
                self.account_info_list.append(temp_model.from_map(k1))

        return self

class InviteSubResellerRequestAccountInfoList(DaraModel):
    def __init__(
        self,
        account_nickname: str = None,
        credit_line: str = None,
        cross_scope_remark: str = None,
        customer_bd: str = None,
        email_address: str = None,
        new_buy_status: str = None,
        register_nation: str = None,
        remark: str = None,
        sub_account_type: str = None,
        zero_credit_shutdown_policy: str = None,
    ):
        # The name of the distribution customer.
        # - If the distribution customer is an enterprise, this is the company name.
        # - If the distribution customer is a T2 Reseller partner, this is the partner name.
        self.account_nickname = account_nickname
        # The total budget quota that the partner allocates to the distribution customer.
        self.credit_line = credit_line
        # The reason for applying for a cross-region association.
        self.cross_scope_remark = cross_scope_remark
        # The customer account manager. The value can be up to 50 characters in length.
        self.customer_bd = customer_bd
        # The email address to which the invitation email is sent.
        self.email_address = email_address
        # The initial order placement status. Valid values:
        # 
        # - ban: Purchase is prohibited. After the customer is registered and associated, the customer cannot place orders to purchase cloud resources immediately. You must set the order control to Normal before the customer can place orders.
        # - normal: Normal. After the customer is registered and associated, the customer can place orders to purchase cloud resources immediately.
        self.new_buy_status = new_buy_status
        # The country or region of the invited T2 Reseller. The value must comply with the ISO 3166-1 alpha-2 code. You can call the ListCountries operation to query the contract coverage area list of the current UID.
        # 
        # The system automatically determines whether the invitation is cross-region based on whether this parameter falls within the T1 contract coverage area.
        # 
        # - If the invitation is cross-region, a cross-region invitation approval process is initiated. After the approval is granted, an invitation registration email is sent to the specified email address.
        # - If the invitation is not cross-region, an invitation registration email is sent directly.
        self.register_nation = register_nation
        # The description of the distribution customer.
        self.remark = remark
        # This parameter is deprecated. You do not need to specify this parameter.
        self.sub_account_type = sub_account_type
        # The shutdown policy that the partner sets for the distribution customer.
        # 
        # - 1: delayStop. The account uses the delayed shutdown quota for deferred instance shutdown. Alibaba Cloud takes over the resources. When the delayed shutdown quota is exhausted, instance shutdown is triggered. If the payment is not made within 15 days, storage resources are released.
        # - 2: noStop. Manual management with no shutdown on overdue payment. The system does not manage the resource lifecycle of the non-trusteeship linked account. The partner must manually manage the instance shutdown status of the customer.
        # - 3: immediatelyStop. Immediate shutdown on overdue payment. When the active quota of the customer account is less than 0, the account enters the overdue payment status and instance shutdown is triggered.
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

        if self.cross_scope_remark is not None:
            result['CrossScopeRemark'] = self.cross_scope_remark

        if self.customer_bd is not None:
            result['CustomerBd'] = self.customer_bd

        if self.email_address is not None:
            result['EmailAddress'] = self.email_address

        if self.new_buy_status is not None:
            result['NewBuyStatus'] = self.new_buy_status

        if self.register_nation is not None:
            result['RegisterNation'] = self.register_nation

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

        if m.get('CrossScopeRemark') is not None:
            self.cross_scope_remark = m.get('CrossScopeRemark')

        if m.get('CustomerBd') is not None:
            self.customer_bd = m.get('CustomerBd')

        if m.get('EmailAddress') is not None:
            self.email_address = m.get('EmailAddress')

        if m.get('NewBuyStatus') is not None:
            self.new_buy_status = m.get('NewBuyStatus')

        if m.get('RegisterNation') is not None:
            self.register_nation = m.get('RegisterNation')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('SubAccountType') is not None:
            self.sub_account_type = m.get('SubAccountType')

        if m.get('ZeroCreditShutdownPolicy') is not None:
            self.zero_credit_shutdown_policy = m.get('ZeroCreditShutdownPolicy')

        return self

