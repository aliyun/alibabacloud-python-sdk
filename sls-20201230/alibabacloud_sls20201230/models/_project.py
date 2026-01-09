# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class Project(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        data_redundancy_type: str = None,
        description: str = None,
        last_modify_time: str = None,
        owner: str = None,
        project_name: str = None,
        quota: Dict[str, Any] = None,
        recycle_bin_enabled: bool = None,
        region: str = None,
        resource_group_id: str = None,
        status: str = None,
    ):
        self.create_time = create_time
        self.data_redundancy_type = data_redundancy_type
        # This parameter is required.
        self.description = description
        self.last_modify_time = last_modify_time
        self.owner = owner
        # This parameter is required.
        self.project_name = project_name
        self.quota = quota
        self.recycle_bin_enabled = recycle_bin_enabled
        self.region = region
        self.resource_group_id = resource_group_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.data_redundancy_type is not None:
            result['dataRedundancyType'] = self.data_redundancy_type

        if self.description is not None:
            result['description'] = self.description

        if self.last_modify_time is not None:
            result['lastModifyTime'] = self.last_modify_time

        if self.owner is not None:
            result['owner'] = self.owner

        if self.project_name is not None:
            result['projectName'] = self.project_name

        if self.quota is not None:
            result['quota'] = self.quota

        if self.recycle_bin_enabled is not None:
            result['recycleBinEnabled'] = self.recycle_bin_enabled

        if self.region is not None:
            result['region'] = self.region

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('dataRedundancyType') is not None:
            self.data_redundancy_type = m.get('dataRedundancyType')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('lastModifyTime') is not None:
            self.last_modify_time = m.get('lastModifyTime')

        if m.get('owner') is not None:
            self.owner = m.get('owner')

        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')

        if m.get('quota') is not None:
            self.quota = m.get('quota')

        if m.get('recycleBinEnabled') is not None:
            self.recycle_bin_enabled = m.get('recycleBinEnabled')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

