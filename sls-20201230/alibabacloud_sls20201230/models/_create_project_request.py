# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateProjectRequest(DaraModel):
    def __init__(
        self,
        data_redundancy_type: str = None,
        description: str = None,
        project_name: str = None,
        recycle_bin_enabled: bool = None,
        resource_group_id: str = None,
    ):
        # The disaster recovery type. Valid values:
        # 
        # *   LRS: locally redundant storage
        # *   ZRS: zone-redundant storage
        self.data_redundancy_type = data_redundancy_type
        # The description of the project.
        # 
        # This parameter is required.
        self.description = description
        # The project name must be unique in a region. You cannot change the name after you create the project. The name must meet the following requirements:
        # 
        # *   The name must be globally unique.
        # *   The name can contain only lowercase letters, digits, and hyphens (-).
        # *   The name must start and end with a lowercase letter or a digit.
        # *   The name must be 3 to 63 characters in length.
        # 
        # This parameter is required.
        self.project_name = project_name
        # Specifies whether to enable the recycle bin feature.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.recycle_bin_enabled = recycle_bin_enabled
        # The ID of the resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_redundancy_type is not None:
            result['dataRedundancyType'] = self.data_redundancy_type

        if self.description is not None:
            result['description'] = self.description

        if self.project_name is not None:
            result['projectName'] = self.project_name

        if self.recycle_bin_enabled is not None:
            result['recycleBinEnabled'] = self.recycle_bin_enabled

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataRedundancyType') is not None:
            self.data_redundancy_type = m.get('dataRedundancyType')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')

        if m.get('recycleBinEnabled') is not None:
            self.recycle_bin_enabled = m.get('recycleBinEnabled')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        return self

