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
        # The detailed configuration of the unusual logon detection rule for the server. This parameter is in JSON format and contains the following fields:
        # 
        # - **totalCount**: the total number of assets.
        # - **uuidCount**: the number of assets on which the rule takes effect.
        # - **id**: the ID of the unusual logon detection rule.
        # - **location**: the name of the common logon location.
        # 
        # > This field is required only when the Type parameter is set to login_common_location.
        # 
        # - **ip**: the common logon IP address.
        # 
        # > This field is required only when the Type parameter is set to login_common_ip.
        # 
        # - **endTime**: the end time of the common logon time range.
        # 
        # > This field is required only when the Type parameter is set to login_common_time.
        # 
        # - **startTime**: the start time of the common logon time range.
        # 
        # > This field is required only when the Type parameter is set to login_common_time.
        # 
        # - **account**: the common logon account.
        # 
        # > This field is required only when the Type parameter is set to login_common_account.
        # 
        # This parameter is required.
        self.config = config
        # The configuration of the servers on which the unusual logon detection rule takes effect. This parameter is in JSON format and contains the following fields:
        # 
        # - **Target**: the UUID of the server to add or remove.
        # - **targetType**: the mode for adding assets on which the rule takes effect. Valid values:
        #     - **uuid**: add by individual server.
        #     - **groupId**: add by server group.
        # - **flag**: the operation to perform on the asset. Valid values:
        #     - **del**: remove the server from the rule.
        #     - **add**: add the server to the rule.
        # 
        # This parameter is required.
        self.target = target
        # The type of unusual logon detection for the server. Valid values:
        # 
        # - **login_common_location**: common logon location.
        # - **login_common_ip**: common logon IP address.
        # - **login_common_time**: common logon time.
        # - **login_common_account**: common logon account.
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

