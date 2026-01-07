# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_accountcenter20241209 import models as main_models
from darabonba.model import DaraModel

class EnterpriseContactQueryDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.EnterpriseContactQueryDetailResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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
            temp_model = main_models.EnterpriseContactQueryDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class EnterpriseContactQueryDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        contact_email: str = None,
        contact_id: int = None,
        contact_mobile: str = None,
        contact_name: str = None,
        contact_position: str = None,
        customer_id: str = None,
        email_confirmed: bool = None,
        entity_id: str = None,
        entity_type: str = None,
        has_subscription: bool = None,
        mobile_confirmed: bool = None,
        shared_contact: bool = None,
        uid: str = None,
        update_date: int = None,
        update_user: str = None,
    ):
        self.contact_email = contact_email
        self.contact_id = contact_id
        self.contact_mobile = contact_mobile
        self.contact_name = contact_name
        self.contact_position = contact_position
        self.customer_id = customer_id
        self.email_confirmed = email_confirmed
        self.entity_id = entity_id
        # leId/customerId
        self.entity_type = entity_type
        self.has_subscription = has_subscription
        self.mobile_confirmed = mobile_confirmed
        self.shared_contact = shared_contact
        self.uid = uid
        self.update_date = update_date
        self.update_user = update_user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email

        if self.contact_id is not None:
            result['ContactId'] = self.contact_id

        if self.contact_mobile is not None:
            result['ContactMobile'] = self.contact_mobile

        if self.contact_name is not None:
            result['ContactName'] = self.contact_name

        if self.contact_position is not None:
            result['ContactPosition'] = self.contact_position

        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id

        if self.email_confirmed is not None:
            result['EmailConfirmed'] = self.email_confirmed

        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.has_subscription is not None:
            result['HasSubscription'] = self.has_subscription

        if self.mobile_confirmed is not None:
            result['MobileConfirmed'] = self.mobile_confirmed

        if self.shared_contact is not None:
            result['SharedContact'] = self.shared_contact

        if self.uid is not None:
            result['Uid'] = self.uid

        if self.update_date is not None:
            result['UpdateDate'] = self.update_date

        if self.update_user is not None:
            result['UpdateUser'] = self.update_user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')

        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')

        if m.get('ContactMobile') is not None:
            self.contact_mobile = m.get('ContactMobile')

        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')

        if m.get('ContactPosition') is not None:
            self.contact_position = m.get('ContactPosition')

        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')

        if m.get('EmailConfirmed') is not None:
            self.email_confirmed = m.get('EmailConfirmed')

        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('HasSubscription') is not None:
            self.has_subscription = m.get('HasSubscription')

        if m.get('MobileConfirmed') is not None:
            self.mobile_confirmed = m.get('MobileConfirmed')

        if m.get('SharedContact') is not None:
            self.shared_contact = m.get('SharedContact')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')

        if m.get('UpdateUser') is not None:
            self.update_user = m.get('UpdateUser')

        return self

