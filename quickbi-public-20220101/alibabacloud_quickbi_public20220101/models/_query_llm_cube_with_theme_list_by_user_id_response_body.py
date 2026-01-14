# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class QueryLlmCubeWithThemeListByUserIdResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.QueryLlmCubeWithThemeListByUserIdResponseBodyResult = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # List of datasets and analysis themes.
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # 
        # - true: The request was successful
        # - false: The request failed
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
            temp_model = main_models.QueryLlmCubeWithThemeListByUserIdResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryLlmCubeWithThemeListByUserIdResponseBodyResult(DaraModel):
    def __init__(
        self,
        cube_ids: Dict[str, str] = None,
        theme_ids: Dict[str, str] = None,
    ):
        # Dataset map.
        # 
        # - key - Dataset ID
        # - value - Dataset name
        self.cube_ids = cube_ids
        # Analysis theme map.
        # - key - Analysis theme ID 
        # - value - Analysis theme name
        self.theme_ids = theme_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cube_ids is not None:
            result['CubeIds'] = self.cube_ids

        if self.theme_ids is not None:
            result['ThemeIds'] = self.theme_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CubeIds') is not None:
            self.cube_ids = m.get('CubeIds')

        if m.get('ThemeIds') is not None:
            self.theme_ids = m.get('ThemeIds')

        return self

