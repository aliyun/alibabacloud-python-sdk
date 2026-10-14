# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class CreateVSwitchRequest(DaraModel):
    def __init__(
        self,
        cidr_block: str = None,
        description: str = None,
        ens_region_id: str = None,
        ipv_6cidr_block: str = None,
        network_id: str = None,
        tag: List[main_models.CreateVSwitchRequestTag] = None,
        v_switch_name: str = None,
    ):
        # The CIDR block of the VSwitch. The following requirements apply:
        # 
        # - The prefix length must be an integer from 16 to 29.
        # 
        # - The CIDR block of the VSwitch must be a subset of the CIDR block of the VPC to which the VSwitch belongs.
        # 
        # - The CIDR block of the VSwitch cannot be the same as the destination CIDR block of an existing route in the VPC, but it can be a subset of the destination CIDR block.
        # 
        # This parameter is required.
        self.cidr_block = cidr_block
        # The description of the VSwitch.
        # 
        # The description must be 2 to 256 characters in length. It must start with a letter or a Chinese character, and cannot start with `http://` or `https://`.
        self.description = description
        # The ID of the ENS node.
        # 
        # This parameter is required.
        self.ens_region_id = ens_region_id
        self.ipv_6cidr_block = ipv_6cidr_block
        # The ID of the network to which the VSwitch belongs.
        self.network_id = network_id
        # The tags of the resource. You can specify up to 20 tags.
        self.tag = tag
        # The name of the VSwitch. The following requirements apply:
        # 
        # - The name must be 2 to 128 characters in length.
        # 
        # - The name must start with a letter or a Chinese character, and cannot start with `http://` or `https://`. The name can contain digits, colons (:), underscores (_), and hyphens (-).
        # 
        # Default value: an empty string.
        self.v_switch_name = v_switch_name

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

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.ipv_6cidr_block is not None:
            result['Ipv6CidrBlock'] = self.ipv_6cidr_block

        if self.network_id is not None:
            result['NetworkId'] = self.network_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('Ipv6CidrBlock') is not None:
            self.ipv_6cidr_block = m.get('Ipv6CidrBlock')

        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateVSwitchRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')

        return self

class CreateVSwitchRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        # 
        # - The tag key cannot start with `aliyun`, `acs:`, `http://`, or `https://`.
        # 
        # - The tag key can be up to 64 characters long.
        # 
        # - The tag key cannot be an empty string.
        self.key = key
        # The value of the tag. It can be up to 128 characters long, can be an empty string, and cannot start with `acs:` or contain `http://` or `https://`.
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

