# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class UpdateKibanaWhiteIpsRequest(DaraModel):
    def __init__(
        self,
        kibana_ipwhitelist: List[str] = None,
        white_ip_group: main_models.UpdateKibanaWhiteIpsRequestWhiteIpGroup = None,
        client_token: str = None,
        modify_mode: str = None,
    ):
        # The IP address whitelists. This parameter is available if the whiteIpGroup parameter is left empty. The default IP address whitelist is updated based on the value of this parameter.
        # 
        # You cannot configure both the kibanaIPWhitelist and whiteIpGroup parameters.
        self.kibana_ipwhitelist = kibana_ipwhitelist
        # The name of the whitelist. This parameter is required if you configure the whiteIpGroup parameter.
        self.white_ip_group = white_ip_group
        # The update mode. Valid values:
        # 
        # *   Cover: overwrites the IP addresses in the specified IP address whitelist with the IP addresses specified by using the ips parameter. This is the default value.
        # *   Append: adds the IP addresses specified by using the ips parameter to the specified IP address whitelist.
        # *   Delete: deletes the IP addresses specified by using the ips parameter from the specified IP address whitelist. At least one IP address must be retained for the whitelist.
        self.client_token = client_token
        # The body of the request.
        self.modify_mode = modify_mode

    def validate(self):
        if self.white_ip_group:
            self.white_ip_group.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.kibana_ipwhitelist is not None:
            result['kibanaIPWhitelist'] = self.kibana_ipwhitelist

        if self.white_ip_group is not None:
            result['whiteIpGroup'] = self.white_ip_group.to_map()

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.modify_mode is not None:
            result['modifyMode'] = self.modify_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('kibanaIPWhitelist') is not None:
            self.kibana_ipwhitelist = m.get('kibanaIPWhitelist')

        if m.get('whiteIpGroup') is not None:
            temp_model = main_models.UpdateKibanaWhiteIpsRequestWhiteIpGroup()
            self.white_ip_group = temp_model.from_map(m.get('whiteIpGroup'))

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('modifyMode') is not None:
            self.modify_mode = m.get('modifyMode')

        return self

class UpdateKibanaWhiteIpsRequestWhiteIpGroup(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        ips: List[str] = None,
        white_ip_type: str = None,
    ):
        # The type of the whitelist. Set the value to PUBLIC_KIBANA. This value indicates a public IP address whitelist.
        self.group_name = group_name
        # The IP addresses in the whitelist. This parameter is required if you configure the whiteIpGroup parameter.
        self.ips = ips
        # The IP addresses in the whitelist.
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

