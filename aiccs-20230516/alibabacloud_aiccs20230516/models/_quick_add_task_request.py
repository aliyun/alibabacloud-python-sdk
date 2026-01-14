# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiccs20230516 import models as main_models
from darabonba.model import DaraModel

class QuickAddTaskRequest(DaraModel):
    def __init__(
        self,
        agent_group_id: int = None,
        call_time_list: List[main_models.QuickAddTaskRequestCallTimeList] = None,
        name: str = None,
        owner_id: int = None,
        reference_task_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sms_template_id: int = None,
        start_time: str = None,
        template_id: int = None,
        template_type: int = None,
    ):
        # 坐席组ID
        self.agent_group_id = agent_group_id
        # 外呼时间
        self.call_time_list = call_time_list
        # 任务名称
        # 
        # This parameter is required.
        self.name = name
        self.owner_id = owner_id
        # 被复制任务ID
        # 
        # This parameter is required.
        self.reference_task_id = reference_task_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 短信模板ID
        self.sms_template_id = sms_template_id
        # 任务启动日期
        self.start_time = start_time
        # 话术模板ID,如果不传则使用被复制任务的话术模板
        self.template_id = template_id
        # 话术模板类型
        self.template_type = template_type

    def validate(self):
        if self.call_time_list:
            for v1 in self.call_time_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_group_id is not None:
            result['AgentGroupId'] = self.agent_group_id

        result['CallTimeList'] = []
        if self.call_time_list is not None:
            for k1 in self.call_time_list:
                result['CallTimeList'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.reference_task_id is not None:
            result['ReferenceTaskId'] = self.reference_task_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.sms_template_id is not None:
            result['SmsTemplateId'] = self.sms_template_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentGroupId') is not None:
            self.agent_group_id = m.get('AgentGroupId')

        self.call_time_list = []
        if m.get('CallTimeList') is not None:
            for k1 in m.get('CallTimeList'):
                temp_model = main_models.QuickAddTaskRequestCallTimeList()
                self.call_time_list.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ReferenceTaskId') is not None:
            self.reference_task_id = m.get('ReferenceTaskId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SmsTemplateId') is not None:
            self.sms_template_id = m.get('SmsTemplateId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        return self

class QuickAddTaskRequestCallTimeList(DaraModel):
    def __init__(
        self,
        call_time: List[str] = None,
    ):
        # 外呼时间
        self.call_time = call_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_time is not None:
            result['CallTime'] = self.call_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallTime') is not None:
            self.call_time = m.get('CallTime')

        return self

