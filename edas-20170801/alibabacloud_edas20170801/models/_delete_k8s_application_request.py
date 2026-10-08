# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteK8sApplicationRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        force: bool = None,
    ):
        # The ID of the application that you want to delete. You can call the ListApplication operation to query the application ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # Specifies whether to forcibly delete the application and disable application deletion protection.
        self.force = force

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.force is not None:
            result['Force'] = self.force

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Force') is not None:
            self.force = m.get('Force')

        return self

