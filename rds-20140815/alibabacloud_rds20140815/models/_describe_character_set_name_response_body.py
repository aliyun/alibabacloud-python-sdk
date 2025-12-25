# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeCharacterSetNameResponseBody(DaraModel):
    def __init__(
        self,
        character_set_name_items: main_models.DescribeCharacterSetNameResponseBodyCharacterSetNameItems = None,
        engine: str = None,
        request_id: str = None,
    ):
        # The character sets that are supported.
        self.character_set_name_items = character_set_name_items
        # The type of the database engine.
        self.engine = engine
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.character_set_name_items:
            self.character_set_name_items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.character_set_name_items is not None:
            result['CharacterSetNameItems'] = self.character_set_name_items.to_map()

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CharacterSetNameItems') is not None:
            temp_model = main_models.DescribeCharacterSetNameResponseBodyCharacterSetNameItems()
            self.character_set_name_items = temp_model.from_map(m.get('CharacterSetNameItems'))

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCharacterSetNameResponseBodyCharacterSetNameItems(DaraModel):
    def __init__(
        self,
        character_set_name: List[str] = None,
    ):
        self.character_set_name = character_set_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.character_set_name is not None:
            result['CharacterSetName'] = self.character_set_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CharacterSetName') is not None:
            self.character_set_name = m.get('CharacterSetName')

        return self

