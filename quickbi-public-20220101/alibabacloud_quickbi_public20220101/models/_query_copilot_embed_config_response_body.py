# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class QueryCopilotEmbedConfigResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.QueryCopilotEmbedConfigResponseBodyResult] = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # List of embedded configurations.
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # 
        # - true: The request was successful.
        # - false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.QueryCopilotEmbedConfigResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryCopilotEmbedConfigResponseBodyResult(DaraModel):
    def __init__(
        self,
        agent_name: str = None,
        copilot_id: str = None,
        create_user: str = None,
        create_user_name: str = None,
        data_range: main_models.QueryCopilotEmbedConfigResponseBodyResultDataRange = None,
        modify_user: str = None,
        module_name: str = None,
        show_name: str = None,
    ):
        # Robot\\"s nickname.
        self.agent_name = agent_name
        # Embedding ID.
        self.copilot_id = copilot_id
        # ID of the creator.
        self.create_user = create_user
        # Nickname of the creator.
        self.create_user_name = create_user_name
        # Data range (analysis themes and question resources).
        self.data_range = data_range
        # ID of the modifier.
        self.modify_user = modify_user
        # Module name.
        self.module_name = module_name
        # Name of the embedded module.
        self.show_name = show_name

    def validate(self):
        if self.data_range:
            self.data_range.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.copilot_id is not None:
            result['CopilotId'] = self.copilot_id

        if self.create_user is not None:
            result['CreateUser'] = self.create_user

        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name

        if self.data_range is not None:
            result['DataRange'] = self.data_range.to_map()

        if self.modify_user is not None:
            result['ModifyUser'] = self.modify_user

        if self.module_name is not None:
            result['ModuleName'] = self.module_name

        if self.show_name is not None:
            result['ShowName'] = self.show_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('CopilotId') is not None:
            self.copilot_id = m.get('CopilotId')

        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')

        if m.get('DataRange') is not None:
            temp_model = main_models.QueryCopilotEmbedConfigResponseBodyResultDataRange()
            self.data_range = temp_model.from_map(m.get('DataRange'))

        if m.get('ModifyUser') is not None:
            self.modify_user = m.get('ModifyUser')

        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')

        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')

        return self

class QueryCopilotEmbedConfigResponseBodyResultDataRange(DaraModel):
    def __init__(
        self,
        all_cube: bool = None,
        all_theme: bool = None,
        llm_cubes: List[str] = None,
        themes: List[str] = None,
    ):
        # Whether all question resources are selected.
        self.all_cube = all_cube
        # Whether all analysis themes are selected.
        self.all_theme = all_theme
        # Collection of question resource IDs.
        self.llm_cubes = llm_cubes
        # Collection of analysis theme IDs.
        self.themes = themes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all_cube is not None:
            result['AllCube'] = self.all_cube

        if self.all_theme is not None:
            result['AllTheme'] = self.all_theme

        if self.llm_cubes is not None:
            result['LlmCubes'] = self.llm_cubes

        if self.themes is not None:
            result['Themes'] = self.themes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllCube') is not None:
            self.all_cube = m.get('AllCube')

        if m.get('AllTheme') is not None:
            self.all_theme = m.get('AllTheme')

        if m.get('LlmCubes') is not None:
            self.llm_cubes = m.get('LlmCubes')

        if m.get('Themes') is not None:
            self.themes = m.get('Themes')

        return self

