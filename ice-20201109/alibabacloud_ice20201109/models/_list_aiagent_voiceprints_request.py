# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAIAgentVoiceprintsRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        voiceprint_id: str = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Value values: [1,100].
        self.page_size = page_size
        # A unique identifier for the voiceprint. This parameter is optional. If provided, only the information for that ID is returned. If not specified, all voiceprints under the account are returned.
        self.voiceprint_id = voiceprint_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.voiceprint_id is not None:
            result['VoiceprintId'] = self.voiceprint_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('VoiceprintId') is not None:
            self.voiceprint_id = m.get('VoiceprintId')

        return self

