# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCronJobPolicyServerlessResponseBody(DaraModel):
    def __init__(
        self,
        action: str = None,
        cron_expression: str = None,
        dbcluster_id: str = None,
        end_time: str = None,
        job_id: str = None,
        region_id: str = None,
        request_id: str = None,
        start_time: str = None,
        status: str = None,
    ):
        # The action of the scheduled task. The value is fixed as `ModifyDBClusterServerlessConf`.
        self.action = action
        # The Cron expression.
        self.cron_expression = cron_expression
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The end time of the task. The time is in the `yyyy-MM-ddTHH:mm:ssZ` format and in UTC.
        self.end_time = end_time
        # The ID of the scheduled task.
        self.job_id = job_id
        # The region ID.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The start time of the task. The time is in the `yyyy-MM-ddTHH:mm:ssZ` format and in UTC.
        self.start_time = start_time
        # The status of the task. Valid values:
        # 
        # - `working`: The scheduled task is running.
        # 
        # - `finish`: The scheduled task is complete.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

