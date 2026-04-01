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
        # Indicates whether the mechanism that is used to mitigate brute-force attacks is enabled:
        # 
        # *   **Enable**
        # *   **Disable**
        # 
        # The return value is a JSON string. Example:
        # 
        #     {"status":"Disable", "check_interval_seconds": 60,
        #               "max_failed_login_attempts": 60, "blocking_seconds": 600}
        # 
        # Description:
        # 
        # *   Each client allows {max_failed_login_attempts} logon attempts that fail due to incorrect passwords within {check_interval_seconds} seconds. If one more such attempt is conducted, the client must wait for {blocking_seconds} seconds before you can try again.
        # 
        # *   Valid values:
        # 
        #     *   check_interval_seconds: **30 to 600**. Unit: seconds.
        #     *   max_failed_login_attempts: **10 to 5000**. Unit: times.
        #     *   blocking_seconds: **30 to 3600**. Unit: seconds.
        self.attacks_protection_configuration = attacks_protection_configuration
        # Indicates whether the short-lived connection optimization feature is enabled.
        # 
        # *   **Enable**
        # *   **Disable**
        # 
        # In this case, the return value is a JSON string. Examples:
        # 
        #     {"status":"Disable"}.
        self.persistent_connections_configuration = persistent_connections_configuration
        # The request ID.
        self.request_id = request_id
        # Indicates whether the transparent switchover feature is enabled.
        # 
        # *   **Enable**
        # *   **Disable**
        # 
        # The return value is a JSON string. Example:
        # 
        #     {"status":"Enable"}
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

