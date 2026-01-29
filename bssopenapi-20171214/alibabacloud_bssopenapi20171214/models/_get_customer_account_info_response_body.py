# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class GetCustomerAccountInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetCustomerAccountInfoResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code returned.
        self.code = code
        # The data returned.
        self.data = data
        # The message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call is successful. A value of true indicates that the call is successful. A value of false indicates that the call failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetCustomerAccountInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetCustomerAccountInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        account_type: str = None,
        credit_limit_status: str = None,
        hosting_status: str = None,
        is_certified: bool = None,
        login_email: str = None,
        mpk: int = None,
    ):
        # The type of the account. A value of 1 indicates an enterprise account. A value of 0 indicates an individual account.
        self.account_type = account_type
        # The business status of the customer. Valid values:
        # 
        # Freeze: The business is frozen.
        # 
        # Thaw: The business is unfrozen.
        # 
        # Trusteeship: The business is hosted.
        # 
        # TrusteeshipCancel: The business is not hosted.
        self.credit_limit_status = credit_limit_status
        # The hosting status of the credit information and instances of the customer. If the credit information and instances of the customer are managed on Alibaba Cloud, Alibaba Cloud suspends a customer service upon overdue payment. Valid values:
        # 
        # FREEZE: The business of the customer is frozen.
        # 
        # TRUSTEESHIP: The business of the customer is hosted.
        self.hosting_status = hosting_status
        # Indicates whether the account passes the real-name verification.
        self.is_certified = is_certified
        # The email address of the customer.
        self.login_email = login_email
        # The ID of the management account.
        self.mpk = mpk

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_type is not None:
            result['AccountType'] = self.account_type

        if self.credit_limit_status is not None:
            result['CreditLimitStatus'] = self.credit_limit_status

        if self.hosting_status is not None:
            result['HostingStatus'] = self.hosting_status

        if self.is_certified is not None:
            result['IsCertified'] = self.is_certified

        if self.login_email is not None:
            result['LoginEmail'] = self.login_email

        if self.mpk is not None:
            result['Mpk'] = self.mpk

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')

        if m.get('CreditLimitStatus') is not None:
            self.credit_limit_status = m.get('CreditLimitStatus')

        if m.get('HostingStatus') is not None:
            self.hosting_status = m.get('HostingStatus')

        if m.get('IsCertified') is not None:
            self.is_certified = m.get('IsCertified')

        if m.get('LoginEmail') is not None:
            self.login_email = m.get('LoginEmail')

        if m.get('Mpk') is not None:
            self.mpk = m.get('Mpk')

        return self

