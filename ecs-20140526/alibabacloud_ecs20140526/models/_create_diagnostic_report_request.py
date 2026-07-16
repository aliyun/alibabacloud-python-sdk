# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class CreateDiagnosticReportRequest(DaraModel):
    def __init__(
        self,
        additional_options: Dict[str, str] = None,
        end_time: str = None,
        metric_set_id: str = None,
        region_id: str = None,
        resource_id: str = None,
        start_time: str = None,
    ):
        self.additional_options = additional_options
        # The end time. This parameter applies only to diagnostic metrics that do not require running Cloud Assistant commands in the guest OS.
        self.end_time = end_time
        # The diagnostic metric set ID. If this parameter is omitted, the default diagnostic metric set for ECS instances, `dms-instancedefault`, is used.
        self.metric_set_id = metric_set_id
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to get the latest list of Alibaba Cloud regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource ID.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The start time. This parameter applies only to diagnostic metrics that do not require running Cloud Assistant commands in the guest OS.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.additional_options is not None:
            result['AdditionalOptions'] = self.additional_options

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.metric_set_id is not None:
            result['MetricSetId'] = self.metric_set_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalOptions') is not None:
            self.additional_options = m.get('AdditionalOptions')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('MetricSetId') is not None:
            self.metric_set_id = m.get('MetricSetId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

