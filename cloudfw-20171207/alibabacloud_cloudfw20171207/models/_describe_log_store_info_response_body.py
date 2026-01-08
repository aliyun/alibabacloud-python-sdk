# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLogStoreInfoResponseBody(DaraModel):
    def __init__(
        self,
        log_store_name: str = None,
        project_name: str = None,
        quota: int = None,
        region_id: str = None,
        request_id: str = None,
        ttl: int = None,
        used: int = None,
    ):
        # The name of the SLS LogStore in the log service.
        self.log_store_name = log_store_name
        # The Project name of the log service.
        self.project_name = project_name
        # Available log storage capacity. Unit: Byte.
        self.quota = quota
        # The region ID for log delivery.
        self.region_id = region_id
        # The ID of this request.
        self.request_id = request_id
        # Log storage duration. Unit: days.
        self.ttl = ttl
        # Used storage capacity. Unit: Byte.
        # 
        # > The statistics of the log service have a delay of approximately two hours.
        self.used = used

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.quota is not None:
            result['Quota'] = self.quota

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        if self.used is not None:
            result['Used'] = self.used

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Quota') is not None:
            self.quota = m.get('Quota')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        if m.get('Used') is not None:
            self.used = m.get('Used')

        return self

