# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class ListPluginRepositoriesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListPluginRepositoriesResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
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
            result['code'] = self.code

        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.ListPluginRepositoriesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListPluginRepositoriesResponseBodyData(DaraModel):
    def __init__(
        self,
        organization_id: str = None,
        organization_name: str = None,
        repositories: List[main_models.ListPluginRepositoriesResponseBodyDataRepositories] = None,
    ):
        self.organization_id = organization_id
        self.organization_name = organization_name
        self.repositories = repositories

    def validate(self):
        if self.repositories:
            for v1 in self.repositories:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.organization_id is not None:
            result['organizationId'] = self.organization_id

        if self.organization_name is not None:
            result['organizationName'] = self.organization_name

        result['repositories'] = []
        if self.repositories is not None:
            for k1 in self.repositories:
                result['repositories'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('organizationId') is not None:
            self.organization_id = m.get('organizationId')

        if m.get('organizationName') is not None:
            self.organization_name = m.get('organizationName')

        self.repositories = []
        if m.get('repositories') is not None:
            for k1 in m.get('repositories'):
                temp_model = main_models.ListPluginRepositoriesResponseBodyDataRepositories()
                self.repositories.append(temp_model.from_map(k1))

        return self

class ListPluginRepositoriesResponseBodyDataRepositories(DaraModel):
    def __init__(
        self,
        repository_id: str = None,
        repository_name: str = None,
    ):
        self.repository_id = repository_id
        self.repository_name = repository_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.repository_id is not None:
            result['repositoryId'] = self.repository_id

        if self.repository_name is not None:
            result['repositoryName'] = self.repository_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('repositoryId') is not None:
            self.repository_id = m.get('repositoryId')

        if m.get('repositoryName') is not None:
            self.repository_name = m.get('repositoryName')

        return self

