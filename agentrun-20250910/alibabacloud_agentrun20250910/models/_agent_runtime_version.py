# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AgentRuntimeVersion(DaraModel):
    def __init__(
        self,
        agent_runtime_arn: str = None,
        agent_runtime_id: str = None,
        agent_runtime_name: str = None,
        agent_runtime_version: str = None,
        description: str = None,
        last_updated_at: str = None,
    ):
        # 智能体运行时的ARN
        self.agent_runtime_arn = agent_runtime_arn
        # 智能体运行时的ID
        self.agent_runtime_id = agent_runtime_id
        # 智能体运行时的名称
        self.agent_runtime_name = agent_runtime_name
        # 已发布版本的版本号
        self.agent_runtime_version = agent_runtime_version
        # 此版本的描述
        self.description = description
        # 最后更新的时间戳
        self.last_updated_at = last_updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_runtime_arn is not None:
            result['agentRuntimeArn'] = self.agent_runtime_arn

        if self.agent_runtime_id is not None:
            result['agentRuntimeId'] = self.agent_runtime_id

        if self.agent_runtime_name is not None:
            result['agentRuntimeName'] = self.agent_runtime_name

        if self.agent_runtime_version is not None:
            result['agentRuntimeVersion'] = self.agent_runtime_version

        if self.description is not None:
            result['description'] = self.description

        if self.last_updated_at is not None:
            result['lastUpdatedAt'] = self.last_updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentRuntimeArn') is not None:
            self.agent_runtime_arn = m.get('agentRuntimeArn')

        if m.get('agentRuntimeId') is not None:
            self.agent_runtime_id = m.get('agentRuntimeId')

        if m.get('agentRuntimeName') is not None:
            self.agent_runtime_name = m.get('agentRuntimeName')

        if m.get('agentRuntimeVersion') is not None:
            self.agent_runtime_version = m.get('agentRuntimeVersion')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('lastUpdatedAt') is not None:
            self.last_updated_at = m.get('lastUpdatedAt')

        return self

