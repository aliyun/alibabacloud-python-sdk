# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListNodesRequest(DaraModel):
    def __init__(
        self,
        biz_name: str = None,
        node_name: str = None,
        owner: str = None,
        page_number: int = None,
        page_size: int = None,
        program_type: str = None,
        project_env: str = None,
        project_id: int = None,
        scheduler_type: str = None,
    ):
        # The error code returned.
        self.biz_name = biz_name
        # The ID of the baseline with which the node is associated.
        self.node_name = node_name
        # The description of the node.
        self.owner = owner
        # The page number. Minimum value: 1. Maximum value: 100.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The operation that you want to perform. Set the value to **ListNodes**.
        self.program_type = program_type
        # The environment in which the node runs. Valid values: DEV and PROD.
        # 
        # This parameter is required.
        self.project_env = project_env
        # The ID of the owner.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The scheduling type. Valid values:
        # 
        # *   NORMAL: Nodes are scheduled as expected.
        # *   PAUSE: Nodes are paused.
        # *   SKIP: Nodes are dry-run. Dry-run nodes are started as scheduled, but the system sets the status of the nodes to successful when it starts to run them.
        self.scheduler_type = scheduler_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_name is not None:
            result['BizName'] = self.biz_name

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.program_type is not None:
            result['ProgramType'] = self.program_type

        if self.project_env is not None:
            result['ProjectEnv'] = self.project_env

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.scheduler_type is not None:
            result['SchedulerType'] = self.scheduler_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProgramType') is not None:
            self.program_type = m.get('ProgramType')

        if m.get('ProjectEnv') is not None:
            self.project_env = m.get('ProjectEnv')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SchedulerType') is not None:
            self.scheduler_type = m.get('SchedulerType')

        return self

