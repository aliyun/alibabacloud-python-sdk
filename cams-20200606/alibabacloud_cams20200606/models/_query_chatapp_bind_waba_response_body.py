# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_cams20200606 import models as main_models
from darabonba.model import DaraModel

class QueryChatappBindWabaResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.QueryChatappBindWabaResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The returned data.
        self.data = data
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QueryChatappBindWabaResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryChatappBindWabaResponseBodyData(DaraModel):
    def __init__(
        self,
        account_review_status: str = None,
        auth_international_rate_eligibility: Dict[str, Any] = None,
        business_id: str = None,
        business_name: str = None,
        currency: str = None,
        id: str = None,
        marketing_message_lite_status: str = None,
        message_template_namespace: str = None,
        name: str = None,
        primary_business_location: str = None,
    ):
        # The review state of the WhatsApp Business account (WABA).
        # 
        # >  Valid values:
        # 
        # *   PENDING: The WABA is to be reviewed.
        # 
        # *   APPROVED: The WABA was approved.
        # 
        # *   REJECTED: The WABA was rejected.
        # 
        # *   DISABLED: The WABA was forbidden.
        self.account_review_status = account_review_status
        # WABA related information.
        self.auth_international_rate_eligibility = auth_international_rate_eligibility
        # The business ID.
        self.business_id = business_id
        # The business name.
        self.business_name = business_name
        # The currency.
        self.currency = currency
        # The ID of the WhatsApp Business account.
        self.id = id
        # The Marketing Messaging Lite status.
        self.marketing_message_lite_status = marketing_message_lite_status
        # The namespace of the message template.
        self.message_template_namespace = message_template_namespace
        # The name of the WhatsApp Business account.
        self.name = name
        # The start time when the authentication-international rate applies.
        self.primary_business_location = primary_business_location

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_review_status is not None:
            result['AccountReviewStatus'] = self.account_review_status

        if self.auth_international_rate_eligibility is not None:
            result['AuthInternationalRateEligibility'] = self.auth_international_rate_eligibility

        if self.business_id is not None:
            result['BusinessId'] = self.business_id

        if self.business_name is not None:
            result['BusinessName'] = self.business_name

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.id is not None:
            result['Id'] = self.id

        if self.marketing_message_lite_status is not None:
            result['MarketingMessageLiteStatus'] = self.marketing_message_lite_status

        if self.message_template_namespace is not None:
            result['MessageTemplateNamespace'] = self.message_template_namespace

        if self.name is not None:
            result['Name'] = self.name

        if self.primary_business_location is not None:
            result['PrimaryBusinessLocation'] = self.primary_business_location

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountReviewStatus') is not None:
            self.account_review_status = m.get('AccountReviewStatus')

        if m.get('AuthInternationalRateEligibility') is not None:
            self.auth_international_rate_eligibility = m.get('AuthInternationalRateEligibility')

        if m.get('BusinessId') is not None:
            self.business_id = m.get('BusinessId')

        if m.get('BusinessName') is not None:
            self.business_name = m.get('BusinessName')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MarketingMessageLiteStatus') is not None:
            self.marketing_message_lite_status = m.get('MarketingMessageLiteStatus')

        if m.get('MessageTemplateNamespace') is not None:
            self.message_template_namespace = m.get('MessageTemplateNamespace')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PrimaryBusinessLocation') is not None:
            self.primary_business_location = m.get('PrimaryBusinessLocation')

        return self

