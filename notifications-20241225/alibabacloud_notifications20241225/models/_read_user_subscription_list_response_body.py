# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_notifications20241225 import models as main_models
from darabonba.model import DaraModel

class ReadUserSubscriptionListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ReadUserSubscriptionListResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code of the operation.
        # 
        # This parameter is required.
        self.code = code
        # The query result.
        self.data = data
        # The message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # - true: The call was successful.
        # - false: The call failed.
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
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

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

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ReadUserSubscriptionListResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ReadUserSubscriptionListResponseBodyData(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        category_code: str = None,
        category_desc: str = None,
        category_group_code: str = None,
        category_group_name: str = None,
        category_name: str = None,
        channel_configs: List[main_models.ReadUserSubscriptionListResponseBodyDataChannelConfigs] = None,
        contact: main_models.ReadUserSubscriptionListResponseBodyDataContact = None,
        receive_time_list: List[int] = None,
    ):
        # The Alibaba Cloud account ID.
        self.ali_uid = ali_uid
        # The message category code.
        self.category_code = category_code
        # The description of the message category.
        self.category_desc = category_desc
        # The category group code.
        self.category_group_code = category_group_code
        # The category group name.
        self.category_group_name = category_group_name
        # The message category name.
        self.category_name = category_name
        # The channel list.
        self.channel_configs = channel_configs
        # The contact.
        self.contact = contact
        # The receiving time list.
        self.receive_time_list = receive_time_list

    def validate(self):
        if self.channel_configs:
            for v1 in self.channel_configs:
                 if v1:
                    v1.validate()
        if self.contact:
            self.contact.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.category_code is not None:
            result['CategoryCode'] = self.category_code

        if self.category_desc is not None:
            result['CategoryDesc'] = self.category_desc

        if self.category_group_code is not None:
            result['CategoryGroupCode'] = self.category_group_code

        if self.category_group_name is not None:
            result['CategoryGroupName'] = self.category_group_name

        if self.category_name is not None:
            result['CategoryName'] = self.category_name

        result['ChannelConfigs'] = []
        if self.channel_configs is not None:
            for k1 in self.channel_configs:
                result['ChannelConfigs'].append(k1.to_map() if k1 else None)

        if self.contact is not None:
            result['Contact'] = self.contact.to_map()

        if self.receive_time_list is not None:
            result['ReceiveTimeList'] = self.receive_time_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('CategoryCode') is not None:
            self.category_code = m.get('CategoryCode')

        if m.get('CategoryDesc') is not None:
            self.category_desc = m.get('CategoryDesc')

        if m.get('CategoryGroupCode') is not None:
            self.category_group_code = m.get('CategoryGroupCode')

        if m.get('CategoryGroupName') is not None:
            self.category_group_name = m.get('CategoryGroupName')

        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')

        self.channel_configs = []
        if m.get('ChannelConfigs') is not None:
            for k1 in m.get('ChannelConfigs'):
                temp_model = main_models.ReadUserSubscriptionListResponseBodyDataChannelConfigs()
                self.channel_configs.append(temp_model.from_map(k1))

        if m.get('Contact') is not None:
            temp_model = main_models.ReadUserSubscriptionListResponseBodyDataContact()
            self.contact = temp_model.from_map(m.get('Contact'))

        if m.get('ReceiveTimeList') is not None:
            self.receive_time_list = m.get('ReceiveTimeList')

        return self

