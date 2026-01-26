# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAlertContactRequest(DaraModel):
    def __init__(
        self,
        contact_name: str = None,
        ding_robot_webhook_url: str = None,
        email: str = None,
        phone_num: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        system_noc: bool = None,
    ):
        # The name of the alert contact.
        self.contact_name = contact_name
        # The webhook URL of the DingTalk chatbot. For more information about how to obtain the URL, see [Configure a DingTalk chatbot to send alert notifications](https://www.alibabacloud.com/help/zh/doc-detail/106247.htm). You must specify at least one of the following parameters: PhoneNum, Email, and DingRobotWebhookUrl.
        # 
        # >  Enter `alert` in the custom keyword field of DingTalk chatbot security settings.
        self.ding_robot_webhook_url = ding_robot_webhook_url
        # The email address of the alert contact. You must specify at least one of the following parameters: PhoneNum, Email, and DingRobotWebhookUrl.
        self.email = email
        # The mobile number of the alert contact. You must specify at least one of the following parameters: PhoneNum, Email, and DingRobotWebhookUrl.
        self.phone_num = phone_num
        # The ID of the region. Set the value to `cn-hangzhou`.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group. You can obtain the resource group ID in the **Resource Management** console.
        self.resource_group_id = resource_group_id
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

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.system_noc is not None:
            result['SystemNoc'] = self.system_noc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SystemNoc') is not None:
            self.system_noc = m.get('SystemNoc')

        return self

