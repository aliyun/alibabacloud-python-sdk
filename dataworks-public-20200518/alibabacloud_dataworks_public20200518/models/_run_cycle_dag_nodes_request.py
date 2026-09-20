# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunCycleDagNodesRequest(DaraModel):
    def __init__(
        self,
        alert_notice_type: str = None,
        alert_type: str = None,
        biz_begin_time: str = None,
        biz_end_time: str = None,
        concurrent_runs: int = None,
        end_biz_date: str = None,
        exclude_node_ids: str = None,
        include_node_ids: str = None,
        name: str = None,
        node_params: str = None,
        parallelism: bool = None,
        project_env: str = None,
        root_node_id: int = None,
        start_biz_date: str = None,
        start_future_instance_immediately: bool = None,
    ):
        # The alert notification method. Valid values:
        # - SMS: text message.
        # - MAIL: email.
        # - SMS_MAIL: text message and email.
        self.alert_notice_type = alert_notice_type
        # The Alarm Metric. Valid values:
        # - SUCCESS: Alerting on success.
        # - FAILURE: Alerting on failed.
        # - SUCCESS_FAILURE: Alerting on success or failed.
        self.alert_type = alert_type
        # The start time of the node. This parameter is required only for hourly scheduled nodes. Format: HH:mm:ss. Valid values: 00:00:00 to 23:59:59.
        self.biz_begin_time = biz_begin_time
        # The end time of the node. This parameter is required only for hourly scheduled nodes. Format: HH:mm:ss. Valid values: 00:00:00 to 23:59:59.
        self.biz_end_time = biz_end_time
        # The number of concurrent nodes. Valid values: 2 to 10.
        self.concurrent_runs = concurrent_runs
        # The end business date for data backfill. Format: yyyy-MM-dd 00:00:00.
        # 
        # This parameter is required.
        self.end_biz_date = end_biz_date
        # The list of node IDs that do not require data backfill. Nodes in this list generate dry-run instances. After a dry-run instance is scheduled, it directly succeeds without executing the script content.
        self.exclude_node_ids = exclude_node_ids
        # The node IDs for data backfill. Separate multiple node IDs with commas (,). You can call the [ListNodes](https://help.aliyun.com/document_detail/173979.html) operation to obtain node IDs.
        # 
        # This parameter is required.
        self.include_node_ids = include_node_ids
        # The name of the workflow.
        # 
        # This parameter is required.
        self.name = name
        # A JSON string in which the key is the node ID and the value is the actual parameter value.
        self.node_params = node_params
        # Specifies whether nodes across multiple business dates can run in parallel.
        # 
        # This parameter is required.
        self.parallelism = parallelism
        # The environment of the workspace. PROD indicates the production environment. DEV indicates the development environment.
        # 
        # This parameter is required.
        self.project_env = project_env
        # The ID of the start node for data backfill. You can call the [ListNodes](https://help.aliyun.com/document_detail/173979.html) operation to obtain the node ID.
        # 
        # This parameter is required.
        self.root_node_id = root_node_id
        # The start business date for data backfill. Format: yyyy-MM-dd 00:00:00.
        # 
        # This parameter is required.
        self.start_biz_date = start_biz_date
        # Specifies whether to immediately run instances whose scheduling time is in the future. If this parameter is set to true, instances with a scheduling time later than the current time run immediately. Otherwise, the instances wait until the scheduling time.
        self.start_future_instance_immediately = start_future_instance_immediately

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_notice_type is not None:
            result['AlertNoticeType'] = self.alert_notice_type

        if self.alert_type is not None:
            result['AlertType'] = self.alert_type

        if self.biz_begin_time is not None:
            result['BizBeginTime'] = self.biz_begin_time

        if self.biz_end_time is not None:
            result['BizEndTime'] = self.biz_end_time

        if self.concurrent_runs is not None:
            result['ConcurrentRuns'] = self.concurrent_runs

        if self.end_biz_date is not None:
            result['EndBizDate'] = self.end_biz_date

        if self.exclude_node_ids is not None:
            result['ExcludeNodeIds'] = self.exclude_node_ids

        if self.include_node_ids is not None:
            result['IncludeNodeIds'] = self.include_node_ids

        if self.name is not None:
            result['Name'] = self.name

        if self.node_params is not None:
            result['NodeParams'] = self.node_params

        if self.parallelism is not None:
            result['Parallelism'] = self.parallelism

        if self.project_env is not None:
            result['ProjectEnv'] = self.project_env

        if self.root_node_id is not None:
            result['RootNodeId'] = self.root_node_id

        if self.start_biz_date is not None:
            result['StartBizDate'] = self.start_biz_date

        if self.start_future_instance_immediately is not None:
            result['StartFutureInstanceImmediately'] = self.start_future_instance_immediately

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertNoticeType') is not None:
            self.alert_notice_type = m.get('AlertNoticeType')

        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')

        if m.get('BizBeginTime') is not None:
            self.biz_begin_time = m.get('BizBeginTime')

        if m.get('BizEndTime') is not None:
            self.biz_end_time = m.get('BizEndTime')

        if m.get('ConcurrentRuns') is not None:
            self.concurrent_runs = m.get('ConcurrentRuns')

        if m.get('EndBizDate') is not None:
            self.end_biz_date = m.get('EndBizDate')

        if m.get('ExcludeNodeIds') is not None:
            self.exclude_node_ids = m.get('ExcludeNodeIds')

        if m.get('IncludeNodeIds') is not None:
            self.include_node_ids = m.get('IncludeNodeIds')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NodeParams') is not None:
            self.node_params = m.get('NodeParams')

        if m.get('Parallelism') is not None:
            self.parallelism = m.get('Parallelism')

        if m.get('ProjectEnv') is not None:
            self.project_env = m.get('ProjectEnv')

        if m.get('RootNodeId') is not None:
            self.root_node_id = m.get('RootNodeId')

        if m.get('StartBizDate') is not None:
            self.start_biz_date = m.get('StartBizDate')

        if m.get('StartFutureInstanceImmediately') is not None:
            self.start_future_instance_immediately = m.get('StartFutureInstanceImmediately')

        return self

