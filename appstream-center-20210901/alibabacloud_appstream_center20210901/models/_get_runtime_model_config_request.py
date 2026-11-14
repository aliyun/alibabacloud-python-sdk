# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRuntimeModelConfigRequest(DaraModel):
    def __init__(
        self,
        agent_platform: str = None,
        agent_provider: str = None,
        include_risk_info: bool = None,
        language: str = None,
        runtime_id: str = None,
        runtime_type: str = None,
        smart_model: bool = None,
    ):
        # The agent platform.
        self.agent_platform = agent_platform
        # The agent provider.
        # 
        # This parameter is required.
        self.agent_provider = agent_provider
        # Specifies whether to include risk information.
        self.include_risk_info = include_risk_info
        # The model display language. Valid values: zh-CN, en-US, ja-JP, and zh-TW. The value is case-insensitive, and leading and trailing spaces are removed. If this parameter is not specified, left empty, or set to an unsupported value, the default value zh-CN is used. The model pool description mapping is returned based on the normalized interface language, and falls back to Chinese if a translation is missing. Bailian and existing dynamic configurations still use Chinese for zh-CN and zh-TW, and English for en-US and ja-JP. This parameter is used for the names and descriptions of system intelligence tiers, as well as general model descriptions. Template fallback text, custom names, and runtime configurations retain their original values. The values zh_CN, en_US, ja_JP, and zh_TW are also supported, and en and ja are compatible. The value is case-insensitive, and leading and trailing spaces are removed. An invalid language value falls back to Chinese and does not cause a parameter error to be returned for Language. The names and descriptions of the four system intelligence tiers (Auto, Standard, Advanced, and Ultimate) support all four languages, and Chinese is retained for missing Japanese and Traditional Chinese items. User template names retain their original values.
        self.language = language
        # The agent runtime ID. The ID mappings are as follows:
        # 
        # JVS Computer: JVS Computer ID, in the format of jvs-xxxx.
        # 
        # OpenClaw: Cloud desktop ID, in the format of ecd-xxxx.
        # 
        # Hermes Agent: Hermes Agent ID, in the format of jvs-xxxx.
        # 
        # This parameter is required.
        self.runtime_id = runtime_id
        # The agent runtime type.
        # 
        # This parameter is required.
        self.runtime_type = runtime_type
        # The smart model filter. Valid values:
        # - true: Queries the system wuying-preset provider models based on the business type of the runtime.
        # - false: Excludes wuying-preset from the effective configuration.
        # - Not specified: Returns both smart and non-smart models in the effective configuration.
        # The business type is read by the server from runtime.biz_type, and the BizType input parameter is not required. Risk information is still independently controlled by IncludeRiskInfo.
        self.smart_model = smart_model

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_platform is not None:
            result['AgentPlatform'] = self.agent_platform

        if self.agent_provider is not None:
            result['AgentProvider'] = self.agent_provider

        if self.include_risk_info is not None:
            result['IncludeRiskInfo'] = self.include_risk_info

        if self.language is not None:
            result['Language'] = self.language

        if self.runtime_id is not None:
            result['RuntimeId'] = self.runtime_id

        if self.runtime_type is not None:
            result['RuntimeType'] = self.runtime_type

        if self.smart_model is not None:
            result['SmartModel'] = self.smart_model

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentPlatform') is not None:
            self.agent_platform = m.get('AgentPlatform')

        if m.get('AgentProvider') is not None:
            self.agent_provider = m.get('AgentProvider')

        if m.get('IncludeRiskInfo') is not None:
            self.include_risk_info = m.get('IncludeRiskInfo')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('RuntimeId') is not None:
            self.runtime_id = m.get('RuntimeId')

        if m.get('RuntimeType') is not None:
            self.runtime_type = m.get('RuntimeType')

        if m.get('SmartModel') is not None:
            self.smart_model = m.get('SmartModel')

        return self

