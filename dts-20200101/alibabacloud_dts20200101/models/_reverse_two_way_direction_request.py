# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReverseTwoWayDirectionRequest(DaraModel):
    def __init__(
        self,
        dts_instance_id: str = None,
        ignore_error_sub_job: bool = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        self.dts_instance_id = dts_instance_id
        self.ignore_error_sub_job = ignore_error_sub_job
        # This parameter is required.
        self.region_id = region_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id

        if self.ignore_error_sub_job is not None:
            result['IgnoreErrorSubJob'] = self.ignore_error_sub_job

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')

        if m.get('IgnoreErrorSubJob') is not None:
            self.ignore_error_sub_job = m.get('IgnoreErrorSubJob')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

