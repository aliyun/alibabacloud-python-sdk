# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyProjectRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        instance_id: str = None,
        member_ids: str = None,
        name: str = None,
        project_id: int = None,
        region_id: str = None,
    ):
        # The new description of the project. The description can be up to 500 characters in length.
        self.description = description
        # The instance ID of the bastion host for which you want to modify project information.
        # > You can invoke the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The UIDs of the member accounts to associate with the project after modification.
        # > You can call the ListMembersNotForProject operation to obtain this parameter. If you do not specify this parameter, no changes are made.
        self.member_ids = member_ids
        # The new name of the project. The name must be 1 to 128 characters in length, cannot start with a special character, and can contain only the following special characters: periods (.), underscores (_), hyphens (-), backslashes (\\), and spaces.
        self.name = name
        # The ID of the project that you want to modify.
        # > You can call the ListProjects operation to obtain this parameter.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The region ID of the bastion host.
        # > For the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.member_ids is not None:
            result['MemberIds'] = self.member_ids

        if self.name is not None:
            result['Name'] = self.name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MemberIds') is not None:
            self.member_ids = m.get('MemberIds')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

