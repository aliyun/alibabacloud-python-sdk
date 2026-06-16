# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentloop20260520 import models as main_models
from darabonba.model import DaraModel

class ListAgentSpacesResponseBody(DaraModel):
    def __init__(
        self,
        agent_spaces: List[main_models.ListAgentSpacesResponseBodyAgentSpaces] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total: int = None,
    ):
        self.agent_spaces = agent_spaces
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total = total

    def validate(self):
        if self.agent_spaces:
            for v1 in self.agent_spaces:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['agentSpaces'] = []
        if self.agent_spaces is not None:
            for k1 in self.agent_spaces:
                result['agentSpaces'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.agent_spaces = []
        if m.get('agentSpaces') is not None:
            for k1 in m.get('agentSpaces'):
                temp_model = main_models.ListAgentSpacesResponseBodyAgentSpaces()
                self.agent_spaces.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListAgentSpacesResponseBodyAgentSpaces(DaraModel):
    def __init__(
        self,
        agent_space: str = None,
        cms_workspace: str = None,
        create_time: str = None,
        description: str = None,
        mse_namespace: main_models.ListAgentSpacesResponseBodyAgentSpacesMseNamespace = None,
        region_id: str = None,
        sls_project: str = None,
        update_time: str = None,
    ):
        self.agent_space = agent_space
        self.cms_workspace = cms_workspace
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.create_time = create_time
        self.description = description
        self.mse_namespace = mse_namespace
        self.region_id = region_id
        self.sls_project = sls_project
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.update_time = update_time

    def validate(self):
        if self.mse_namespace:
            self.mse_namespace.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_space is not None:
            result['agentSpace'] = self.agent_space

        if self.cms_workspace is not None:
            result['cmsWorkspace'] = self.cms_workspace

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.description is not None:
            result['description'] = self.description

        if self.mse_namespace is not None:
            result['mseNamespace'] = self.mse_namespace.to_map()

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.sls_project is not None:
            result['slsProject'] = self.sls_project

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentSpace') is not None:
            self.agent_space = m.get('agentSpace')

        if m.get('cmsWorkspace') is not None:
            self.cms_workspace = m.get('cmsWorkspace')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('mseNamespace') is not None:
            temp_model = main_models.ListAgentSpacesResponseBodyAgentSpacesMseNamespace()
            self.mse_namespace = temp_model.from_map(m.get('mseNamespace'))

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('slsProject') is not None:
            self.sls_project = m.get('slsProject')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

class ListAgentSpacesResponseBodyAgentSpacesMseNamespace(DaraModel):
    def __init__(
        self,
        namespace_id: str = None,
        namespace_name: str = None,
    ):
        self.namespace_id = namespace_id
        self.namespace_name = namespace_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.namespace_id is not None:
            result['namespaceId'] = self.namespace_id

        if self.namespace_name is not None:
            result['namespaceName'] = self.namespace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('namespaceId') is not None:
            self.namespace_id = m.get('namespaceId')

        if m.get('namespaceName') is not None:
            self.namespace_name = m.get('namespaceName')

        return self

