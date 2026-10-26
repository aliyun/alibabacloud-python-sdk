# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AttachMembersToProjectRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        member_ids: str = None,
        project_id: int = None,
        region_id: str = None,
    ):
        # The Bastionhost instance ID.
        # 
        # > You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The UIDs of the member accounts to associate with the project.
        # > You can call the ListMembersNotForProject operation to obtain this parameter.
        # 
        # This parameter is required.
        self.member_ids = member_ids
        # The ID of the project to which you want to associate member accounts.
        # > You can call the ListProjects operation to obtain this parameter.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The region ID of the Bastionhost instance.
        # 
        # > For the mappings between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
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

        if self.member_ids is not None:
            result['MemberIds'] = self.member_ids

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MemberIds') is not None:
            self.member_ids = m.get('MemberIds')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

