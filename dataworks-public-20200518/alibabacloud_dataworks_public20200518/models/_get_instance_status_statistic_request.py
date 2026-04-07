# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetInstanceStatusStatisticRequest(DaraModel):
    def __init__(
        self,
        biz_date: str = None,
        dag_type: str = None,
        project_env: str = None,
        project_id: int = None,
        scheduler_period: str = None,
        scheduler_type: str = None,
    ):
        # The date on which the numbers of instances in different states are obtained. Specify the date in the yyyy-MM-dd format.
        # 
        # This parameter is required.
        self.biz_date = biz_date
        # The type of the directed acyclic graph (DAG). Valid values:
        # 
        # *   MANUAL: DAG for a manually triggered workflow
        # *   SMOKE_TEST: DAG for a smoke testing workflow
        # *   SUPPLY_DATA: DAG for a data backfill instance
        # *   BUSINESS_PROCESS_DAG: DAG for a one-time workflow
        # 
        # <!---->
        # 
        # *   DAILY
        # *   MANUAL
        # *   SMOKE_TEST
        # *   SUPPLY_DATA
        # *   BUSINESS_PROCESS_DAG
        self.dag_type = dag_type
        # The runtime environment. Valid values: PROD and DEV.
        # 
        # This parameter is required.
        self.project_env = project_env
        # The DataWorks workspace ID. You can log on to the DataWorks console and go to the Workspace page to query the ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The scheduling cycle. Valid values:
        # 
        # *   MINUTE
        # *   HOUR
        # *   DAY
        # *   WEEK
        # *   MONTH
        self.scheduler_period = scheduler_period
        # The scheduling type of the node. Valid values:
        # 
        # *   NORMAL: auto triggered node
        # *   MANUAL: manually triggered node
        # *   PAUSE: paused node
        # *   SKIP: dry-run node
        self.scheduler_type = scheduler_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_date is not None:
            result['BizDate'] = self.biz_date

        if self.dag_type is not None:
            result['DagType'] = self.dag_type

        if self.project_env is not None:
            result['ProjectEnv'] = self.project_env

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.scheduler_period is not None:
            result['SchedulerPeriod'] = self.scheduler_period

        if self.scheduler_type is not None:
            result['SchedulerType'] = self.scheduler_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')

        if m.get('DagType') is not None:
            self.dag_type = m.get('DagType')

        if m.get('ProjectEnv') is not None:
            self.project_env = m.get('ProjectEnv')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SchedulerPeriod') is not None:
            self.scheduler_period = m.get('SchedulerPeriod')

        if m.get('SchedulerType') is not None:
            self.scheduler_type = m.get('SchedulerType')

        return self

