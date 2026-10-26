# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDatabasesProjectRequest(DaraModel):
    def __init__(
        self,
        database_ids: str = None,
        instance_id: str = None,
        project_id: int = None,
        region_id: str = None,
        target_project_id: int = None,
    ):
        # The IDs of the database instances that you want to move. The value is a JSON string. You can specify up to 100 database instance IDs. Separate multiple IDs with commas (,).
        # 
        # > You can call the [ListDatabases](https://help.aliyun.com/document_detail/2758822.html) operation to query the database instance IDs.
        # 
        # This parameter is required.
        self.database_ids = database_ids
        # The ID of the Bastionhost instance.
        # > You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to query the instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the project to which the database instances currently belong.
        self.project_id = project_id
        # The region ID of the Bastionhost instance.
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id
        # The ID of the destination project to which you want to move the database instances.
        # > You can call the ListProjectsForProjectAuthorizationPrincipal operation to query the project ID.
        # 
        # This parameter is required.
        self.target_project_id = target_project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_ids is not None:
            result['DatabaseIds'] = self.database_ids

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.target_project_id is not None:
            result['TargetProjectId'] = self.target_project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseIds') is not None:
            self.database_ids = m.get('DatabaseIds')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TargetProjectId') is not None:
            self.target_project_id = m.get('TargetProjectId')

        return self

