# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAlertContactRequest(DaraModel):
    def __init__(
        self,
        contact_id: int = None,
        contact_name: str = None,
        ding_robot_webhook_url: str = None,
        email: str = None,
        phone_num: str = None,
        region_id: str = None,
        system_noc: bool = None,
    ):
        # The ID of the alert contact to be updated. You can call the SearchAlertContact operation to query the contact ID. For more information, see [SearchAlertContact](https://help.aliyun.com/document_detail/130703.html).
        # 
        # This parameter is required.
        self.contact_id = contact_id
        # The new name of the alert contact.
        self.contact_name = contact_name
        # The new webhook URL of the DingTalk chatbot. For more information, see [Configure a DingTalk chatbot to send alert notifications](https://help.aliyun.com/document_detail/106247.html). You must specify at least one of the following parameters: PhoneNum, Email, and DingRobotWebhookUrl.
        # 
        # >  If you do not specify this parameter, the original parameter value is deleted. If you specify this parameter, the original parameter value is updated.
        self.ding_robot_webhook_url = ding_robot_webhook_url
        # The new email address of the alert contact. You must specify at least one of the following parameters: PhoneNum, Email, and DingRobotWebhookUrl.
        # 
        # >  If you do not specify this parameter, the original parameter value is deleted. If you specify this parameter, the original parameter value is updated.
        self.email = email
        # The new mobile phone number of the alert contact. You must specify at least one of the following parameters: PhoneNum, Email, and DingRobotWebhookUrl.
        # 
        # >  If you do not specify this parameter, the original parameter value is deleted. If you specify this parameter, the original parameter value is updated.
        self.phone_num = phone_num
        # The ID of the region. Set the value to `cn-hangzhou`.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Specifies whether the alert contact receives system notifications. Valid values:
        # 
        # *   `true`: The alert contact receives system notifications.
        # *   `false`: The alert contact does not receive system notifications.
        self.system_noc = system_noc

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

        if self.ding_robot_webhook_url is not None:
            result['DingRobotWebhookUrl'] = self.ding_robot_webhook_url

        if self.email is not None:
            result['Email'] = self.email

        if self.phone_num is not None:
            result['PhoneNum'] = self.phone_num

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.system_noc is not None:
            result['SystemNoc'] = self.system_noc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')

        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')

        if m.get('DingRobotWebhookUrl') is not None:
            self.ding_robot_webhook_url = m.get('DingRobotWebhookUrl')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('PhoneNum') is not None:
            self.phone_num = m.get('PhoneNum')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SystemNoc') is not None:
            self.system_noc = m.get('SystemNoc')

        return self

