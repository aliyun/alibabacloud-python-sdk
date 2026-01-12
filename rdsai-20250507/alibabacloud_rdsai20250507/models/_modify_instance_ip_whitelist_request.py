# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyInstanceIpWhitelistRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        group_name: str = None,
        instance_name: str = None,
        ip_whitelist: str = None,
        modify_mode: str = None,
        region_id: str = None,
    ):
        # The method that is used to modify the IP address whitelist. Valid values:
        # 
        # *   **Cover** (default): Uses the IP addresses and CIDR blocks that are specified in the **IpWhitelist** parameter to **overwrite** the existing ones in the current whitelist.
        # *   **Append**: **Appends** the IP addresses and CIDR blocks that are specified in the **IpWhitelist** parameter to the current whitelist.
        # *   **Delete**: **Deletes** the IP addresses and CIDR blocks that are specified in the **IpWhitelist** parameter from the current whitelist. You must retain at least one IP address or CIDR block.
        self.client_token = client_token
        # The idempotency token. The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        self.group_name = group_name
        # The region ID.
        self.instance_name = instance_name
        # The ID of the RDS Supabase instance.
        self.ip_whitelist = ip_whitelist
        # The IP address whitelist. Before you modify the IP address whitelist, call the DescribeInstanceIpWhitelist operation to query the existing IP address whitelist of the instance.
        # 
        # **Configuration rules**
        # 
        # *   You can configure IP addresses (such as 10.23.XXX.XXX) or CIDR blocks (such as 10.23.XXX.XXX/24).
        # *   Separate multiple IP addresses or CIDR blocks with commas (,) and do not add spaces preceding or following the commas.
        # *   You can configure up to 1,000 IP addresses and CIDR blocks in total for each instance. If you want to add a large number of IP addresses, we recommend that you merge the IP addresses into CIDR blocks, such as 10.23.XXX.XXX/24.
        self.modify_mode = modify_mode
        # The operation that you want to perform. Set the value to **ModifyInstanceIpWhitelist**.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.ip_whitelist is not None:
            result['IpWhitelist'] = self.ip_whitelist

        if self.modify_mode is not None:
            result['ModifyMode'] = self.modify_mode

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('IpWhitelist') is not None:
            self.ip_whitelist = m.get('IpWhitelist')

        if m.get('ModifyMode') is not None:
            self.modify_mode = m.get('ModifyMode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

