# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class BatchConfigRuntimeChannelRequest(DaraModel):
    def __init__(
        self,
        agent_platform: str = None,
        agent_provider: str = None,
        channel_configs: List[main_models.BatchConfigRuntimeChannelRequestChannelConfigs] = None,
        runtime_type: str = None,
    ):
        # The agent platform, such as ENTERPRISE. If the value is invalid, the error code InvalidParameter.AgentPlatform is returned.
        # 
        # This parameter is required.
        self.agent_platform = agent_platform
        # The agent provider.
        # 
        # - JVS Computer: Enter OpenClaw.
        # - OpenClaw: Enter OpenClaw.
        # - Hermes Agent: Enter HermesAgent.
        # 
        # This parameter is required.
        self.agent_provider = agent_provider
        # The list of channel configurations. A maximum of 200 configurations are supported. Each configuration item specifies an agent runtime and the third-party channel to be configured for it. Different channel configurations can be delivered to different runtimes. Multiple configuration items for the same runtime are processed sequentially.
        # 
        # This parameter is required.
        self.channel_configs = channel_configs
        # The agent runtime type, such as CloudDesktop (cloud desktop).
        # 
        # This parameter is required.
        self.runtime_type = runtime_type

    def validate(self):
        if self.channel_configs:
            for v1 in self.channel_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_platform is not None:
            result['AgentPlatform'] = self.agent_platform

        if self.agent_provider is not None:
            result['AgentProvider'] = self.agent_provider

        result['ChannelConfigs'] = []
        if self.channel_configs is not None:
            for k1 in self.channel_configs:
                result['ChannelConfigs'].append(k1.to_map() if k1 else None)

        if self.runtime_type is not None:
            result['RuntimeType'] = self.runtime_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentPlatform') is not None:
            self.agent_platform = m.get('AgentPlatform')

        if m.get('AgentProvider') is not None:
            self.agent_provider = m.get('AgentProvider')

        self.channel_configs = []
        if m.get('ChannelConfigs') is not None:
            for k1 in m.get('ChannelConfigs'):
                temp_model = main_models.BatchConfigRuntimeChannelRequestChannelConfigs()
                self.channel_configs.append(temp_model.from_map(k1))

        if m.get('RuntimeType') is not None:
            self.runtime_type = m.get('RuntimeType')

        return self

class BatchConfigRuntimeChannelRequestChannelConfigs(DaraModel):
    def __init__(
        self,
        code: str = None,
        config: str = None,
        config_mode: str = None,
        name: str = None,
        runtime_id: str = None,
    ):
        # The third-party channel code, such as dingtalk-connector (DingTalk), feishu (Lark), and wecom (WeCom). System channel codes are not case-sensitive. Configuring wechat and jvsclaw is not supported. If these values are passed, the entire request fails and the error code ChannelConfig.NotSupported is returned.
        # 
        # This parameter is required.
        self.code = code
        # The JSON string for the channel configuration.
        # 
        # - Simple mode: only appKey and appSecret are allowed.
        # - Custom mode: all configuration items required for the channel under the current agent provider must be included.
        # 
        # If the string is not valid JSON, the error code InvalidParameter.ValueInvalid is returned.
        # 
        # This parameter is required.
        self.config = config
        # The configuration mode. Valid values:
        # 
        # - Simple: the simple configuration mode.
        # - Custom: the custom configuration mode.
        # 
        # This parameter is required.
        self.config_mode = config_mode
        # The channel name.
        # 
        # If this parameter is not specified, the system automatically uses the code as the name.
        self.name = name
        # The agent runtime ID. The ID mappings are as follows:
        # 
        # - JVS Computer: the JVS Computer ID, in the format of jvs-xxxx.
        # - OpenClaw: the cloud desktop ID, in the format of ecd-xxxx.
        # - Hermes Agent: the Hermes Agent ID, in the format of jvs-xxxx.
        # 
        # This parameter is required.
        self.runtime_id = runtime_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.config is not None:
            result['Config'] = self.config

        if self.config_mode is not None:
            result['ConfigMode'] = self.config_mode

        if self.name is not None:
            result['Name'] = self.name

        if self.runtime_id is not None:
            result['RuntimeId'] = self.runtime_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('ConfigMode') is not None:
            self.config_mode = m.get('ConfigMode')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RuntimeId') is not None:
            self.runtime_id = m.get('RuntimeId')

        return self

