# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetComputeResourceAuthUserMappingsRequest(DaraModel):
    def __init__(
        self,
        compute_resource_id: int = None,
        project_id: int = None,
    ):
        # The ID of the compute resource.
        # 
        # This parameter is required.
        self.compute_resource_id = compute_resource_id
        # The DataWorks workspace to which the data source belongs.
        # 
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compute_resource_id is not None:
            result['ComputeResourceId'] = self.compute_resource_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputeResourceId') is not None:
            self.compute_resource_id = m.get('ComputeResourceId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

