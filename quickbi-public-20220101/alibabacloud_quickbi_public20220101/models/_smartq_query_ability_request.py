# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SmartqQueryAbilityRequest(DaraModel):
    def __init__(
        self,
        cube_id: str = None,
        multiple_cube_ids: str = None,
        user_id: str = None,
        user_question: str = None,
    ):
        # Dataset ID.
        self.cube_id = cube_id
        self.multiple_cube_ids = multiple_cube_ids
        # User ID.
        # >Notice: If this field is not filled, the data will be queried by default as the organization owner.
        self.user_id = user_id
        # Question text.
        # 
        # This parameter is required.
        self.user_question = user_question

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id

        if self.multiple_cube_ids is not None:
            result['MultipleCubeIds'] = self.multiple_cube_ids

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_question is not None:
            result['UserQuestion'] = self.user_question

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')

        if m.get('MultipleCubeIds') is not None:
            self.multiple_cube_ids = m.get('MultipleCubeIds')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserQuestion') is not None:
            self.user_question = m.get('UserQuestion')

        return self

