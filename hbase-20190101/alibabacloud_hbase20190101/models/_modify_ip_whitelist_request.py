# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyIpWhitelistRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        group_name: str = None,
        ip_list: str = None,
        ip_version: str = None,
    ):
        # The ID of target instance. You can call [DescribeInstances](https://help.aliyun.com/document_detail/144595.html) to obtain target instance ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The name of the whitelist group for the target instance. You can invoke [DescribeIpWhitelist](https://help.aliyun.com/document_detail/144606.html) to obtain the whitelist group name.
        # 
        # This parameter is required.
        self.group_name = group_name
        # The IP addresses in the whitelist group after modification. Separate multiple IP addresses with commas (,).
        self.ip_list = ip_list
        # The version of the IP address. Valid values:
        # 
        # - **4**: IPv4.
        # - **6**: IPv6.
        # 
        # This parameter is required.
        self.ip_version = ip_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.ip_list is not None:
            result['IpList'] = self.ip_list

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        return self

