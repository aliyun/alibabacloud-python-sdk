# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExecuteAdhocWorkflowInstanceShrinkRequest(DaraModel):
    def __init__(
        self,
        biz_date: int = None,
        env_type: str = None,
        name: str = None,
        owner: str = None,
        project_id: int = None,
        tasks_shrink: str = None,
    ):
        # The data timestamp.
        self.biz_date = biz_date
        # The environment of the workspace. Valid values:
        # 
        # *   Prod: production environment
        # *   Dev: development environment
        self.env_type = env_type
        # The name of the workflow instance.
        # 
        # This parameter is required.
        self.name = name
        # The account ID of the owner.
        # 
        # This parameter is required.
        self.owner = owner
        # The workspace ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The tasks.
        # 
        # This parameter is required.
        self.tasks_shrink = tasks_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_date is not None:
            result['BizDate'] = self.biz_date

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.tasks_shrink is not None:
            result['Tasks'] = self.tasks_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Tasks') is not None:
            self.tasks_shrink = m.get('Tasks')

        return self

