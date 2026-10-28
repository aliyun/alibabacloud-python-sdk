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
        # The list of account information for the invitation. A maximum of five accounts can be invited at a time.
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
        # The name of the distribution customer. Valid values:
        # - If the distribution customer is an enterprise, this is the company name.
        # - If the distribution customer is a T2 reseller partner, this is the partner name.
        # 
        # This parameter is required.
        self.account_nickname = account_nickname
        # The total budget quota that the partner allocates to the distribution customer.
        # 
        # This parameter is required.
        self.credit_line = credit_line
        # The account manager of the customer. Maximum length: 50 characters.
        self.customer_bd = customer_bd
        # The customer ID returned by the CreateCustomer API.
        # 
        # This parameter is required.
        self.customer_id = customer_id
        # The email address of the distribution customer account. The invitation email is sent to this address.
        # 
        # This parameter is required.
        self.email_address = email_address
        # The initial order placement status. Valid values:
        # 
        # - ban: Purchase is prohibited. After the customer is registered and associated, the customer cannot immediately place orders to purchase cloud resources. You must set the order control to normal before the customer can place orders.
        # - normal: Normal. After the customer is registered and associated, the customer can immediately place orders to purchase cloud resources.
        # 
        # This parameter is required.
        self.new_buy_status = new_buy_status
        # The description of the distribution customer.
        self.remark = remark
        # The type of the sub-account. Valid values:
        # - 1: end user of Agency.
        # - 2: end user of Reseller. 
        # - 5: T2 partner of Reseller.
        # 
        # This parameter is required.
        self.sub_account_type = sub_account_type
        # The shutdown policy that the partner manages for the distribution customer. Valid values:
        # 
        # - 1: delayStop. Alibaba Cloud takes over the resources and the customer enjoys a delayed shutdown quota. When the delayed shutdown quota is exhausted, instance shutdown is triggered. If payment is not made within 15 days, storage resources are released.
        # - 2: noStop. Manual management with no shutdown on overdue payment. The system does not manage the resource lifecycle of the non-trusteeship linked account. The partner must manually manage the instance shutdown status of the customer.
        # - 3: immediatelyStop. Instances are immediately shut down on overdue payment. When the available quota of the customer account is less than 0, the account enters the overdue payment status and instance shutdown is triggered.
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

