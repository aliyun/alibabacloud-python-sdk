# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyVulWhitelistTargetRequest(DaraModel):
    def __init__(
        self,
        id: int = None,
        reason: str = None,
        source_ip: str = None,
        target_info: str = None,
    ):
        # The ID of the whitelist.
        # 
        # >  You can call the [DescribeVulWhitelist](~~DescribeVulWhitelist~~) operation to query the IDs of whitelists.
        # 
        # This parameter is required.
        self.id = id
        # The reason why you add the server to the whitelist.
        self.reason = reason
        # The source IP address of the request.
        self.source_ip = source_ip
        # The applicable scope of the whitelist. The value of this parameter is in the JSON format and contains the following fields:
        # 
        # *   **type**: the type of the applicable scope. Valid values:
        # 
        #     *   **GroupId**: the ID of a server group
        #     *   **Uuid**: the UUID of a server
        # 
        # *   **uuids**: the UUIDs of servers
        # 
        # *   **groupIds**: the IDs of server groups
        # 
        # >  If you leave this parameter empty, all servers are added to the whitelist. If you set the **type** field to **GroupId**, you must also specify the **groupIds** field. If you set the **type** field to **Uuid**, you must also specify the **uuids** field.
        self.target_info = target_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.target_info is not None:
            result['TargetInfo'] = self.target_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('TargetInfo') is not None:
            self.target_info = m.get('TargetInfo')

        return self

