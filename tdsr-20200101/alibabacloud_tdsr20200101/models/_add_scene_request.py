# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddSceneRequest(DaraModel):
    def __init__(
        self,
        customer_uid: str = None,
        name: str = None,
        project_id: str = None,
        type: str = None,
    ):
        self.customer_uid = customer_uid
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.project_id = project_id
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.customer_uid is not None:
            result['CustomerUid'] = self.customer_uid

        if self.name is not None:
            result['Name'] = self.name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerUid') is not None:
            self.customer_uid = m.get('CustomerUid')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

