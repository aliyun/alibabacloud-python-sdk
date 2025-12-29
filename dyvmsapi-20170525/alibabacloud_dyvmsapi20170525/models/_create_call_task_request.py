# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCallTaskRequest(DaraModel):
    def __init__(
        self,
        biz_type: str = None,
        data: str = None,
        data_type: str = None,
        fire_time: str = None,
        owner_id: int = None,
        resource: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        schedule_type: str = None,
        stop_time: str = None,
        task_name: str = None,
        template_code: str = None,
        template_name: str = None,
    ):
        # The type of the task template. Valid values:
        # 
        # *   **VMS_VOICE_TTS**: the text-to-speech (TTS) notification template.
        # *   **VMS_VOICE_CODE**: the voice notification template.
        # *   **VMS_TTS**: the voice verification code template.
        self.biz_type = biz_type
        # The called numbers.
        # 
        # *   If you set DataType to LIST, the value of Data is in the LIST format.
        # *   If you set DataType to JSON, the value of Data is in the JSON format.
        self.data = data
        # The type of called numbers. Valid values:
        # 
        # *   **LIST**: the called numbers that are separated by commas (,).
        # *   **JSON**: a JSON-formatted list of called numbers with template parameters.
        self.data_type = data_type
        # This parameter is unavailable.
        self.fire_time = fire_time
        self.owner_id = owner_id
        # The calling number. Only virtual numbers are supported.
        self.resource = resource
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The type of the calling number. Set the value to **LIST**.
        self.resource_type = resource_type
        # This parameter is unavailable.
        self.schedule_type = schedule_type
        # This parameter is unavailable.
        self.stop_time = stop_time
        # The task name.
        self.task_name = task_name
        # The template ID.
        self.template_code = template_code
        # The template name.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.data is not None:
            result['Data'] = self.data

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.fire_time is not None:
            result['FireTime'] = self.fire_time

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource is not None:
            result['Resource'] = self.resource

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type

        if self.stop_time is not None:
            result['StopTime'] = self.stop_time

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.template_code is not None:
            result['TemplateCode'] = self.template_code

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('FireTime') is not None:
            self.fire_time = m.get('FireTime')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Resource') is not None:
            self.resource = m.get('Resource')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')

        if m.get('StopTime') is not None:
            self.stop_time = m.get('StopTime')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

