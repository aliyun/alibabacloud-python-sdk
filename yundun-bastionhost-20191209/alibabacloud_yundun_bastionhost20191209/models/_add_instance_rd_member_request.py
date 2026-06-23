# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddInstanceRdMemberRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        member_id: str = None,
        region_id: str = None,
    ):
        # The ID of the Bastionhost instance.
        # 
        # > Call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to obtain the instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The UID of the RD member account to add.
        # 
        # This parameter is required.
        self.member_id = member_id
        # The region ID of the Bastionhost instance.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.member_id is not None:
            result['MemberId'] = self.member_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

