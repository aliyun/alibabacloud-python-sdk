# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeInstanceIdsRequest(DaraModel):
    def __init__(
        self,
        edition: int = None,
        instance_ids: List[str] = None,
        resource_group_id: str = None,
    ):
        # The edition of the Anti-DDoS Pro or Anti-DDoS Premium instance to query. Valid values:
        # 
        # - **0**: Anti-DDoS Pro or Anti-DDoS Premium (outside the Chinese mainland) Insurance Edition.
        # - **1**: Anti-DDoS Pro or Anti-DDoS Premium (outside the Chinese mainland) Unlimited Edition.
        # - **2**: Anti-DDoS Pro or Anti-DDoS Premium (outside the Chinese mainland) Acceleration Line.
        # - **3**: Anti-DDoS Pro or Anti-DDoS Premium (outside the Chinese mainland) Secure Acceleration Line.
        # - **9**: Anti-DDoS Pro or Anti-DDoS Premium (the Chinese mainland) Professional Edition.
        self.edition = edition
        # The IDs of the Anti-DDoS Pro or Anti-DDoS Premium instances to query. Maximum value of N: 200.
        self.instance_ids = instance_ids
        # The ID of the resource group to which the Anti-DDoS Pro or Anti-DDoS Premium instance belongs in Resource Management.
        # 
        # If you do not specify this parameter, the default resource group is used.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.edition is not None:
            result['Edition'] = self.edition

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

