# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ConfigInstanceSecurityGroupsRequest(DaraModel):
    def __init__(
        self,
        authorized_security_groups: List[str] = None,
        instance_id: str = None,
        lang: str = None,
        region_id: str = None,
    ):
        # An array that consists of the IDs of authorized security groups.
        # 
        # This parameter is required.
        self.authorized_security_groups = authorized_security_groups
        # The ID of the bastion host.
        # 
        # > You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to query the ID of the bastion host.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The region ID of the bastion host.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorized_security_groups is not None:
            result['AuthorizedSecurityGroups'] = self.authorized_security_groups

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizedSecurityGroups') is not None:
            self.authorized_security_groups = m.get('AuthorizedSecurityGroups')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

