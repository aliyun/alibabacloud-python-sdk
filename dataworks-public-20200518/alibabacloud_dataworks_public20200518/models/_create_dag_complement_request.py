# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDagComplementRequest(DaraModel):
    def __init__(
        self,
        biz_begin_time: str = None,
        biz_end_time: str = None,
        end_biz_date: str = None,
        exclude_node_ids: str = None,
        include_node_ids: str = None,
        name: str = None,
        node_params: str = None,
        parallelism: bool = None,
        project_env: str = None,
        root_node_id: int = None,
        start_biz_date: str = None,
    ):
        self.biz_begin_time = biz_begin_time
        self.biz_end_time = biz_end_time
        # This parameter is required.
        self.end_biz_date = end_biz_date
        self.exclude_node_ids = exclude_node_ids
        # This parameter is required.
        self.include_node_ids = include_node_ids
        # This parameter is required.
        self.name = name
        self.node_params = node_params
        # This parameter is required.
        self.parallelism = parallelism
        # This parameter is required.
        self.project_env = project_env
        # This parameter is required.
        self.root_node_id = root_node_id
        # This parameter is required.
        self.start_biz_date = start_biz_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_begin_time is not None:
            result['BizBeginTime'] = self.biz_begin_time

        if self.biz_end_time is not None:
            result['BizEndTime'] = self.biz_end_time

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizBeginTime') is not None:
            self.biz_begin_time = m.get('BizBeginTime')

        if m.get('BizEndTime') is not None:
            self.biz_end_time = m.get('BizEndTime')

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

        return self

