# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyLoginBaseConfigRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        target: str = None,
        type: str = None,
    ):
        # The details of the configuration that is used to detect unusual logons to your servers. The value of this parameter is in the JSON format and contains the following fields:
        # 
        # *   **totalCount**: the total number of servers.
        # *   **uuidCount**: the number of servers to which the configuration is applied.
        # *   **id**: the ID of the configuration.
        # *   **location**: the common logon location.
        # 
        # > You must specify this field if the Type parameter is set to login_common_location.
        # 
        # *   **ip**: the common logon IP address.
        # 
        # > You must specify this field if the Type parameter is set to login_common_ip.
        # 
        # *   **endTime**: the end time of the common logon time range.
        # 
        # > You must specify this field if the Type parameter is set to login_common_time.
        # 
        # *   **startTime**: the start time of the common logon time range.
        # 
        # > You must specify this field if the Type parameter is set to login_common_time.
        # 
        # *   **account**: the common logon account.
        # 
        # > You must specify this field if the Type parameter is set to login_common_account.
        # 
        # This parameter is required.
        self.config = config
        # The details of the server to which the configuration is applied. The value of this parameter is in the JSON format and contains the following fields:
        # 
        # *   **Target**: the UUID of the server.
        # 
        # *   **targetType**: the type of the server to which the configuration is applied. Valid values:
        # 
        #     *   **uuid**: a server
        #     *   **groupId**: a server group
        # 
        # *   **flag**: the operation that you want to perform on the server. Valid values:
        # 
        #     *   **del**: removes the server from the configuration.
        #     *   **add**: adds the server to the configuration.
        # 
        # This parameter is required.
        self.target = target
        # The logon type of the configuration to modify. Valid values:
        # 
        # *   **login_common_location**: common logon location
        # *   **login_common_ip**: common logon IP address
        # *   **login_common_time**: common logon time range
        # *   **login_common_account**: common logon account
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

