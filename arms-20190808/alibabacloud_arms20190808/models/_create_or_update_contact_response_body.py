# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class CreateOrUpdateContactResponseBody(DaraModel):
    def __init__(
        self,
        alert_contact: main_models.CreateOrUpdateContactResponseBodyAlertContact = None,
        request_id: str = None,
    ):
        # The object of the alert contact.
        self.alert_contact = alert_contact
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.alert_contact:
            self.alert_contact.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_contact is not None:
            result['AlertContact'] = self.alert_contact.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertContact') is not None:
            temp_model = main_models.CreateOrUpdateContactResponseBodyAlertContact()
            self.alert_contact = temp_model.from_map(m.get('AlertContact'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateOrUpdateContactResponseBodyAlertContact(DaraModel):
    def __init__(
        self,
        contact_id: float = None,
        contact_name: str = None,
        ding_robot_url: str = None,
        email: str = None,
        is_verify: bool = None,
        phone: str = None,
        reissue_send_notice: int = None,
        is_email_verify: bool = None,
    ):
        # The ID of the alert contact.
        self.contact_id = contact_id
        # The name of the alert contact.
        self.contact_name = contact_name
        # The webhook URL of the DingTalk chatbot.
        self.ding_robot_url = ding_robot_url
        # The email address of the alert contact.
        self.email = email
        # Indicates whether the mobile number was verified. Valid values:
        # 
        # *   `false` (default value): No
        # *   `true`: Yes
        # 
        # You can call the **SendTTSVerifyLink** operation to verify the mobile number of an alert contact. Only verified mobile numbers can be specified in a notification policy to receive phone calls.
        self.is_verify = is_verify
        # The mobile number of the alert contact.
        self.phone = phone
        # The operation that you want to perform if phone calls fail to be answered. Valid values: 0: No operation is performed. 1: A phone call is made again. 2: A text message is sent. 3 (default value): The global default value is used.
        self.reissue_send_notice = reissue_send_notice
        # Indicates whether the email address was verified.
        self.is_email_verify = is_email_verify

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id

        if self.contact_name is not None:
            result['ContactName'] = self.contact_name

        if self.ding_robot_url is not None:
            result['DingRobotUrl'] = self.ding_robot_url

        if self.email is not None:
            result['Email'] = self.email

        if self.is_verify is not None:
            result['IsVerify'] = self.is_verify

        if self.phone is not None:
            result['Phone'] = self.phone

        if self.reissue_send_notice is not None:
            result['ReissueSendNotice'] = self.reissue_send_notice

        if self.is_email_verify is not None:
            result['isEmailVerify'] = self.is_email_verify

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')

        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')

        if m.get('DingRobotUrl') is not None:
            self.ding_robot_url = m.get('DingRobotUrl')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('IsVerify') is not None:
            self.is_verify = m.get('IsVerify')

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        if m.get('ReissueSendNotice') is not None:
            self.reissue_send_notice = m.get('ReissueSendNotice')

        if m.get('isEmailVerify') is not None:
            self.is_email_verify = m.get('isEmailVerify')

        return self

