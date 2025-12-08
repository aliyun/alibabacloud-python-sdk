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
        self.client_token = client_token
        self.group_name = group_name
        self.instance_name = instance_name
        self.ip_whitelist = ip_whitelist
        self.modify_mode = modify_mode
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

