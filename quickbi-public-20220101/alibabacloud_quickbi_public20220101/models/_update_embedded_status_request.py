# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateEmbeddedStatusRequest(DaraModel):
    def __init__(
        self,
        third_part_auth_flag: bool = None,
        works_id: str = None,
    ):
        # Whether to enable the embedding feature for the work. Valid values:
        # 
        # *   true: enables embedding.
        # *   false: disables embedding.
        # 
        # This parameter is required.
        self.third_part_auth_flag = third_part_auth_flag
        # The ID of the work.
        # 
        # *   Batch modification is supported. Separate multiple values with commas (,).
        # 
        # This parameter is required.
        self.works_id = works_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.third_part_auth_flag is not None:
            result['ThirdPartAuthFlag'] = self.third_part_auth_flag

        if self.works_id is not None:
            result['WorksId'] = self.works_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ThirdPartAuthFlag') is not None:
            self.third_part_auth_flag = m.get('ThirdPartAuthFlag')

        if m.get('WorksId') is not None:
            self.works_id = m.get('WorksId')

        return self

