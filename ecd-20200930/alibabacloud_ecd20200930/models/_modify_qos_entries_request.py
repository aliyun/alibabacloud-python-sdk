# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyQosEntriesRequest(DaraModel):
    def __init__(
        self,
        auth_android_id: List[str] = None,
        auth_desktop_group_id: List[str] = None,
        auth_desktop_id: List[str] = None,
        qos_rule_id: str = None,
        revoke_android_id: List[str] = None,
        revoke_desktop_group_id: List[str] = None,
        revoke_desktop_id: List[str] = None,
    ):
        # The IDs of the cloud phones to bind to the QoS rule.
        self.auth_android_id = auth_android_id
        self.auth_desktop_group_id = auth_desktop_group_id
        # The IDs of the cloud desktops to bind to the QoS rule.
        self.auth_desktop_id = auth_desktop_id
        # The ID of the QoS rule.
        # 
        # This parameter is required.
        self.qos_rule_id = qos_rule_id
        # The IDs of the cloud phones to unbind from the QoS rule.
        self.revoke_android_id = revoke_android_id
        self.revoke_desktop_group_id = revoke_desktop_group_id
        # The IDs of the cloud desktops to unbind from the QoS rule.
        self.revoke_desktop_id = revoke_desktop_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_android_id is not None:
            result['AuthAndroidId'] = self.auth_android_id

        if self.auth_desktop_group_id is not None:
            result['AuthDesktopGroupId'] = self.auth_desktop_group_id

        if self.auth_desktop_id is not None:
            result['AuthDesktopId'] = self.auth_desktop_id

        if self.qos_rule_id is not None:
            result['QosRuleId'] = self.qos_rule_id

        if self.revoke_android_id is not None:
            result['RevokeAndroidId'] = self.revoke_android_id

        if self.revoke_desktop_group_id is not None:
            result['RevokeDesktopGroupId'] = self.revoke_desktop_group_id

        if self.revoke_desktop_id is not None:
            result['RevokeDesktopId'] = self.revoke_desktop_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthAndroidId') is not None:
            self.auth_android_id = m.get('AuthAndroidId')

        if m.get('AuthDesktopGroupId') is not None:
            self.auth_desktop_group_id = m.get('AuthDesktopGroupId')

        if m.get('AuthDesktopId') is not None:
            self.auth_desktop_id = m.get('AuthDesktopId')

        if m.get('QosRuleId') is not None:
            self.qos_rule_id = m.get('QosRuleId')

        if m.get('RevokeAndroidId') is not None:
            self.revoke_android_id = m.get('RevokeAndroidId')

        if m.get('RevokeDesktopGroupId') is not None:
            self.revoke_desktop_group_id = m.get('RevokeDesktopGroupId')

        if m.get('RevokeDesktopId') is not None:
            self.revoke_desktop_id = m.get('RevokeDesktopId')

        return self

