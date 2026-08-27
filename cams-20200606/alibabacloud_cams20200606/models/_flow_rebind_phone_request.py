# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cams20200606 import models as main_models
from darabonba.model import DaraModel

class FlowRebindPhoneRequest(DaraModel):
    def __init__(
        self,
        channel_code: str = None,
        channel_type: str = None,
        flow_code: str = None,
        flow_version: str = None,
        multi_waba_phone_numbers: List[main_models.FlowRebindPhoneRequestMultiWabaPhoneNumbers] = None,
        owner_id: int = None,
        phone_numbers: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        waba_id: str = None,
    ):
        # The message channel code, which is the channel ID. You can view the channel ID in the [Channel Management](https://chatapp.console.aliyun.com/ChannelsManagement) console.
        self.channel_code = channel_code
        # The message channel type. Valid values:
        # 
        # - INSTAGRAM
        # 
        # - WHATSAPP
        # 
        # - MESSENGER
        # 
        # <props="intl">- VIBER
        # 
        # This parameter is required.
        self.channel_type = channel_type
        # The flow code. You can view this in the [Flow Builder](https://chatapp.console.aliyun.com/ChatFlowBuilder) console.
        # 
        # This parameter is required.
        self.flow_code = flow_code
        # The flow version. In the [Flow Builder](https://chatapp.console.aliyun.com/ChatFlowBuilder) console, click the flow name to open the flow editor canvas and view the flow version.
        self.flow_version = flow_version
        # The multi-WABA binding configurations.
        self.multi_waba_phone_numbers = multi_waba_phone_numbers
        self.owner_id = owner_id
        # The list of phone numbers, PageIds, or AccountIds<props="intl">, or ServiceIds under the channel instance.
        self.phone_numbers = phone_numbers
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The WABA account ID, PageId, or AccountId<props="intl">, or ServiceId.
        # 
        # - If ChannelType is set to WHATSAPP, specify the WABA account ID. You can view the WABA account ID in Channel Management > Manage > WABA Management.
        # 
        # - If ChannelType is not set to WHATSAPP, specify the PageId for MESSENGER, the AccountId for INSTAGRAM<props="intl">, or the ServiceId for VIBER.
        self.waba_id = waba_id

    def validate(self):
        if self.multi_waba_phone_numbers:
            for v1 in self.multi_waba_phone_numbers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_code is not None:
            result['ChannelCode'] = self.channel_code

        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type

        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code

        if self.flow_version is not None:
            result['FlowVersion'] = self.flow_version

        result['MultiWabaPhoneNumbers'] = []
        if self.multi_waba_phone_numbers is not None:
            for k1 in self.multi_waba_phone_numbers:
                result['MultiWabaPhoneNumbers'].append(k1.to_map() if k1 else None)

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.phone_numbers is not None:
            result['PhoneNumbers'] = self.phone_numbers

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.waba_id is not None:
            result['WabaId'] = self.waba_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelCode') is not None:
            self.channel_code = m.get('ChannelCode')

        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')

        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')

        if m.get('FlowVersion') is not None:
            self.flow_version = m.get('FlowVersion')

        self.multi_waba_phone_numbers = []
        if m.get('MultiWabaPhoneNumbers') is not None:
            for k1 in m.get('MultiWabaPhoneNumbers'):
                temp_model = main_models.FlowRebindPhoneRequestMultiWabaPhoneNumbers()
                self.multi_waba_phone_numbers.append(temp_model.from_map(k1))

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PhoneNumbers') is not None:
            self.phone_numbers = m.get('PhoneNumbers')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('WabaId') is not None:
            self.waba_id = m.get('WabaId')

        return self

class FlowRebindPhoneRequestMultiWabaPhoneNumbers(DaraModel):
    def __init__(
        self,
        channel_code: str = None,
        phone_numbers: List[str] = None,
        waba_id: str = None,
    ):
        # The channel code.
        self.channel_code = channel_code
        # The list of phone numbers.
        self.phone_numbers = phone_numbers
        # wabaId
        self.waba_id = waba_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_code is not None:
            result['ChannelCode'] = self.channel_code

        if self.phone_numbers is not None:
            result['PhoneNumbers'] = self.phone_numbers

        if self.waba_id is not None:
            result['WabaId'] = self.waba_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelCode') is not None:
            self.channel_code = m.get('ChannelCode')

        if m.get('PhoneNumbers') is not None:
            self.phone_numbers = m.get('PhoneNumbers')

        if m.get('WabaId') is not None:
            self.waba_id = m.get('WabaId')

        return self

