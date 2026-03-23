# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBInstanceProxyConfigurationResponseBody(DaraModel):
    def __init__(
        self,
        attacks_protection_configuration: str = None,
        persistent_connections_configuration: str = None,
        request_id: str = None,
        transparent_switch_configuration: str = None,
    ):
        self.attacks_protection_configuration = attacks_protection_configuration
        self.persistent_connections_configuration = persistent_connections_configuration
        self.request_id = request_id
        self.transparent_switch_configuration = transparent_switch_configuration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attacks_protection_configuration is not None:
            result['AttacksProtectionConfiguration'] = self.attacks_protection_configuration

        if self.persistent_connections_configuration is not None:
            result['PersistentConnectionsConfiguration'] = self.persistent_connections_configuration

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.transparent_switch_configuration is not None:
            result['TransparentSwitchConfiguration'] = self.transparent_switch_configuration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttacksProtectionConfiguration') is not None:
            self.attacks_protection_configuration = m.get('AttacksProtectionConfiguration')

        if m.get('PersistentConnectionsConfiguration') is not None:
            self.persistent_connections_configuration = m.get('PersistentConnectionsConfiguration')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TransparentSwitchConfiguration') is not None:
            self.transparent_switch_configuration = m.get('TransparentSwitchConfiguration')

        return self

