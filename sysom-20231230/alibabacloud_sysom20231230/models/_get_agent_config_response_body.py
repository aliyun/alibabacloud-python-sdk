# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class GetAgentConfigResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.GetAgentConfigResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        total: int = None,
    ):
        # The status code.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        # - If `code == Success`, this field is empty.
        # - Otherwise, this field contains the error message of the request.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # The number of returned records.
        self.total = total

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

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.GetAgentConfigResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class GetAgentConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        config_id: str = None,
        config_name: str = None,
        config_type: str = None,
        content: str = None,
        created_at: str = None,
        resource: main_models.GetAgentConfigResponseBodyDataResource = None,
        updated_at: str = None,
    ):
        # The ID of the component configuration.
        self.config_id = config_id
        # The name of the configuration.
        self.config_name = config_name
        # The type of the configuration.
        self.config_type = config_type
        # The text of the chat content.
        self.content = content
        # The creation time.
        self.created_at = created_at
        # The information about the resources to which the configuration is applied.
        self.resource = resource
        # The update time.
        self.updated_at = updated_at

    def validate(self):
        if self.resource:
            self.resource.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['configId'] = self.config_id

        if self.config_name is not None:
            result['configName'] = self.config_name

        if self.config_type is not None:
            result['configType'] = self.config_type

        if self.content is not None:
            result['content'] = self.content

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.resource is not None:
            result['resource'] = self.resource.to_map()

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configId') is not None:
            self.config_id = m.get('configId')

        if m.get('configName') is not None:
            self.config_name = m.get('configName')

        if m.get('configType') is not None:
            self.config_type = m.get('configType')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('resource') is not None:
            temp_model = main_models.GetAgentConfigResponseBodyDataResource()
            self.resource = temp_model.from_map(m.get('resource'))

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        return self

class GetAgentConfigResponseBodyDataResource(DaraModel):
    def __init__(
        self,
        cluster: int = None,
        node: int = None,
    ):
        # The number of clusters to which the configuration is applied.
        self.cluster = cluster
        # The number of nodes to which the configuration is applied.
        self.node = node

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster is not None:
            result['cluster'] = self.cluster

        if self.node is not None:
            result['node'] = self.node

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')

        if m.get('node') is not None:
            self.node = m.get('node')

        return self

