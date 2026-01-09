# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateOutboundTaskRequest(DaraModel):
    def __init__(
        self,
        ani: str = None,
        call_infos: str = None,
        department_id: int = None,
        description: str = None,
        end_date: str = None,
        end_time: str = None,
        ext_attrs: str = None,
        group_name: str = None,
        instance_id: str = None,
        model: int = None,
        retry_interval: int = None,
        retry_time: int = None,
        skill_group: int = None,
        start_date: str = None,
        start_time: str = None,
        task_name: str = None,
        task_type: int = None,
    ):
        # This parameter is required.
        self.ani = ani
        self.call_infos = call_infos
        self.department_id = department_id
        self.description = description
        # This parameter is required.
        self.end_date = end_date
        # This parameter is required.
        self.end_time = end_time
        self.ext_attrs = ext_attrs
        self.group_name = group_name
        # This parameter is required.
        self.instance_id = instance_id
        self.model = model
        self.retry_interval = retry_interval
        self.retry_time = retry_time
        # This parameter is required.
        self.skill_group = skill_group
        # This parameter is required.
        self.start_date = start_date
        # This parameter is required.
        self.start_time = start_time
        # This parameter is required.
        self.task_name = task_name
        # This parameter is required.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ani is not None:
            result['Ani'] = self.ani

        if self.call_infos is not None:
            result['CallInfos'] = self.call_infos

        if self.department_id is not None:
            result['DepartmentId'] = self.department_id

        if self.description is not None:
            result['Description'] = self.description

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.ext_attrs is not None:
            result['ExtAttrs'] = self.ext_attrs

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.model is not None:
            result['Model'] = self.model

        if self.retry_interval is not None:
            result['RetryInterval'] = self.retry_interval

        if self.retry_time is not None:
            result['RetryTime'] = self.retry_time

        if self.skill_group is not None:
            result['SkillGroup'] = self.skill_group

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ani') is not None:
            self.ani = m.get('Ani')

        if m.get('CallInfos') is not None:
            self.call_infos = m.get('CallInfos')

        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ExtAttrs') is not None:
            self.ext_attrs = m.get('ExtAttrs')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('RetryInterval') is not None:
            self.retry_interval = m.get('RetryInterval')

        if m.get('RetryTime') is not None:
            self.retry_time = m.get('RetryTime')

        if m.get('SkillGroup') is not None:
            self.skill_group = m.get('SkillGroup')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

