# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ConfigInstanceNetworkRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        private_white_list: List[str] = None,
        public_access_control: int = None,
        public_white_list: List[str] = None,
        region_id: str = None,
        security_group_ids: List[str] = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.private_white_list = private_white_list
        # This parameter is required.
        self.public_access_control = public_access_control
        self.public_white_list = public_white_list
        self.region_id = region_id
        # This parameter is required.
        self.security_group_ids = security_group_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.private_white_list is not None:
            result['PrivateWhiteList'] = self.private_white_list

        if self.public_access_control is not None:
            result['PublicAccessControl'] = self.public_access_control

        if self.public_white_list is not None:
            result['PublicWhiteList'] = self.public_white_list

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PrivateWhiteList') is not None:
            self.private_white_list = m.get('PrivateWhiteList')

        if m.get('PublicAccessControl') is not None:
            self.public_access_control = m.get('PublicAccessControl')

        if m.get('PublicWhiteList') is not None:
            self.public_white_list = m.get('PublicWhiteList')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')

        return self

