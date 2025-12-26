# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class ResourceGroup(DaraModel):
    def __init__(
        self,
        creator_id: str = None,
        gmt_created_time: str = None,
        gmt_modified_time: str = None,
        name: str = None,
        node_count: int = None,
        resource_group_id: str = None,
        user_vpc: main_models.UserVpc = None,
        version: str = None,
        workspace_id: str = None,
    ):
        self.creator_id = creator_id
        self.gmt_created_time = gmt_created_time
        self.gmt_modified_time = gmt_modified_time
        self.name = name
        self.node_count = node_count
        self.resource_group_id = resource_group_id
        self.user_vpc = user_vpc
        self.version = version
        self.workspace_id = workspace_id

    def validate(self):
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator_id is not None:
            result['CreatorID'] = self.creator_id

        if self.gmt_created_time is not None:
            result['GmtCreatedTime'] = self.gmt_created_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.name is not None:
            result['Name'] = self.name

        if self.node_count is not None:
            result['NodeCount'] = self.node_count

        if self.resource_group_id is not None:
            result['ResourceGroupID'] = self.resource_group_id

        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()

        if self.version is not None:
            result['Version'] = self.version

        if self.workspace_id is not None:
            result['WorkspaceID'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatorID') is not None:
            self.creator_id = m.get('CreatorID')

        if m.get('GmtCreatedTime') is not None:
            self.gmt_created_time = m.get('GmtCreatedTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')

        if m.get('ResourceGroupID') is not None:
            self.resource_group_id = m.get('ResourceGroupID')

        if m.get('UserVpc') is not None:
            temp_model = main_models.UserVpc()
            self.user_vpc = temp_model.from_map(m.get('UserVpc'))

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('WorkspaceID') is not None:
            self.workspace_id = m.get('WorkspaceID')

        return self

