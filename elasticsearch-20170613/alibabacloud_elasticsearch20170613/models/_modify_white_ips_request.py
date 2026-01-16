# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class ModifyWhiteIpsRequest(DaraModel):
    def __init__(
        self,
        modify_mode: str = None,
        network_type: str = None,
        node_type: str = None,
        white_ip_group: main_models.ModifyWhiteIpsRequestWhiteIpGroup = None,
        white_ip_list: List[str] = None,
        client_token: str = None,
    ):
        # The information about the IP address whitelist that you want to update. You can specify only one whitelist.
        # 
        # > You cannot configure both the whiteIpList and whiteIpGroup parameters.
        self.modify_mode = modify_mode
        # The IP addresses in the whitelist. This parameter is available if the whiteIpGroup parameter is left empty. The default IP address whitelist is updated based on the value of this parameter.
        # 
        # > You cannot configure both the whiteIpList and whiteIpGroup parameters.
        self.network_type = network_type
        # The IP addresses in the whitelist. This parameter is available if the whiteIpGroup parameter is left empty. The default IP address whitelist is updated based on the value of this parameter.
        self.node_type = node_type
        # The IP addresses in the whitelist. This parameter is required if you configure the whiteIpGroup parameter.
        self.white_ip_group = white_ip_group
        # The name of the whitelist. This parameter is required if you configure the whiteIpGroup parameter.
        self.white_ip_list = white_ip_list
        # The network type. This parameter is required if you configure the whiteIpList parameter. Valid values:
        # 
        # *   PRIVATE
        # *   PUBLIC
        self.client_token = client_token

    def validate(self):
        if self.white_ip_group:
            self.white_ip_group.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.modify_mode is not None:
            result['modifyMode'] = self.modify_mode

        if self.network_type is not None:
            result['networkType'] = self.network_type

        if self.node_type is not None:
            result['nodeType'] = self.node_type

        if self.white_ip_group is not None:
            result['whiteIpGroup'] = self.white_ip_group.to_map()

        if self.white_ip_list is not None:
            result['whiteIpList'] = self.white_ip_list

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modifyMode') is not None:
            self.modify_mode = m.get('modifyMode')

        if m.get('networkType') is not None:
            self.network_type = m.get('networkType')

        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')

        if m.get('whiteIpGroup') is not None:
            temp_model = main_models.ModifyWhiteIpsRequestWhiteIpGroup()
            self.white_ip_group = temp_model.from_map(m.get('whiteIpGroup'))

        if m.get('whiteIpList') is not None:
            self.white_ip_list = m.get('whiteIpList')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

class ModifyWhiteIpsRequestWhiteIpGroup(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        ips: List[str] = None,
        white_ip_type: str = None,
    ):
        # The type of the IP address whitelist. Valid values:
        # 
        # *   PRIVATE_KIBANA
        # *   PRIVATE_ES
        # *   PUBLIC_ES
        # *   PUBLIC_KIBANA
        self.group_name = group_name
        # The returned result.
        self.ips = ips
        # The request ID.
        self.white_ip_type = white_ip_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_name is not None:
            result['groupName'] = self.group_name

        if self.ips is not None:
            result['ips'] = self.ips

        if self.white_ip_type is not None:
            result['whiteIpType'] = self.white_ip_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')

        if m.get('ips') is not None:
            self.ips = m.get('ips')

        if m.get('whiteIpType') is not None:
            self.white_ip_type = m.get('whiteIpType')

        return self

