# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateOrUpdateContactRequest(DaraModel):
    def __init__(
        self,
        contact_id: int = None,
        contact_name: str = None,
        corp_user_id: str = None,
        ding_robot_url: str = None,
        email: str = None,
        is_email_verify: bool = None,
        phone: str = None,
        reissue_send_notice: int = None,
        resource_group_id: str = None,
    ):
        # The ID of the alert contact.
        # 
        # *   If you do not specify this parameter, a new alert contact is created.
        # *   If you specify this parameter, the specified alert contact is modified.
        self.contact_id = contact_id
        # The name of the alert contact.
        # 
        # This parameter is required.
        self.contact_name = contact_name
        # The ID of the alert contact that is shown to the enterprise when the contact is mentioned with the at sign (@) by a third-party instant messaging (IM) tool.
        self.corp_user_id = corp_user_id
        # The webhook URL of the DingTalk chatbot.
        self.ding_robot_url = ding_robot_url
        # The email address of the alert contact.
        # 
        # > You must specify at least one of the **Phone** and **Email** parameters. Each mobile number or email address can be used for only one alert contact.
        self.email = email
        # Specifies whether the email address is verified.
        self.is_email_verify = is_email_verify
        # The mobile number of the alert contact.
        # 
        # > You must specify at least one of the **Phone** and **Email** parameters. Each mobile number or email address can be used for only one alert contact.
        self.phone = phone
        # The operation that you want to perform if phone calls fail to be answered. Valid values:
        # 
        # *   0: No operation is performed.
        # *   1: A phone call is made again.
        # *   2: A text message is sent.
        # *   3 (default value): The global default value is used.
        self.reissue_send_notice = reissue_send_notice
        # The resource group ID.
        self.resource_group_id = resource_group_id

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

        if self.corp_user_id is not None:
            result['CorpUserId'] = self.corp_user_id

        if self.ding_robot_url is not None:
            result['DingRobotUrl'] = self.ding_robot_url

        if self.email is not None:
            result['Email'] = self.email

        if self.is_email_verify is not None:
            result['IsEmailVerify'] = self.is_email_verify

        if self.phone is not None:
            result['Phone'] = self.phone

        if self.reissue_send_notice is not None:
            result['ReissueSendNotice'] = self.reissue_send_notice

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')

        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')

        if m.get('CorpUserId') is not None:
            self.corp_user_id = m.get('CorpUserId')

        if m.get('DingRobotUrl') is not None:
            self.ding_robot_url = m.get('DingRobotUrl')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('IsEmailVerify') is not None:
            self.is_email_verify = m.get('IsEmailVerify')

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        if m.get('ReissueSendNotice') is not None:
            self.reissue_send_notice = m.get('ReissueSendNotice')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

