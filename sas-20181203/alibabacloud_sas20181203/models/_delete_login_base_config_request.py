# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteLoginBaseConfigRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        target: str = None,
        type: str = None,
    ):
        # The content of the logon security settings to delete. The content varies based on the type of the logon security settings. Valid values:
        # 
        # *   **login_common_ip**: approved logon IP addresses
        # 
        # Example: {"ip":"10.23.23.23"}.
        # 
        # *   **login_common_time**: approved logon time ranges
        # 
        # Example: {"startTime":"06:00:00","endTime":"16:00:00"}.
        # 
        # *   **login_common_account**: approved logon accounts
        # 
        # Example: {"account":"test_account_001"}.
        # 
        # *   **login_common_location**: approved logon locations
        # 
        # Example: {"location":"Shanghai"}.
        # 
        # This parameter is required.
        self.config = config
        # The UUID of the server whose logon security settings you want to delete.
        # 
        # > You can call the [DescribeCloudCenterInstances](~~DescribeCloudCenterInstances~~) operation to query the UUIDs of servers.
        self.target = target
        # The type of the logon security settings to delete. Valid values:
        # 
        # *   **login_common_ip**: approved logon IP addresses
        # *   **login_common_time**: approved logon time ranges
        # *   **login_common_account**: approved logon accounts
        # *   **login_common_location**: approved logon locations
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.target is not None:
            result['Target'] = self.target

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

