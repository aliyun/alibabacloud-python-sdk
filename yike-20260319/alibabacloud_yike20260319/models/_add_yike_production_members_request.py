# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddYikeProductionMembersRequest(DaraModel):
    def __init__(
        self,
        production_id: str = None,
        yike_user_ids: str = None,
    ):
        # The project ID.
        # 
        # This parameter is required.
        self.production_id = production_id
        # The IDs of the RAM users.
        # 
        # This parameter is required.
        self.yike_user_ids = yike_user_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.production_id is not None:
            result['ProductionId'] = self.production_id

        if self.yike_user_ids is not None:
            result['YikeUserIds'] = self.yike_user_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductionId') is not None:
            self.production_id = m.get('ProductionId')

        if m.get('YikeUserIds') is not None:
            self.yike_user_ids = m.get('YikeUserIds')

        return self