class ReadUserSubscriptionListResponseBodyDataContact(DaraModel):
    def __init__(
        self,
        common_contacts: List[main_models.ReadUserSubscriptionListResponseBodyDataContactCommonContacts] = None,
        webhook_contacts: List[main_models.ReadUserSubscriptionListResponseBodyDataContactWebhookContacts] = None,
    ):
        # The Account Center contact list.
        self.common_contacts = common_contacts
        # The webhook contact list.
        self.webhook_contacts = webhook_contacts

    def validate(self):
        if self.common_contacts:
            for v1 in self.common_contacts:
                 if v1:
                    v1.validate()
        if self.webhook_contacts:
            for v1 in self.webhook_contacts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CommonContacts'] = []
        if self.common_contacts is not None:
            for k1 in self.common_contacts:
                result['CommonContacts'].append(k1.to_map() if k1 else None)

        result['WebhookContacts'] = []
        if self.webhook_contacts is not None:
            for k1 in self.webhook_contacts:
                result['WebhookContacts'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.common_contacts = []
        if m.get('CommonContacts') is not None:
            for k1 in m.get('CommonContacts'):
                temp_model = main_models.ReadUserSubscriptionListResponseBodyDataContactCommonContacts()
                self.common_contacts.append(temp_model.from_map(k1))

        self.webhook_contacts = []
        if m.get('WebhookContacts') is not None:
            for k1 in m.get('WebhookContacts'):
                temp_model = main_models.ReadUserSubscriptionListResponseBodyDataContactWebhookContacts()
                self.webhook_contacts.append(temp_model.from_map(k1))

        return self

class ReadUserSubscriptionListResponseBodyDataContactWebhookContacts(DaraModel):
    def __init__(
        self,
        contact_id: int = None,
        contact_name: str = None,
        message_source: main_models.ReadUserSubscriptionListResponseBodyDataContactWebhookContactsMessageSource = None,
        security_token: str = None,
        server_url: str = None,
        webhook_type: str = None,
    ):
        # The contact ID.
        self.contact_id = contact_id
        # The name of the Account Center contact.
        self.contact_name = contact_name
        # The message source.
        self.message_source = message_source
        # The security token.
        self.security_token = security_token
        # The webhook URL.
        self.server_url = server_url
        # The webhook type.
        self.webhook_type = webhook_type

    def validate(self):
        if self.message_source:
            self.message_source.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id

        if self.contact_name is not None:
            result['ContactName'] = self.contact_name

        if self.message_source is not None:
            result['MessageSource'] = self.message_source.to_map()

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.server_url is not None:
            result['ServerUrl'] = self.server_url

        if self.webhook_type is not None:
            result['WebhookType'] = self.webhook_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')

        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')

        if m.get('MessageSource') is not None:
            temp_model = main_models.ReadUserSubscriptionListResponseBodyDataContactWebhookContactsMessageSource()
            self.message_source = temp_model.from_map(m.get('MessageSource'))

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('ServerUrl') is not None:
            self.server_url = m.get('ServerUrl')

        if m.get('WebhookType') is not None:
            self.webhook_type = m.get('WebhookType')

        return self

class ReadUserSubscriptionListResponseBodyDataContactWebhookContactsMessageSource(DaraModel):
    def __init__(
        self,
        keyword_blacklist: List[str] = None,
        keyword_whitelist: List[str] = None,
    ):
        # The blacklist.
        self.keyword_blacklist = keyword_blacklist
        # The whitelist.
        self.keyword_whitelist = keyword_whitelist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keyword_blacklist is not None:
            result['KeywordBlacklist'] = self.keyword_blacklist

        if self.keyword_whitelist is not None:
            result['KeywordWhitelist'] = self.keyword_whitelist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeywordBlacklist') is not None:
            self.keyword_blacklist = m.get('KeywordBlacklist')

        if m.get('KeywordWhitelist') is not None:
            self.keyword_whitelist = m.get('KeywordWhitelist')

        return self

class ReadUserSubscriptionListResponseBodyDataContactCommonContacts(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        contact_email: str = None,
        contact_id: int = None,
        contact_mobile: str = None,
        contact_name: str = None,
        email_confirmed: bool = None,
        message_source: main_models.ReadUserSubscriptionListResponseBodyDataContactCommonContactsMessageSource = None,
        mobile_confirmed: bool = None,
        position: str = None,
    ):
        # The Alibaba Cloud account ID.
        self.ali_uid = ali_uid
        # The email address of the contact.
        self.contact_email = contact_email
        # The contact ID.
        self.contact_id = contact_id
        # The masked mobile phone number of the Account Center contact.
        self.contact_mobile = contact_mobile
        # The name of the Account Center contact.
        self.contact_name = contact_name
        # Indicates whether the email address is verified.
        self.email_confirmed = email_confirmed
        # The message source.
        self.message_source = message_source
        # Indicates whether the mobile phone number of the Account Center contact is verified.
        self.mobile_confirmed = mobile_confirmed
        # The position of the Account Center contact.
        self.position = position

    def validate(self):
        if self.message_source:
            self.message_source.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email

        if self.contact_id is not None:
            result['ContactId'] = self.contact_id

        if self.contact_mobile is not None:
            result['ContactMobile'] = self.contact_mobile

        if self.contact_name is not None:
            result['ContactName'] = self.contact_name

        if self.email_confirmed is not None:
            result['EmailConfirmed'] = self.email_confirmed

        if self.message_source is not None:
            result['MessageSource'] = self.message_source.to_map()

        if self.mobile_confirmed is not None:
            result['MobileConfirmed'] = self.mobile_confirmed

        if self.position is not None:
            result['Position'] = self.position

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')

        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')

        if m.get('ContactMobile') is not None:
            self.contact_mobile = m.get('ContactMobile')

        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')

        if m.get('EmailConfirmed') is not None:
            self.email_confirmed = m.get('EmailConfirmed')

        if m.get('MessageSource') is not None:
            temp_model = main_models.ReadUserSubscriptionListResponseBodyDataContactCommonContactsMessageSource()
            self.message_source = temp_model.from_map(m.get('MessageSource'))

        if m.get('MobileConfirmed') is not None:
            self.mobile_confirmed = m.get('MobileConfirmed')

        if m.get('Position') is not None:
            self.position = m.get('Position')

        return self

class ReadUserSubscriptionListResponseBodyDataContactCommonContactsMessageSource(DaraModel):
    def __init__(
        self,
        keyword_blacklist: List[str] = None,
        keyword_whitelist: List[str] = None,
    ):
        # The blacklist.
        self.keyword_blacklist = keyword_blacklist
        # The whitelist.
        self.keyword_whitelist = keyword_whitelist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keyword_blacklist is not None:
            result['KeywordBlacklist'] = self.keyword_blacklist

        if self.keyword_whitelist is not None:
            result['KeywordWhitelist'] = self.keyword_whitelist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeywordBlacklist') is not None:
            self.keyword_blacklist = m.get('KeywordBlacklist')

        if m.get('KeywordWhitelist') is not None:
            self.keyword_whitelist = m.get('KeywordWhitelist')

        return self

class ReadUserSubscriptionListResponseBodyDataChannelConfigs(DaraModel):
    def __init__(
        self,
        channel_type: str = None,
        checked_state: str = None,
        default_checked: str = None,
        fatigue_day_limit: int = None,
        optional: str = None,
    ):
        # The channel type.
        self.channel_type = channel_type
        # Indicates whether the subscription is configured.
        self.checked_state = checked_state
        # Indicates whether the option is selected by default.
        self.default_checked = default_checked
        # The fatigue limit.
        self.fatigue_day_limit = fatigue_day_limit
        # Indicates whether the option can be modified.
        self.optional = optional

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type

        if self.checked_state is not None:
            result['CheckedState'] = self.checked_state

        if self.default_checked is not None:
            result['DefaultChecked'] = self.default_checked

        if self.fatigue_day_limit is not None:
            result['FatigueDayLimit'] = self.fatigue_day_limit

        if self.optional is not None:
            result['Optional'] = self.optional

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')

        if m.get('CheckedState') is not None:
            self.checked_state = m.get('CheckedState')

        if m.get('DefaultChecked') is not None:
            self.default_checked = m.get('DefaultChecked')

        if m.get('FatigueDayLimit') is not None:
            self.fatigue_day_limit = m.get('FatigueDayLimit')

        if m.get('Optional') is not None:
            self.optional = m.get('Optional')

        return self

