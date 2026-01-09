# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryTaskDetailRequest(DaraModel):
    def __init__(
        self,
        ani: str = None,
        current_page: int = None,
        department_id_list: str = None,
        dnis: str = None,
        end_reason_list: str = None,
        instance_id: str = None,
        outbound_task_id: str = None,
        page_size: int = None,
        priority_list: str = None,
        servicer_id: str = None,
        servicer_name: str = None,
        sid: str = None,
        skill_group: str = None,
        status_list: str = None,
        task_id: int = None,
    ):
        self.ani = ani
        self.current_page = current_page
        self.department_id_list = department_id_list
        self.dnis = dnis
        self.end_reason_list = end_reason_list
        # This parameter is required.
        self.instance_id = instance_id
        self.outbound_task_id = outbound_task_id
        self.page_size = page_size
        self.priority_list = priority_list
        self.servicer_id = servicer_id
        self.servicer_name = servicer_name
        self.sid = sid
        self.skill_group = skill_group
        self.status_list = status_list
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ani is not None:
            result['Ani'] = self.ani

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.department_id_list is not None:
            result['DepartmentIdList'] = self.department_id_list

        if self.dnis is not None:
            result['Dnis'] = self.dnis

        if self.end_reason_list is not None:
            result['EndReasonList'] = self.end_reason_list

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.outbound_task_id is not None:
            result['OutboundTaskId'] = self.outbound_task_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.priority_list is not None:
            result['PriorityList'] = self.priority_list

        if self.servicer_id is not None:
            result['ServicerId'] = self.servicer_id

        if self.servicer_name is not None:
            result['ServicerName'] = self.servicer_name

        if self.sid is not None:
            result['Sid'] = self.sid

        if self.skill_group is not None:
            result['SkillGroup'] = self.skill_group

        if self.status_list is not None:
            result['StatusList'] = self.status_list

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ani') is not None:
            self.ani = m.get('Ani')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DepartmentIdList') is not None:
            self.department_id_list = m.get('DepartmentIdList')

        if m.get('Dnis') is not None:
            self.dnis = m.get('Dnis')

        if m.get('EndReasonList') is not None:
            self.end_reason_list = m.get('EndReasonList')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OutboundTaskId') is not None:
            self.outbound_task_id = m.get('OutboundTaskId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PriorityList') is not None:
            self.priority_list = m.get('PriorityList')

        if m.get('ServicerId') is not None:
            self.servicer_id = m.get('ServicerId')

        if m.get('ServicerName') is not None:
            self.servicer_name = m.get('ServicerName')

        if m.get('Sid') is not None:
            self.sid = m.get('Sid')

        if m.get('SkillGroup') is not None:
            self.skill_group = m.get('SkillGroup')

        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

