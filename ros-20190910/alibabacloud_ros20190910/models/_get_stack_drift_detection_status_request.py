# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetStackDriftDetectionStatusRequest(DaraModel):
    def __init__(
        self,
        drift_detection_id: str = None,
        region_id: str = None,
    ):
        # The ID of the drift detection operation.
        # 
        # You can call the [ListStackResourceDrifts](https://help.aliyun.com/document_detail/155098.html) operation to obtain the ID of the drift detection operation.
        # 
        # This parameter is required.
        self.drift_detection_id = drift_detection_id
        # The region ID of the stack to be detected for drift.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/131035.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.drift_detection_id is not None:
            result['DriftDetectionId'] = self.drift_detection_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DriftDetectionId') is not None:
            self.drift_detection_id = m.get('DriftDetectionId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

