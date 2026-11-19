# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CancelCollectionRequest(DaraModel):
    def __init__(
        self,
        user_id: str = None,
        works_id: str = None,
    ):
        # The ID of the user who favorited the work. The user ID here refers to the Quick BI user ID, not the Alibaba Cloud UID.
        # 
        # This parameter is required.
        self.user_id = user_id
        # The ID of the work to remove from favorites.
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
        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.works_id is not None:
            result['WorksId'] = self.works_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('WorksId') is not None:
            self.works_id = m.get('WorksId')

        return self

