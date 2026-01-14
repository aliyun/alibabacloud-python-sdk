# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class QueryDataRangeResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.QueryDataRangeResponseBodyResult = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Data range object.
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # - true: The request was successful.
        # - false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.QueryDataRangeResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryDataRangeResponseBodyResult(DaraModel):
    def __init__(
        self,
        api_copilot_llm_cube_models: List[main_models.QueryDataRangeResponseBodyResultApiCopilotLlmCubeModels] = None,
        api_copilot_theme_models: List[main_models.QueryDataRangeResponseBodyResultApiCopilotThemeModels] = None,
    ):
        # Array of LlmCube resources.
        self.api_copilot_llm_cube_models = api_copilot_llm_cube_models
        # Array of analysis themes.
        self.api_copilot_theme_models = api_copilot_theme_models

    def validate(self):
        if self.api_copilot_llm_cube_models:
            for v1 in self.api_copilot_llm_cube_models:
                 if v1:
                    v1.validate()
        if self.api_copilot_theme_models:
            for v1 in self.api_copilot_theme_models:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApiCopilotLlmCubeModels'] = []
        if self.api_copilot_llm_cube_models is not None:
            for k1 in self.api_copilot_llm_cube_models:
                result['ApiCopilotLlmCubeModels'].append(k1.to_map() if k1 else None)

        result['ApiCopilotThemeModels'] = []
        if self.api_copilot_theme_models is not None:
            for k1 in self.api_copilot_theme_models:
                result['ApiCopilotThemeModels'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_copilot_llm_cube_models = []
        if m.get('ApiCopilotLlmCubeModels') is not None:
            for k1 in m.get('ApiCopilotLlmCubeModels'):
                temp_model = main_models.QueryDataRangeResponseBodyResultApiCopilotLlmCubeModels()
                self.api_copilot_llm_cube_models.append(temp_model.from_map(k1))

        self.api_copilot_theme_models = []
        if m.get('ApiCopilotThemeModels') is not None:
            for k1 in m.get('ApiCopilotThemeModels'):
                temp_model = main_models.QueryDataRangeResponseBodyResultApiCopilotThemeModels()
                self.api_copilot_theme_models.append(temp_model.from_map(k1))

        return self

class QueryDataRangeResponseBodyResultApiCopilotThemeModels(DaraModel):
    def __init__(
        self,
        api_copilot_llm_cube_models: List[main_models.QueryDataRangeResponseBodyResultApiCopilotThemeModelsApiCopilotLlmCubeModels] = None,
        create_user: str = None,
        theme_id: str = None,
        theme_name: str = None,
    ):
        # Array of LlmCube resources.
        self.api_copilot_llm_cube_models = api_copilot_llm_cube_models
        # Nickname of the creator.
        self.create_user = create_user
        # Analysis theme ID.
        self.theme_id = theme_id
        # Nickname of the analysis theme.
        self.theme_name = theme_name

    def validate(self):
        if self.api_copilot_llm_cube_models:
            for v1 in self.api_copilot_llm_cube_models:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApiCopilotLlmCubeModels'] = []
        if self.api_copilot_llm_cube_models is not None:
            for k1 in self.api_copilot_llm_cube_models:
                result['ApiCopilotLlmCubeModels'].append(k1.to_map() if k1 else None)

        if self.create_user is not None:
            result['CreateUser'] = self.create_user

        if self.theme_id is not None:
            result['ThemeId'] = self.theme_id

        if self.theme_name is not None:
            result['ThemeName'] = self.theme_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_copilot_llm_cube_models = []
        if m.get('ApiCopilotLlmCubeModels') is not None:
            for k1 in m.get('ApiCopilotLlmCubeModels'):
                temp_model = main_models.QueryDataRangeResponseBodyResultApiCopilotThemeModelsApiCopilotLlmCubeModels()
                self.api_copilot_llm_cube_models.append(temp_model.from_map(k1))

        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        if m.get('ThemeId') is not None:
            self.theme_id = m.get('ThemeId')

        if m.get('ThemeName') is not None:
            self.theme_name = m.get('ThemeName')

        return self

class QueryDataRangeResponseBodyResultApiCopilotThemeModelsApiCopilotLlmCubeModels(DaraModel):
    def __init__(
        self,
        alias: str = None,
        create_user: str = None,
        llm_cube_id: str = None,
    ):
        # Alias of the LLM cube resource.
        self.alias = alias
        # Nickname of the creator.
        self.create_user = create_user
        # LlmCube resource ID.
        self.llm_cube_id = llm_cube_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['Alias'] = self.alias

        if self.create_user is not None:
            result['CreateUser'] = self.create_user

        if self.llm_cube_id is not None:
            result['LlmCubeId'] = self.llm_cube_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        if m.get('LlmCubeId') is not None:
            self.llm_cube_id = m.get('LlmCubeId')

        return self

class QueryDataRangeResponseBodyResultApiCopilotLlmCubeModels(DaraModel):
    def __init__(
        self,
        alias: str = None,
        create_user: str = None,
        llm_cube_id: str = None,
    ):
        # Alias of the LlmCube resource.
        self.alias = alias
        # Nickname of the creator.
        self.create_user = create_user
        # LlmCube resource ID.
        self.llm_cube_id = llm_cube_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['Alias'] = self.alias

        if self.create_user is not None:
            result['CreateUser'] = self.create_user

        if self.llm_cube_id is not None:
            result['LlmCubeId'] = self.llm_cube_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        if m.get('LlmCubeId') is not None:
            self.llm_cube_id = m.get('LlmCubeId')

        return self

