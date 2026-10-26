# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DetachProjectsFromProjectAuthorizationRequest(DaraModel):
    def __init__(
        self,
        authorization_id: int = None,
        instance_id: str = None,
        project_ids: str = None,
        region_id: str = None,
    ):
        # The project authorization ID.
        # > You can call the ListProjectAuthorizations operation to query this parameter.
        # 
        # This parameter is required.
        self.authorization_id = authorization_id
        # The ID of the bastion host instance.
        # > You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to query this parameter.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The array of project IDs to remove from the project authorization.
        # > You can call the GetProjectAuthorization operation to query this parameter.
        # 
        # This parameter is required.
        self.project_ids = project_ids
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
        if self.authorization_id is not None:
            result['AuthorizationId'] = self.authorization_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.project_ids is not None:
            result['ProjectIds'] = self.project_ids

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationId') is not None:
            self.authorization_id = m.get('AuthorizationId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ProjectIds') is not None:
            self.project_ids = m.get('ProjectIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

