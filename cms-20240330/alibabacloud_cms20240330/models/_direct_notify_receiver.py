# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DirectNotifyReceiver(DaraModel):
    def __init__(
        self,
        channels: List[str] = None,
        identifiers: List[str] = None,
        target_type: str = None,
    ):
        # The list of notification channels. This parameter is valid only for person-based types (CONTACT/GROUP/DUTY). Valid values: SMS, CALL, EMAIL.
        self.channels = channels
        # The list of Notification Recipient identifiers. For person-based types, the identifiers are contacts, contact groups, or on-call schedule identifiers. For IM-based types, the identifiers are webhook identifiers.
        self.identifiers = identifiers
        # The Notification Recipient type. Person-object types (CONTACT/GROUP/DUTY) require channels to specify notification methods. IM-object types (DINGTALK/FEISHU/SLACK/WEIXIN/WEBHOOK) do not require channels.
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channels is not None:
            result['channels'] = self.channels

        if self.identifiers is not None:
            result['identifiers'] = self.identifiers

        if self.target_type is not None:
            result['targetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channels') is not None:
            self.channels = m.get('channels')

        if m.get('identifiers') is not None:
            self.identifiers = m.get('identifiers')

        if m.get('targetType') is not None:
            self.target_type = m.get('targetType')

        return self

