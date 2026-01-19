# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudcallcenter20200701 import models as main_models
from darabonba.model import DaraModel

class ListMonoRecordingsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListMonoRecordingsResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListMonoRecordingsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListMonoRecordingsResponseBodyData(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_name: str = None,
        contact_id: str = None,
        duration: str = None,
        file_name: str = None,
        file_url: str = None,
        ram_id: str = None,
        skill_group_id: str = None,
        start_time: str = None,
    ):
        self.agent_id = agent_id
        self.agent_name = agent_name
        self.contact_id = contact_id
        self.duration = duration
        self.file_name = file_name
        self.file_url = file_url
        self.ram_id = ram_id
        self.skill_group_id = skill_group_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.contact_id is not None:
            result['ContactId'] = self.contact_id

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.ram_id is not None:
            result['RamId'] = self.ram_id

        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('RamId') is not None:
            self.ram_id = m.get('RamId')

        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

