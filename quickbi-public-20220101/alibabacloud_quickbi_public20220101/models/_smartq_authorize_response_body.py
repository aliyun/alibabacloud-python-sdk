# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class SmartqAuthorizeResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.SmartqAuthorizeResponseBodyResult] = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Array of failed user information.
        self.result = result
        # Indicates whether the request was successful. The value range is as follows:
        # 
        # - true: Request succeeded
        # - false: Request failed
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
                temp_model = main_models.SmartqAuthorizeResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class SmartqAuthorizeResponseBodyResult(DaraModel):
    def __init__(
        self,
        detail_message: str = None,
        llm_cube: str = None,
        llm_cube_theme: str = None,
        user_id: str = None,
    ):
        # Reason for failure.
        self.detail_message = detail_message
        # Q&A resource ID.
        self.llm_cube = llm_cube
        # Analysis theme ID.
        self.llm_cube_theme = llm_cube_theme
        # User ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detail_message is not None:
            result['DetailMessage'] = self.detail_message

        if self.llm_cube is not None:
            result['LlmCube'] = self.llm_cube

        if self.llm_cube_theme is not None:
            result['LlmCubeTheme'] = self.llm_cube_theme

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetailMessage') is not None:
            self.detail_message = m.get('DetailMessage')

        if m.get('LlmCube') is not None:
            self.llm_cube = m.get('LlmCube')

        if m.get('LlmCubeTheme') is not None:
            self.llm_cube_theme = m.get('LlmCubeTheme')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

