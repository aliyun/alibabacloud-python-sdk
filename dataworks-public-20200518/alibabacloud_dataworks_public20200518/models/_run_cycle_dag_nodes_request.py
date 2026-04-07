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
        # 
        # *   SMS
        # *   MAIL
        # *   SMS_MAIL
        self.alert_notice_type = alert_notice_type
        # The alert type. Valid values:
        # 
        # *   SUCCESS: An alert is generated when data backfill succeeds.
        # *   FAILURE: An alert is generated when data backfill fails.
        # *   SUCCESS_FAILURE: An alert is generated regardless of whether data backfill succeeds or fails.
        self.alert_type = alert_type
        # The time when the node starts to run. This parameter is required only for auto triggered nodes that are scheduled by hour. Specify the value in the HH:mm:ss format. Valid values: 00:00:00 to 23:59:59.
        self.biz_begin_time = biz_begin_time
        # The time when the node stops running. This parameter is required only for auto triggered nodes that are scheduled by hour. Specify the value in the HH:mm:ss format. Valid values: 00:00:00 to 23:59:59.
        self.biz_end_time = biz_end_time
        # The number of nodes that can run in parallel. Valid values: 2 to 10.
        self.concurrent_runs = concurrent_runs
        # The data timestamp at which data is no longer backfilled. Specify the value in the yyyy-MM-dd 00:00:00 format.
        # 
        # This parameter is required.
        self.end_biz_date = end_biz_date
        # The IDs of the nodes for which no data needs to be backfilled. The system generates dry-run instances for all these nodes. After these dry-run instances are scheduled, the statuses of these instances are directly set to successful, but the script is not run.
        self.exclude_node_ids = exclude_node_ids
        # The ID of the node for which you want to backfill data. If you want to backfill data for multiple nodes, separate the IDs of the nodes with commas (,). You can call the [ListNodes](https://help.aliyun.com/document_detail/173979.html) operation to obtain the node ID.
        # 
        # This parameter is required.
        self.include_node_ids = include_node_ids
        # The name of the workflow.
        # 
        # This parameter is required.
        self.name = name
        # The parameters that need to be configured for the node. Set this parameter to a JSON string. The key indicates the ID of the node, and the value indicates the actual values of the parameters.
        self.node_params = node_params
        # Specifies whether data can be backfilled for multiple nodes at the same time.
        # 
        # This parameter is required.
        self.parallelism = parallelism
        # The environment of the workspace. Valid values: PROD and DEV. The value PROD indicates the production environment, and the value DEV indicates the development environment.
        # 
        # This parameter is required.
        self.project_env = project_env
        # The ID of the node for which data is first backfilled. You can call the [ListNodes](https://help.aliyun.com/document_detail/173979.html) operation to obtain the node ID.
        # 
        # This parameter is required.
        self.root_node_id = root_node_id
        # The data timestamp at which data starts to be backfilled. Specify the value in the yyyy-MM-dd 00:00:00 format.
        # 
        # This parameter is required.
        self.start_biz_date = start_biz_date
        # Specifies whether to immediately run an instance that is scheduled to run in the future. If you set this parameter to true, the instance that is scheduled to run in the future is run immediately. Otherwise, the instance is run as scheduled.
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

