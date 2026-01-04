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
        ens_region_id: str = None,
        network_name: str = None,
        tag: List[main_models.CreateNetworkRequestTag] = None,
    ):
        # The CIDR block of the network. You can use one of the following CIDR blocks or their subnets as the CIDR block of the network:
        # 
        # *   10.0.0.0/8 (default)
        # *   172.16.0.0/12
        # *   192.168.0.0/16
        # 
        # This parameter is required.
        self.cidr_block = cidr_block
        # The description of the network.
        # 
        # The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https://.
        self.description = description
        # The ID of the edge node.
        # 
        # This parameter is required.
        self.ens_region_id = ens_region_id
        # The name of the network. The name must meet the following requirements:
        # 
        # *   The name must be 2 to 128 characters in length.
        # *   The name must start with a letter but cannot start with http:// or https://.
        # *   The name can contain letters, digits, colons (:), underscores (_), and hyphens (-).
        self.network_name = network_name
        # The resource tags.
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

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

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

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

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
        # The key of the tag that are to add to the instance. Valid values of N: **1** to **20**.
        # 
        # *   The key cannot start with `aliyun`, `acs:`, `http://`, or `https://`.
        # *   The key must be up to 64 characters in length.
        # *   The tag key cannot be an empty string.
        self.key = key
        # The value of tag N that is added to the resource. You can specify up to 20 tag values. The tag value can be an empty string. The tag value can be up to 128 characters in length. It cannot start with acs: or contain http:// or https://.
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

