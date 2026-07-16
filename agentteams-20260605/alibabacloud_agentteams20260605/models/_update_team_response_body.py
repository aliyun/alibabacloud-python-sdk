# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentteams20260605 import models as main_models
from darabonba.model import DaraModel

class UpdateTeamResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.UpdateTeamResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.UpdateTeamResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class UpdateTeamResponseBodyData(DaraModel):
    def __init__(
        self,
        admin_name: str = None,
        created_at: str = None,
        description: str = None,
        instance_id: str = None,
        leader_name: str = None,
        name: str = None,
        team_members: List[main_models.UpdateTeamResponseBodyDataTeamMembers] = None,
        updated_at: str = None,
        worker_names: List[str] = None,
    ):
        self.admin_name = admin_name
        self.created_at = created_at
        self.description = description
        self.instance_id = instance_id
        self.leader_name = leader_name
        self.name = name
        self.team_members = team_members
        self.updated_at = updated_at
        self.worker_names = worker_names

    def validate(self):
        if self.team_members:
            for v1 in self.team_members:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.admin_name is not None:
            result['AdminName'] = self.admin_name

        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.leader_name is not None:
            result['LeaderName'] = self.leader_name

        if self.name is not None:
            result['Name'] = self.name

        result['TeamMembers'] = []
        if self.team_members is not None:
            for k1 in self.team_members:
                result['TeamMembers'].append(k1.to_map() if k1 else None)

        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at

        if self.worker_names is not None:
            result['WorkerNames'] = self.worker_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdminName') is not None:
            self.admin_name = m.get('AdminName')

        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LeaderName') is not None:
            self.leader_name = m.get('LeaderName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.team_members = []
        if m.get('TeamMembers') is not None:
            for k1 in m.get('TeamMembers'):
                temp_model = main_models.UpdateTeamResponseBodyDataTeamMembers()
                self.team_members.append(temp_model.from_map(k1))

        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')

        if m.get('WorkerNames') is not None:
            self.worker_names = m.get('WorkerNames')

        return self

class UpdateTeamResponseBodyDataTeamMembers(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

