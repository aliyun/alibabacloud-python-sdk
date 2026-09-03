# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_umeng_push20220225 import models as main_models
from darabonba.model import DaraModel

class SendByFilterRequest(DaraModel):
    def __init__(
        self,
        android_payload: main_models.AndroidPayload = None,
        android_short_payload: main_models.AndroidShortPayload = None,
        channel_properties: main_models.ChannelProperties = None,
        description: str = None,
        filter: str = None,
        harmony_payload: main_models.HarmonyPayload = None,
        ios_payload: main_models.IosPayload = None,
        policy: main_models.Policy = None,
        production_mode: bool = None,
        receipt_type: int = None,
        receipt_url: str = None,
        third_party_id: str = None,
        callback_params: str = None,
    ):
        self.android_payload = android_payload
        self.android_short_payload = android_short_payload
        self.channel_properties = channel_properties
        self.description = description
        self.filter = filter
        self.harmony_payload = harmony_payload
        self.ios_payload = ios_payload
        self.policy = policy
        self.production_mode = production_mode
        self.receipt_type = receipt_type
        self.receipt_url = receipt_url
        self.third_party_id = third_party_id
        self.callback_params = callback_params

    def validate(self):
        if self.android_payload:
            self.android_payload.validate()
        if self.android_short_payload:
            self.android_short_payload.validate()
        if self.channel_properties:
            self.channel_properties.validate()
        if self.harmony_payload:
            self.harmony_payload.validate()
        if self.ios_payload:
            self.ios_payload.validate()
        if self.policy:
            self.policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.android_payload is not None:
            result['AndroidPayload'] = self.android_payload.to_map()

        if self.android_short_payload is not None:
            result['AndroidShortPayload'] = self.android_short_payload.to_map()

        if self.channel_properties is not None:
            result['ChannelProperties'] = self.channel_properties.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.filter is not None:
            result['Filter'] = self.filter

        if self.harmony_payload is not None:
            result['HarmonyPayload'] = self.harmony_payload.to_map()

        if self.ios_payload is not None:
            result['IosPayload'] = self.ios_payload.to_map()

        if self.policy is not None:
            result['Policy'] = self.policy.to_map()

        if self.production_mode is not None:
            result['ProductionMode'] = self.production_mode

        if self.receipt_type is not None:
            result['ReceiptType'] = self.receipt_type

        if self.receipt_url is not None:
            result['ReceiptUrl'] = self.receipt_url

        if self.third_party_id is not None:
            result['ThirdPartyId'] = self.third_party_id

        if self.callback_params is not None:
            result['callbackParams'] = self.callback_params

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidPayload') is not None:
            temp_model = main_models.AndroidPayload()
            self.android_payload = temp_model.from_map(m.get('AndroidPayload'))

        if m.get('AndroidShortPayload') is not None:
            temp_model = main_models.AndroidShortPayload()
            self.android_short_payload = temp_model.from_map(m.get('AndroidShortPayload'))

        if m.get('ChannelProperties') is not None:
            temp_model = main_models.ChannelProperties()
            self.channel_properties = temp_model.from_map(m.get('ChannelProperties'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('HarmonyPayload') is not None:
            temp_model = main_models.HarmonyPayload()
            self.harmony_payload = temp_model.from_map(m.get('HarmonyPayload'))

        if m.get('IosPayload') is not None:
            temp_model = main_models.IosPayload()
            self.ios_payload = temp_model.from_map(m.get('IosPayload'))

        if m.get('Policy') is not None:
            temp_model = main_models.Policy()
            self.policy = temp_model.from_map(m.get('Policy'))

        if m.get('ProductionMode') is not None:
            self.production_mode = m.get('ProductionMode')

        if m.get('ReceiptType') is not None:
            self.receipt_type = m.get('ReceiptType')

        if m.get('ReceiptUrl') is not None:
            self.receipt_url = m.get('ReceiptUrl')

        if m.get('ThirdPartyId') is not None:
            self.third_party_id = m.get('ThirdPartyId')

        if m.get('callbackParams') is not None:
            self.callback_params = m.get('callbackParams')

        return self

