# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cams20200606 import models as main_models
from darabonba.model import DaraModel

class ListMessengerSubscriptionTokenResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: List[main_models.ListMessengerSubscriptionTokenResponseBodyData] = None,
        message: str = None,
        next_page: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.next_page = next_page
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.next_page is not None:
            result['NextPage'] = self.next_page

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

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListMessengerSubscriptionTokenResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListMessengerSubscriptionTokenResponseBodyData(DaraModel):
    def __init__(
        self,
        creation_timestamp: int = None,
        custom_audience_id: str = None,
        next_eligible_time: int = None,
        notification_messages_reoptin: str = None,
        notification_messages_timezone: str = None,
        notification_messages_token: str = None,
        page_id: str = None,
        recipient_id: str = None,
        token_expiry_timestamp: int = None,
        topic_title: str = None,
        user_token_status: str = None,
    ):
        self.creation_timestamp = creation_timestamp
        self.custom_audience_id = custom_audience_id
        self.next_eligible_time = next_eligible_time
        self.notification_messages_reoptin = notification_messages_reoptin
        self.notification_messages_timezone = notification_messages_timezone
        self.notification_messages_token = notification_messages_token
        self.page_id = page_id
        # The customer\\"s Page-scoped ID (PSID)
        self.recipient_id = recipient_id
        self.token_expiry_timestamp = token_expiry_timestamp
        # The message\\"s title
        self.topic_title = topic_title
        self.user_token_status = user_token_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_timestamp is not None:
            result['CreationTimestamp'] = self.creation_timestamp

        if self.custom_audience_id is not None:
            result['CustomAudienceId'] = self.custom_audience_id

        if self.next_eligible_time is not None:
            result['NextEligibleTime'] = self.next_eligible_time

        if self.notification_messages_reoptin is not None:
            result['NotificationMessagesReoptin'] = self.notification_messages_reoptin

        if self.notification_messages_timezone is not None:
            result['NotificationMessagesTimezone'] = self.notification_messages_timezone

        if self.notification_messages_token is not None:
            result['NotificationMessagesToken'] = self.notification_messages_token

        if self.page_id is not None:
            result['PageId'] = self.page_id

        if self.recipient_id is not None:
            result['RecipientId'] = self.recipient_id

        if self.token_expiry_timestamp is not None:
            result['TokenExpiryTimestamp'] = self.token_expiry_timestamp

        if self.topic_title is not None:
            result['TopicTitle'] = self.topic_title

        if self.user_token_status is not None:
            result['UserTokenStatus'] = self.user_token_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTimestamp') is not None:
            self.creation_timestamp = m.get('CreationTimestamp')

        if m.get('CustomAudienceId') is not None:
            self.custom_audience_id = m.get('CustomAudienceId')

        if m.get('NextEligibleTime') is not None:
            self.next_eligible_time = m.get('NextEligibleTime')

        if m.get('NotificationMessagesReoptin') is not None:
            self.notification_messages_reoptin = m.get('NotificationMessagesReoptin')

        if m.get('NotificationMessagesTimezone') is not None:
            self.notification_messages_timezone = m.get('NotificationMessagesTimezone')

        if m.get('NotificationMessagesToken') is not None:
            self.notification_messages_token = m.get('NotificationMessagesToken')

        if m.get('PageId') is not None:
            self.page_id = m.get('PageId')

        if m.get('RecipientId') is not None:
            self.recipient_id = m.get('RecipientId')

        if m.get('TokenExpiryTimestamp') is not None:
            self.token_expiry_timestamp = m.get('TokenExpiryTimestamp')

        if m.get('TopicTitle') is not None:
            self.topic_title = m.get('TopicTitle')

        if m.get('UserTokenStatus') is not None:
            self.user_token_status = m.get('UserTokenStatus')

        return self

