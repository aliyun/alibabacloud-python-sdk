# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAppNotificationSceneRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        channels_json: str = None,
        description: str = None,
        email_fields_json: str = None,
        email_limit_json: str = None,
        email_recipient_ids_json: str = None,
        name: str = None,
        phone_recipient_ids_json: str = None,
        sms_fields_json: str = None,
        sms_limit_json: str = None,
        table_name: str = None,
        trigger_events_json: str = None,
    ):
        # The business ID.
        self.biz_id = biz_id
        # The notification channels in a JSON array string, such as ["sms","email"].
        self.channels_json = channels_json
        # The description of the scenario.
        self.description = description
        # The email notification fields in a JSON array string. A maximum of 10 fields are supported.
        self.email_fields_json = email_fields_json
        # The email sending limit in a JSON string, including the minInterval and dailyLimit fields.
        self.email_limit_json = email_limit_json
        # The list of email recipient IDs in a JSON array string.
        self.email_recipient_ids_json = email_recipient_ids_json
        # The name of the scenario.
        self.name = name
        # The list of SMS recipient IDs in a JSON array string.
        self.phone_recipient_ids_json = phone_recipient_ids_json
        # The SMS notification fields in a JSON array string. A maximum of 3 fields are supported.
        self.sms_fields_json = sms_fields_json
        # The SMS sending limit in a JSON string, including the minInterval and dailyLimit fields.
        self.sms_limit_json = sms_limit_json
        # The name of the monitored data table.
        self.table_name = table_name
        # The trigger events in a JSON array string, such as ["INSERT","UPDATE","DELETE"].
        self.trigger_events_json = trigger_events_json

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.channels_json is not None:
            result['ChannelsJson'] = self.channels_json

        if self.description is not None:
            result['Description'] = self.description

        if self.email_fields_json is not None:
            result['EmailFieldsJson'] = self.email_fields_json

        if self.email_limit_json is not None:
            result['EmailLimitJson'] = self.email_limit_json

        if self.email_recipient_ids_json is not None:
            result['EmailRecipientIdsJson'] = self.email_recipient_ids_json

        if self.name is not None:
            result['Name'] = self.name

        if self.phone_recipient_ids_json is not None:
            result['PhoneRecipientIdsJson'] = self.phone_recipient_ids_json

        if self.sms_fields_json is not None:
            result['SmsFieldsJson'] = self.sms_fields_json

        if self.sms_limit_json is not None:
            result['SmsLimitJson'] = self.sms_limit_json

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.trigger_events_json is not None:
            result['TriggerEventsJson'] = self.trigger_events_json

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('ChannelsJson') is not None:
            self.channels_json = m.get('ChannelsJson')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EmailFieldsJson') is not None:
            self.email_fields_json = m.get('EmailFieldsJson')

        if m.get('EmailLimitJson') is not None:
            self.email_limit_json = m.get('EmailLimitJson')

        if m.get('EmailRecipientIdsJson') is not None:
            self.email_recipient_ids_json = m.get('EmailRecipientIdsJson')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PhoneRecipientIdsJson') is not None:
            self.phone_recipient_ids_json = m.get('PhoneRecipientIdsJson')

        if m.get('SmsFieldsJson') is not None:
            self.sms_fields_json = m.get('SmsFieldsJson')

        if m.get('SmsLimitJson') is not None:
            self.sms_limit_json = m.get('SmsLimitJson')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TriggerEventsJson') is not None:
            self.trigger_events_json = m.get('TriggerEventsJson')

        return self

