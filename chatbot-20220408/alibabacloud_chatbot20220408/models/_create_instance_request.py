# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateInstanceRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        introduction: str = None,
        language_code: str = None,
        name: str = None,
        robot_type: str = None,
    ):
        # The workspace key. If this parameter is not specified, the default workspace is accessed. Obtain the key value from the business management page of the Alibaba Cloud account.
        self.agent_key = agent_key
        # The description of the chatbot. The description can be up to 50 characters in length.
        self.introduction = introduction
        # The language of the chatbot service, such as zh-cn or en-us. Default value: the default language of the workspace. Valid values: the languages supported by the workspace.
        self.language_code = language_code
        # The name of the chatbot. The name can be up to 50 characters in length.
        self.name = name
        # The type of the chatbot. Default value: scenario_im.
        self.robot_type = robot_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.introduction is not None:
            result['Introduction'] = self.introduction

        if self.language_code is not None:
            result['LanguageCode'] = self.language_code

        if self.name is not None:
            result['Name'] = self.name

        if self.robot_type is not None:
            result['RobotType'] = self.robot_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')

        if m.get('LanguageCode') is not None:
            self.language_code = m.get('LanguageCode')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RobotType') is not None:
            self.robot_type = m.get('RobotType')

        return self

