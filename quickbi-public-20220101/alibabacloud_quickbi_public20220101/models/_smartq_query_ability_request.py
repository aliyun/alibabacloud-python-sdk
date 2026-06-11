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
        # The ID of the dataset. To obtain the ID, navigate to \\*\\*Workbench\\*\\* > \\*\\*Dataset\\*\\* in the Quick BI console. Open the dataset and find the \\`cubeId\\` in the URL.
        # 
        # In multi-table scenarios, this parameter must be empty.
        self.cube_id = cube_id
        # A list of dataset IDs. The model selects one or more tables from the list to generate an answer based on the question. This parameter is required for multi-table scenarios and is not used for single-table scenarios.
        self.multiple_cube_ids = multiple_cube_ids
        # The ID of the user.
        # >Notice: If you do not specify this parameter, data is queried as the organization owner by default.
        self.user_id = user_id
        # The question in text format.
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

