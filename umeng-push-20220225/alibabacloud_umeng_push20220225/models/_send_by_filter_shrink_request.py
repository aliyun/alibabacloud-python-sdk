# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_umeng_push20220225 import models as main_models
from darabonba.model import DaraModel

class SendByFilterShrinkRequest(DaraModel):
    def __init__(
        self,
        android_payload_shrink: str = None,
        android_short_payload: main_models.AndroidShortPayload = None,
        channel_properties_shrink: str = None,
        description: str = None,
        filter: str = None,
        harmony_payload_shrink: str = None,
        ios_payload_shrink: str = None,
        policy_shrink: str = None,
        production_mode: bool = None,
        receipt_type: int = None,
        receipt_url: str = None,
        third_party_id: str = None,
        callback_params: str = None,
    ):
        self.android_payload_shrink = android_payload_shrink
        self.android_short_payload = android_short_payload
        self.channel_properties_shrink = channel_properties_shrink
        self.description = description
        self.filter = filter
        self.harmony_payload_shrink = harmony_payload_shrink
        self.ios_payload_shrink = ios_payload_shrink
        self.policy_shrink = policy_shrink
        self.production_mode = production_mode
        self.receipt_type = receipt_type
        self.receipt_url = receipt_url
        self.third_party_id = third_party_id
        self.callback_params = callback_params

    def validate(self):
        if self.android_short_payload:
            self.android_short_payload.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.android_payload_shrink is not None:
            result['AndroidPayload'] = self.android_payload_shrink

        if self.android_short_payload is not None:
            result['AndroidShortPayload'] = self.android_short_payload.to_map()

        if self.channel_properties_shrink is not None:
            result['ChannelProperties'] = self.channel_properties_shrink

        if self.description is not None:
            result['Description'] = self.description

        if self.filter is not None:
            result['Filter'] = self.filter

        if self.harmony_payload_shrink is not None:
            result['HarmonyPayload'] = self.harmony_payload_shrink

        if self.ios_payload_shrink is not None:
            result['IosPayload'] = self.ios_payload_shrink

        if self.policy_shrink is not None:
            result['Policy'] = self.policy_shrink

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
            self.android_payload_shrink = m.get('AndroidPayload')

        if m.get('AndroidShortPayload') is not None:
            temp_model = main_models.AndroidShortPayload()
            self.android_short_payload = temp_model.from_map(m.get('AndroidShortPayload'))

        if m.get('ChannelProperties') is not None:
            self.channel_properties_shrink = m.get('ChannelProperties')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('HarmonyPayload') is not None:
            self.harmony_payload_shrink = m.get('HarmonyPayload')

        if m.get('IosPayload') is not None:
            self.ios_payload_shrink = m.get('IosPayload')

        if m.get('Policy') is not None:
            self.policy_shrink = m.get('Policy')

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

