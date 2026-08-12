# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_riskmanagement20260424 import models as main_models
from darabonba.model import DaraModel

class GetNotificationContactsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.GetNotificationContactsResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code.
        # 
        # - **200**: Success.
        # - **Other (400, 500)**: Failure.
        self.code = code
        # The query result.
        self.data = data
        # The prompt message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the operation is successful.
        # 
        # - **true**: Success.
        # - **false**: Failure.
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
                temp_model = main_models.GetNotificationContactsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetNotificationContactsResponseBodyData(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        category_code: str = None,
        category_desc: str = None,
        category_group_code: str = None,
        category_group_name: str = None,
        category_name: str = None,
        channel_configs: List[main_models.GetNotificationContactsResponseBodyDataChannelConfigs] = None,
        choose_all_channel: bool = None,
        contact_info_list: List[main_models.GetNotificationContactsResponseBodyDataContactInfoList] = None,
    ):
        # The Alibaba Cloud account ID.
        self.ali_uid = ali_uid
        # The message category code.
        self.category_code = category_code
        # The message category description.
        self.category_desc = category_desc
        # The category group code.
        self.category_group_code = category_group_code
        # The category group name.
        self.category_group_name = category_group_name
        # The message category name.
        self.category_name = category_name
        # The channel list.
        self.channel_configs = channel_configs
        # Indicates whether all notification methods are selected.
        # 
        # - **true**
        # - **false**
        self.choose_all_channel = choose_all_channel
        # The general contact list.
        self.contact_info_list = contact_info_list

    def validate(self):
        if self.channel_configs:
            for v1 in self.channel_configs:
                 if v1:
                    v1.validate()
        if self.contact_info_list:
            for v1 in self.contact_info_list:
                 if v1:
                    v1.validate()

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

        if self.choose_all_channel is not None:
            result['ChooseAllChannel'] = self.choose_all_channel

        result['ContactInfoList'] = []
        if self.contact_info_list is not None:
            for k1 in self.contact_info_list:
                result['ContactInfoList'].append(k1.to_map() if k1 else None)

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
                temp_model = main_models.GetNotificationContactsResponseBodyDataChannelConfigs()
                self.channel_configs.append(temp_model.from_map(k1))

        if m.get('ChooseAllChannel') is not None:
            self.choose_all_channel = m.get('ChooseAllChannel')

        self.contact_info_list = []
        if m.get('ContactInfoList') is not None:
            for k1 in m.get('ContactInfoList'):
                temp_model = main_models.GetNotificationContactsResponseBodyDataContactInfoList()
                self.contact_info_list.append(temp_model.from_map(k1))

        return self

class GetNotificationContactsResponseBodyDataContactInfoList(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        bind_contact: bool = None,
        contact_email: str = None,
        contact_id: int = None,
        contact_mobile: str = None,
        contact_name: str = None,
        email_confirmed: bool = None,
        mobile_confirmed: bool = None,
        position: str = None,
    ):
        # The Alibaba Cloud account ID.
        self.ali_uid = ali_uid
        # Indicates whether the contact is bound.
        # 
        # - **true**
        # - **fasle**
        self.bind_contact = bind_contact
        # The contact email address.
        self.contact_email = contact_email
        # The Account Center contact ID. A value of 0 indicates the account contact.
        self.contact_id = contact_id
        # The Account Center contact mobile number (masked).
        self.contact_mobile = contact_mobile
        # The Account Center contact name.
        self.contact_name = contact_name
        # Indicates whether the email address is verified.
        # 
        # - **true**
        # - **false**
        self.email_confirmed = email_confirmed
        # Indicates whether the Account Center contact mobile number is verified.
        # 
        # - **true**
        # - **false**
        self.mobile_confirmed = mobile_confirmed
        # The Account Center contact position.
        self.position = position

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.bind_contact is not None:
            result['BindContact'] = self.bind_contact

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

        if self.mobile_confirmed is not None:
            result['MobileConfirmed'] = self.mobile_confirmed

        if self.position is not None:
            result['Position'] = self.position

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('BindContact') is not None:
            self.bind_contact = m.get('BindContact')

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

        if m.get('MobileConfirmed') is not None:
            self.mobile_confirmed = m.get('MobileConfirmed')

        if m.get('Position') is not None:
            self.position = m.get('Position')

        return self

class GetNotificationContactsResponseBodyDataChannelConfigs(DaraModel):
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
        # 
        # - **NO**
        # - **YES**
        self.checked_state = checked_state
        # Indicates whether the channel is selected by default.
        # 
        # - **NO**
        # - **YES**
        self.default_checked = default_checked
        # The fatigue limit.
        self.fatigue_day_limit = fatigue_day_limit
        # Indicates whether the channel is modifiable.
        # 
        # - **NO**
        # - **YES**
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

