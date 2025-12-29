# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteInstancesRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        instance_ids: str = None,
    ):
        # The ID of the application.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The ID of the instance to be deleted.
        # 
        # This parameter is required.
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        return self

