# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yike20260319 import models as main_models
from darabonba.model import DaraModel

class ListYikeProductionsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        production_list: List[main_models.ListYikeProductionsResponseBodyProductionList] = None,
        request_id: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.production_list = production_list
        self.request_id = request_id

    def validate(self):
        if self.production_list:
            for v1 in self.production_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['ProductionList'] = []
        if self.production_list is not None:
            for k1 in self.production_list:
                result['ProductionList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.production_list = []
        if m.get('ProductionList') is not None:
            for k1 in m.get('ProductionList'):
                temp_model = main_models.ListYikeProductionsResponseBodyProductionList()
                self.production_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListYikeProductionsResponseBodyProductionList(DaraModel):
    def __init__(
        self,
        auth: str = None,
        cover_url: str = None,
        create_time: str = None,
        create_user_name: str = None,
        description: str = None,
        production_id: str = None,
        title: str = None,
        workspace_id: str = None,
    ):
        self.auth = auth
        self.cover_url = cover_url
        self.create_time = create_time
        self.create_user_name = create_user_name
        self.description = description
        self.production_id = production_id
        self.title = title
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth is not None:
            result['Auth'] = self.auth

        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name

        if self.description is not None:
            result['Description'] = self.description

        if self.production_id is not None:
            result['ProductionId'] = self.production_id

        if self.title is not None:
            result['Title'] = self.title

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Auth') is not None:
            self.auth = m.get('Auth')

        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ProductionId') is not None:
            self.production_id = m.get('ProductionId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

