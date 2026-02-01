# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class ListClusterAgentInstallRecordsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: List[main_models.ListClusterAgentInstallRecordsResponseBodyData] = None,
        message: str = None,
        total: int = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data
        self.message = message
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.code is not None:
            result['code'] = self.code

        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('code') is not None:
            self.code = m.get('code')

        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.ListClusterAgentInstallRecordsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListClusterAgentInstallRecordsResponseBodyData(DaraModel):
    def __init__(
        self,
        agent_config_id: str = None,
        agent_config_name: str = None,
        cluster_id: str = None,
        created_at: str = None,
        grayscale_config: str = None,
        plugin_id: str = None,
        plugin_version: str = None,
        updated_at: str = None,
    ):
        self.agent_config_id = agent_config_id
        self.agent_config_name = agent_config_name
        self.cluster_id = cluster_id
        self.created_at = created_at
        self.grayscale_config = grayscale_config
        self.plugin_id = plugin_id
        self.plugin_version = plugin_version
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_config_id is not None:
            result['agent_config_id'] = self.agent_config_id

        if self.agent_config_name is not None:
            result['agent_config_name'] = self.agent_config_name

        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id

        if self.created_at is not None:
            result['created_at'] = self.created_at

        if self.grayscale_config is not None:
            result['grayscale_config'] = self.grayscale_config

        if self.plugin_id is not None:
            result['plugin_id'] = self.plugin_id

        if self.plugin_version is not None:
            result['plugin_version'] = self.plugin_version

        if self.updated_at is not None:
            result['updated_at'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agent_config_id') is not None:
            self.agent_config_id = m.get('agent_config_id')

        if m.get('agent_config_name') is not None:
            self.agent_config_name = m.get('agent_config_name')

        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')

        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')

        if m.get('grayscale_config') is not None:
            self.grayscale_config = m.get('grayscale_config')

        if m.get('plugin_id') is not None:
            self.plugin_id = m.get('plugin_id')

        if m.get('plugin_version') is not None:
            self.plugin_version = m.get('plugin_version')

        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')

        return self

