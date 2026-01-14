# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SmartqAuthorizeRequest(DaraModel):
    def __init__(
        self,
        cube_ids: str = None,
        expire_day: str = None,
        llm_cube_themes: str = None,
        llm_cubes: str = None,
        operation_type: int = None,
        user_ids: str = None,
    ):
        # Array of dataset IDs, separated by English commas. <notice>This parameter will be converted to the corresponding question resource ID for authorization. Therefore, if the input cubeId does not correspond to any question resource, an error indicating that the question resource does not exist will be reported. Please ensure the correctness of the cubeId.</notice>
        self.cube_ids = cube_ids
        # Expiration time, with a default of seven days.
        # Format: 2099-12-31
        self.expire_day = expire_day
        # Array of analysis theme IDs, separated by English commas.
        self.llm_cube_themes = llm_cube_themes
        # Array of Q&A resource IDs, separated by English commas.
        self.llm_cubes = llm_cubes
        # Operation type. The values are as follows:
        # - 0: Add authorization
        # - 1: Remove authorization
        # 
        # This parameter is required.
        self.operation_type = operation_type
        # Array of user IDs, separated by English commas.
        # >Notice: The number of user IDs per request * (number of Q&A resources + number of analysis themes) cannot exceed 100.
        # 
        # This parameter is required.
        self.user_ids = user_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cube_ids is not None:
            result['CubeIds'] = self.cube_ids

        if self.expire_day is not None:
            result['ExpireDay'] = self.expire_day

        if self.llm_cube_themes is not None:
            result['LlmCubeThemes'] = self.llm_cube_themes

        if self.llm_cubes is not None:
            result['LlmCubes'] = self.llm_cubes

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.user_ids is not None:
            result['UserIds'] = self.user_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CubeIds') is not None:
            self.cube_ids = m.get('CubeIds')

        if m.get('ExpireDay') is not None:
            self.expire_day = m.get('ExpireDay')

        if m.get('LlmCubeThemes') is not None:
            self.llm_cube_themes = m.get('LlmCubeThemes')

        if m.get('LlmCubes') is not None:
            self.llm_cubes = m.get('LlmCubes')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')

        return self

