# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class UpdateWhiteIpsRequest(DaraModel):
    def __init__(
        self,
        es_ipwhitelist: List[str] = None,
        white_ip_group: main_models.UpdateWhiteIpsRequestWhiteIpGroup = None,
        client_token: str = None,
        modify_mode: str = None,
    ):
        # The IP address information in the whitelist.
        self.es_ipwhitelist = es_ipwhitelist
        # Updates the whitelist configuration of the instance by using a whitelist group. You can update only one whitelist group.
        # >Notice:  You cannot configure esIPWhitelist and whiteIpGroup at the same time.
        self.white_ip_group = white_ip_group
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain a maximum of 64 ASCII characters.
        self.client_token = client_token
        # The modification method. Valid values:
        # 
        # - Cover (default): Overwrites the IP addresses in the original whitelist with the value of the ips parameter.
        # 
        # - Append: Adds the IP addresses specified by the ips parameter to the original whitelist.
        # 
        # - Delete: Removes the IP addresses specified by the ips parameter from the original whitelist. You must retain at least one IP address.
        self.modify_mode = modify_mode

    def validate(self):
        if self.white_ip_group:
            self.white_ip_group.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.es_ipwhitelist is not None:
            result['esIPWhitelist'] = self.es_ipwhitelist

        if self.white_ip_group is not None:
            result['whiteIpGroup'] = self.white_ip_group.to_map()

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.modify_mode is not None:
            result['modifyMode'] = self.modify_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('esIPWhitelist') is not None:
            self.es_ipwhitelist = m.get('esIPWhitelist')

        if m.get('whiteIpGroup') is not None:
            temp_model = main_models.UpdateWhiteIpsRequestWhiteIpGroup()
            self.white_ip_group = temp_model.from_map(m.get('whiteIpGroup'))

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('modifyMode') is not None:
            self.modify_mode = m.get('modifyMode')

        return self

class UpdateWhiteIpsRequestWhiteIpGroup(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        ips: List[str] = None,
        white_ip_type: str = None,
    ):
        # The name of the whitelist group. This parameter is required if the whiteIpGroup parameter is specified.
        self.group_name = group_name
        # The list of IP addresses in the whitelist group.
        self.ips = ips
        # The type of the IP address whitelist. Set the value to **PRIVATE_ES**, which indicates a private network access whitelist.
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

