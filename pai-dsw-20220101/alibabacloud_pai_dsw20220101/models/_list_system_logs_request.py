# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSystemLogsRequest(DaraModel):
    def __init__(
        self,
        gmt_end_time: str = None,
        gmt_start_time: str = None,
        instance_id: str = None,
        lifecycle_id: str = None,
        log_level: str = None,
        log_repository: str = None,
        offset: str = None,
        order: str = None,
        problem_category: str = None,
        sort_by: str = None,
        source_request_id: str = None,
    ):
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.gmt_end_time = gmt_end_time
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.gmt_start_time = gmt_start_time
        self.instance_id = instance_id
        self.lifecycle_id = lifecycle_id
        self.log_level = log_level
        self.log_repository = log_repository
        self.offset = offset
        self.order = order
        self.problem_category = problem_category
        self.sort_by = sort_by
        self.source_request_id = source_request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_end_time is not None:
            result['GmtEndTime'] = self.gmt_end_time

        if self.gmt_start_time is not None:
            result['GmtStartTime'] = self.gmt_start_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lifecycle_id is not None:
            result['LifecycleId'] = self.lifecycle_id

        if self.log_level is not None:
            result['LogLevel'] = self.log_level

        if self.log_repository is not None:
            result['LogRepository'] = self.log_repository

        if self.offset is not None:
            result['Offset'] = self.offset

        if self.order is not None:
            result['Order'] = self.order

        if self.problem_category is not None:
            result['ProblemCategory'] = self.problem_category

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.source_request_id is not None:
            result['SourceRequestId'] = self.source_request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtEndTime') is not None:
            self.gmt_end_time = m.get('GmtEndTime')

        if m.get('GmtStartTime') is not None:
            self.gmt_start_time = m.get('GmtStartTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LifecycleId') is not None:
            self.lifecycle_id = m.get('LifecycleId')

        if m.get('LogLevel') is not None:
            self.log_level = m.get('LogLevel')

        if m.get('LogRepository') is not None:
            self.log_repository = m.get('LogRepository')

        if m.get('Offset') is not None:
            self.offset = m.get('Offset')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('ProblemCategory') is not None:
            self.problem_category = m.get('ProblemCategory')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('SourceRequestId') is not None:
            self.source_request_id = m.get('SourceRequestId')

        return self

