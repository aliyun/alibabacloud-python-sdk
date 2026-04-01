# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AttachRCInstancesShrinkRequest(DaraModel):
    def __init__(
        self,
        instance_ids_shrink: str = None,
        key_pair: str = None,
        password: str = None,
        region_id: str = None,
        vpc_id: str = None,
    ):
        # The node IDs.
        # 
        # This parameter is required.
        self.instance_ids_shrink = instance_ids_shrink
        # The key pair of the node.
        self.key_pair = key_pair
        # The logon password of the node.
        self.password = password
        # The region ID.
        self.region_id = region_id
        # The virtual private cloud (VPC) ID.
        # 
        # > This is a reserved parameter.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_ids_shrink is not None:
            result['InstanceIds'] = self.instance_ids_shrink

        if self.key_pair is not None:
            result['KeyPair'] = self.key_pair

        if self.password is not None:
            result['Password'] = self.password

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids_shrink = m.get('InstanceIds')

        if m.get('KeyPair') is not None:
            self.key_pair = m.get('KeyPair')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

