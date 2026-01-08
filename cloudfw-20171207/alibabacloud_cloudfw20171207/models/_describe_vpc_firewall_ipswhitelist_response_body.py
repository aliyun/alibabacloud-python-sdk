# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeVpcFirewallIPSWhitelistResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        whitelists: List[main_models.DescribeVpcFirewallIPSWhitelistResponseBodyWhitelists] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The details of the IPS whitelist of the VPC firewall.
        self.whitelists = whitelists

    def validate(self):
        if self.whitelists:
            for v1 in self.whitelists:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Whitelists'] = []
        if self.whitelists is not None:
            for k1 in self.whitelists:
                result['Whitelists'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.whitelists = []
        if m.get('Whitelists') is not None:
            for k1 in m.get('Whitelists'):
                temp_model = main_models.DescribeVpcFirewallIPSWhitelistResponseBodyWhitelists()
                self.whitelists.append(temp_model.from_map(k1))

        return self

class DescribeVpcFirewallIPSWhitelistResponseBodyWhitelists(DaraModel):
    def __init__(
        self,
        list_type: int = None,
        list_value: str = None,
        vpc_firewall_id: str = None,
        white_list_value: List[str] = None,
        white_type: int = None,
    ):
        # The type of the list. Valid values:
        # 
        # *   **1**: user-defined
        # *   **2**: address book
        self.list_type = list_type
        # The entries in the list.
        self.list_value = list_value
        # The instance ID of the VPC firewall.
        self.vpc_firewall_id = vpc_firewall_id
        # An array of entries in the list.
        self.white_list_value = white_list_value
        # The type of the whitelist. Valid values:
        # 
        # *   **1**: destination
        # *   **2**: source
        self.white_type = white_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.list_type is not None:
            result['ListType'] = self.list_type

        if self.list_value is not None:
            result['ListValue'] = self.list_value

        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id

        if self.white_list_value is not None:
            result['WhiteListValue'] = self.white_list_value

        if self.white_type is not None:
            result['WhiteType'] = self.white_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListType') is not None:
            self.list_type = m.get('ListType')

        if m.get('ListValue') is not None:
            self.list_value = m.get('ListValue')

        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')

        if m.get('WhiteListValue') is not None:
            self.white_list_value = m.get('WhiteListValue')

        if m.get('WhiteType') is not None:
            self.white_type = m.get('WhiteType')

        return self

