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
        # An array of dataset IDs. Separate multiple IDs with commas.
        # >Notice: This parameter is converted to the corresponding Q\\&A resource ID for authorization. If a \\`cubeId\\` does not correspond to an existing Q\\&A resource, an error is reported that the Q\\&A resource does not exist. Ensure that the \\`cubeId\\` is correct.
        self.cube_ids = cube_ids
        # The expiration time. The default is seven days.
        # Format: 2099-12-31
        self.expire_day = expire_day
        # An array of analysis subject IDs. Separate multiple IDs with commas.
        self.llm_cube_themes = llm_cube_themes
        # An array of Q\\&A resource IDs. Separate multiple IDs with commas.
        self.llm_cubes = llm_cubes
        # The operation type. Valid values:
        # 
        # - 0: Grant authorization
        # 
        # - 1: Delete authorization
        # 
        # This parameter is required.
        self.operation_type = operation_type
        # An array of user IDs. Separate multiple IDs with commas.
        # >Notice: The number of user IDs × (the number of Q\\&A resources + the number of analysis subjects) in a single request cannot exceed 100.
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

