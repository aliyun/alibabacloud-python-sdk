# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_intelligentcreation20240313 import models as main_models
from darabonba.model import DaraModel

class ListAvatarProjectResponseBody(DaraModel):
    def __init__(
        self,
        query_avatar_project_result_list: List[main_models.ListAvatarProjectResponseBodyQueryAvatarProjectResultList] = None,
        request_id: str = None,
    ):
        self.query_avatar_project_result_list = query_avatar_project_result_list
        self.request_id = request_id

    def validate(self):
        if self.query_avatar_project_result_list:
            for v1 in self.query_avatar_project_result_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['queryAvatarProjectResultList'] = []
        if self.query_avatar_project_result_list is not None:
            for k1 in self.query_avatar_project_result_list:
                result['queryAvatarProjectResultList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.query_avatar_project_result_list = []
        if m.get('queryAvatarProjectResultList') is not None:
            for k1 in m.get('queryAvatarProjectResultList'):
                temp_model = main_models.ListAvatarProjectResponseBodyQueryAvatarProjectResultList()
                self.query_avatar_project_result_list.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListAvatarProjectResponseBodyQueryAvatarProjectResultList(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        error_msg: str = None,
        project_id: str = None,
        project_name: str = None,
        status: str = None,
    ):
        self.agent_id = agent_id
        self.error_msg = error_msg
        self.project_id = project_id
        self.project_name = project_name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg

        if self.project_id is not None:
            result['projectId'] = self.project_id

        if self.project_name is not None:
            result['projectName'] = self.project_name

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')

        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')

        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

