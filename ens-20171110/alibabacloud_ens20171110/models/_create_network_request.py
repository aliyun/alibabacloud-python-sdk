# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class CreateNetworkRequest(DaraModel):
    def __init__(
        self,
        cidr_block: str = None,
        description: str = None,
        enable_ipv_6: bool = None,
        ens_region_id: str = None,
        ipv_6isp: str = None,
        network_name: str = None,
        tag: List[main_models.CreateNetworkRequestTag] = None,
    ):
        # The CIDR block of the network. You can use one of the following CIDR blocks or their subsets:
        # 
        # - 10.0.0.0/8 (default).
        # 
        # - 172.16.0.0/12.
        # 
        # - 192.168.0.0/16.
        # 
        # This parameter is required.
        self.cidr_block = cidr_block
        # A description of the network.
        # 
        # Must be 2 to 256 characters long, start with a letter or a Chinese character, and cannot start with http\\:// or https\\://.
        self.description = description
        self.enable_ipv_6 = enable_ipv_6
        # The node ID of ENS.
        # 
        # This parameter is required.
        self.ens_region_id = ens_region_id
        self.ipv_6isp = ipv_6isp
        # The network name. Follow these naming rules:
        # 
        # - Must be 2 to 128 characters long, using English or Chinese characters.
        # 
        # - Must start with a letter or a Chinese character. Cannot start with http\\:// or https\\://.
        # 
        # - Can contain digits, colons (:), underscores (_), or hyphens (-).
        self.network_name = network_name
        # Resource tags.
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.description is not None:
            result['Description'] = self.description

        if self.enable_ipv_6 is not None:
            result['EnableIpv6'] = self.enable_ipv_6

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.ipv_6isp is not None:
            result['Ipv6Isp'] = self.ipv_6isp

        if self.network_name is not None:
            result['NetworkName'] = self.network_name

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnableIpv6') is not None:
            self.enable_ipv_6 = m.get('EnableIpv6')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('Ipv6Isp') is not None:
            self.ipv_6isp = m.get('Ipv6Isp')

        if m.get('NetworkName') is not None:
            self.network_name = m.get('NetworkName')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateNetworkRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreateNetworkRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key for the instance. N ranges from **1** to **20**.
        # 
        # - Cannot start with `aliyun`, `acs:`, `http://`, or `https://`.
        # 
        # - Supports up to 64 characters.
        # 
        # - Cannot be an empty string.
        self.key = key
        # The tag value for the resource. N ranges from 1 to 20. This value can be an empty string once provided. It supports up to 128 characters, cannot start with acs:, and cannot contain http\\:// or https\\://.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

