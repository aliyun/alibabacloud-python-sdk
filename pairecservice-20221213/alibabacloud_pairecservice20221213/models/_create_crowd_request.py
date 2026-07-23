# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCrowdRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        instance_id: str = None,
        label: str = None,
        name: str = None,
        source: str = None,
        users: str = None,
    ):
        # The description of the crowd.
        # 
        # This parameter is required.
        self.description = description
        # The instance ID. To get this ID, call the ListInstances operation.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The crowd label.
        self.label = label
        # The crowd name.
        # 
        # This parameter is required.
        self.name = name
        # The source of the user data. Valid values: ● ManualInput: Users are provided in the Users parameter. ● UploadFile: Users are provided from an uploaded file.
        self.source = source
        # The users to include in the crowd. Separate multiple users with commas (,).
        self.users = users

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.label is not None:
            result['Label'] = self.label

        if self.name is not None:
            result['Name'] = self.name

        if self.source is not None:
            result['Source'] = self.source

        if self.users is not None:
            result['Users'] = self.users

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Users') is not None:
            self.users = m.get('Users')

        return self

