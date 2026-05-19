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
        # List of invited account information, up to 5 at a time.
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
        # Name of the distribution customer:
        # - If the distribution customer is a company, this is the company name.
        # - If the distribution customer is a T2 reseller partner, this is the partner name.
        self.account_nickname = account_nickname
        # Total budget quota allocated by the partner to the distribution customer (quota).
        self.credit_line = credit_line
        # Reason for applying for cross-regional association.
        self.cross_scope_remark = cross_scope_remark
        # Customer Business Manager (limited to 50 characters).
        self.customer_bd = customer_bd
        # The email address to which the invitation email will be sent.
        self.email_address = email_address
        # Initial order status:
        # 
        # - ban: Purchase Ban - The customer cannot place orders immediately after successful registration and association. The \\"Order Control\\" must be set to \\"Normal\\" before placing orders.
        # - normal: Normal - The customer can place orders immediately after successful registration and association.
        self.new_buy_status = new_buy_status
        # Country or region of the invited T2 Reseller. The parameter should comply with the ISO 3166-1 two-letter code (Alpha-2). You can use the ListCountries API to get the current UID contract coverage area list.
        # 
        # The system will automatically determine if the invitation is cross-regional based on whether the `registerNation` parameter is within the T1 contract coverage area:
        # 
        # - If it\\"s a cross-regional invitation, a cross-regional approval process will be initiated. After approval by Alibaba Cloud, an invitation registration email will be sent to the invited email address.
        # - If it\\"s not a cross-regional invitation, an invitation registration email will be sent directly.
        self.register_nation = register_nation
        # Description of the distribution customer.
        self.remark = remark
        # Do not fill in, deprecated parameter.
        self.sub_account_type = sub_account_type
        # Management of the shutdown policy for the distribution customer by the partner.
        # 
        # - 1: delayStop - Enjoy delayed shutdown with a grace period: Alibaba Cloud takes over the resources, and when the grace period quota is exhausted, the instance will be shut down. If payment is not made within 15 days, the storage resources will be released.
        # - 2: noStop - Manual management of overdue without stopping: The system does not manage the lifecycle of the sub-account\\"s resources. The partner needs to manually manage the shutdown status of the customer\\"s instances.
        # - 3: immediatelyStop - Immediate shutdown upon overdue: When the available quota of the customer\\"s account is less than 0, the account enters an overdue state, triggering the shutdown of the instance.
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

