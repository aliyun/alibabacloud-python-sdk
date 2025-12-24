# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class AddCasterEpisodeGroupResponseBody(DaraModel):
    def __init__(
        self,
        item_ids: main_models.AddCasterEpisodeGroupResponseBodyItemIds = None,
        program_id: str = None,
        request_id: str = None,
    ):
        # The IDs of the episodes.
        self.item_ids = item_ids
        # The ID of the episode list that was added. Record the ID as it can be used to manage the program being added.
        self.program_id = program_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.item_ids:
            self.item_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.item_ids is not None:
            result['ItemIds'] = self.item_ids.to_map()

        if self.program_id is not None:
            result['ProgramId'] = self.program_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemIds') is not None:
            temp_model = main_models.AddCasterEpisodeGroupResponseBodyItemIds()
            self.item_ids = temp_model.from_map(m.get('ItemIds'))

        if m.get('ProgramId') is not None:
            self.program_id = m.get('ProgramId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class AddCasterEpisodeGroupResponseBodyItemIds(DaraModel):
    def __init__(
        self,
        item_id: List[str] = None,
    ):
        self.item_id = item_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.item_id is not None:
            result['ItemId'] = self.item_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')

        return self

