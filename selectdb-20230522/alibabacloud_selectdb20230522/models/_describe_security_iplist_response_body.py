# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_selectdb20230522 import models as main_models
from darabonba.model import DaraModel

class DescribeSecurityIPListResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        group_items: List[main_models.DescribeSecurityIPListResponseBodyGroupItems] = None,
        request_id: str = None,
    ):
        # The instance ID.
        self.dbinstance_name = dbinstance_name
        # The details about each IP address whitelist returned.
        self.group_items = group_items
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.group_items:
            for v1 in self.group_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        result['GroupItems'] = []
        if self.group_items is not None:
            for k1 in self.group_items:
                result['GroupItems'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        self.group_items = []
        if m.get('GroupItems') is not None:
            for k1 in m.get('GroupItems'):
                temp_model = main_models.DescribeSecurityIPListResponseBodyGroupItems()
                self.group_items.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeSecurityIPListResponseBodyGroupItems(DaraModel):
    def __init__(
        self,
        aecurity_iptype: str = None,
        group_name: str = None,
        group_tag: str = None,
        security_iplist: str = None,
        whitelist_net_type: str = None,
    ):
        # The IP address type. Valid values:
        # 
        # *   ipv4
        # *   ipv6 (not supported)
        self.aecurity_iptype = aecurity_iptype
        # The name of the whitelist.
        self.group_name = group_name
        # The tag of the whitelist.
        self.group_tag = group_tag
        # The IP addresses in the whitelist. Multiple IP addresses are separated by commas (,).
        self.security_iplist = security_iplist
        # The network type of the whitelist.
        self.whitelist_net_type = whitelist_net_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aecurity_iptype is not None:
            result['AecurityIPType'] = self.aecurity_iptype

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.group_tag is not None:
            result['GroupTag'] = self.group_tag

        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist

        if self.whitelist_net_type is not None:
            result['WhitelistNetType'] = self.whitelist_net_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AecurityIPType') is not None:
            self.aecurity_iptype = m.get('AecurityIPType')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('GroupTag') is not None:
            self.group_tag = m.get('GroupTag')

        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')

        if m.get('WhitelistNetType') is not None:
            self.whitelist_net_type = m.get('WhitelistNetType')

        return self

