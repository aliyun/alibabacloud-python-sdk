# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class GetAgentRuntimeStatisticResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetAgentRuntimeStatisticResponseBodyData] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of runtime statistics grouped by agent platform and agent provider. If AgentProvider is specified but no matching runtimes are found, a record with all statistical values set to 0 is returned.
        self.data = data
        # The request ID, which uniquely identifies the request.
        self.request_id = request_id
        # The number of returned statistics records, which is the length of the Data list.
        self.total_count = total_count

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
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetAgentRuntimeStatisticResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class GetAgentRuntimeStatisticResponseBodyData(DaraModel):
    def __init__(
        self,
        agent_display_name: str = None,
        agent_platform: str = None,
        agent_provider: str = None,
        expired_count: int = None,
        no_channel_configured_runtime_count: int = None,
        no_model_configured_runtime_count: int = None,
        risky_runtime_count: int = None,
        total_runtime_count: int = None,
    ):
        # The agent display name, which is determined by both the agent platform and the agent provider. For example, OpenClaw under the ENTERPRISE platform is displayed as OpenClaw, and OpenClaw under the JVS platform is displayed as JVS Claw.
        self.agent_display_name = agent_display_name
        # The agent platform, such as ENTERPRISE_AGENTIC_COMPUTER.
        self.agent_platform = agent_platform
        # The agent provider, such as AgenticComputer.
        self.agent_provider = agent_provider
        # The number of expired runtime resources in the group. A runtime is counted as expired if its resource status is Expired or Ceased, case-insensitive.
        self.expired_count = expired_count
        # The number of runtime resources without channel configurations in the group, which is the total number of runtime resources minus the number of runtime resources with channel configurations.
        self.no_channel_configured_runtime_count = no_channel_configured_runtime_count
        # The number of runtime resources without model configurations in the group. A runtime is considered to have a model configured if a model is configured for the runtime itself or its associated resource group.
        self.no_model_configured_runtime_count = no_model_configured_runtime_count
        # The number of risky runtime resources in the group, deduplicated by runtime ID. A runtime is counted as risky if it has any of the following risks: model configuration modified, third-party channel configuration modified, or agent being uninstalled.
        self.risky_runtime_count = risky_runtime_count
        # The total number of runtime resources in the group, deduplicated by runtime ID.
        self.total_runtime_count = total_runtime_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_display_name is not None:
            result['AgentDisplayName'] = self.agent_display_name

        if self.agent_platform is not None:
            result['AgentPlatform'] = self.agent_platform

        if self.agent_provider is not None:
            result['AgentProvider'] = self.agent_provider

        if self.expired_count is not None:
            result['ExpiredCount'] = self.expired_count

        if self.no_channel_configured_runtime_count is not None:
            result['NoChannelConfiguredRuntimeCount'] = self.no_channel_configured_runtime_count

        if self.no_model_configured_runtime_count is not None:
            result['NoModelConfiguredRuntimeCount'] = self.no_model_configured_runtime_count

        if self.risky_runtime_count is not None:
            result['RiskyRuntimeCount'] = self.risky_runtime_count

        if self.total_runtime_count is not None:
            result['TotalRuntimeCount'] = self.total_runtime_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentDisplayName') is not None:
            self.agent_display_name = m.get('AgentDisplayName')

        if m.get('AgentPlatform') is not None:
            self.agent_platform = m.get('AgentPlatform')

        if m.get('AgentProvider') is not None:
            self.agent_provider = m.get('AgentProvider')

        if m.get('ExpiredCount') is not None:
            self.expired_count = m.get('ExpiredCount')

        if m.get('NoChannelConfiguredRuntimeCount') is not None:
            self.no_channel_configured_runtime_count = m.get('NoChannelConfiguredRuntimeCount')

        if m.get('NoModelConfiguredRuntimeCount') is not None:
            self.no_model_configured_runtime_count = m.get('NoModelConfiguredRuntimeCount')

        if m.get('RiskyRuntimeCount') is not None:
            self.risky_runtime_count = m.get('RiskyRuntimeCount')

        if m.get('TotalRuntimeCount') is not None:
            self.total_runtime_count = m.get('TotalRuntimeCount')

        return self

