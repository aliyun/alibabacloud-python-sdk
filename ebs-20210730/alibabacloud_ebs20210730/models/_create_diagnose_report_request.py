# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDiagnoseReportRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        diagnose_type: str = None,
        end_time: str = None,
        region_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
        start_time: str = None,
    ):
        # A client-generated token to ensure request idempotency. This lets you safely retry the request without creating a duplicate diagnostic report. The token can contain a maximum of 64 ASCII characters.
        self.client_token = client_token
        # The diagnosis type. The only valid value is:
        # 
        # - Performance: performance diagnosis
        # 
        # This parameter is required.
        self.diagnose_type = diagnose_type
        # The end time for the diagnosis, in UTC. The time must be in the ISO 8601 format (yyyy-MM-ddTHH:mm:ssZ).
        self.end_time = end_time
        # The region ID. Call the [DescribeRegions](https://help.aliyun.com/zh/ecs/developer-reference/api-ebs-2021-07-30-describeregions?spm=a2c4g.11186623.0.i7) operation to find all regions supported by EBS Data Insight.
        self.region_id = region_id
        # The resource ID.
        self.resource_id = resource_id
        # The resource type. The only valid value is:
        # 
        # - Disk: a cloud disk
        self.resource_type = resource_type
        # The start time for the diagnosis, in UTC. The time must be in the ISO 8601 format (yyyy-MM-ddTHH:mm:ssZ).
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.diagnose_type is not None:
            result['DiagnoseType'] = self.diagnose_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DiagnoseType') is not None:
            self.diagnose_type = m.get('DiagnoseType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

