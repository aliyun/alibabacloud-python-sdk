# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSubCrowdRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        source: str = None,
        users: str = None,
    ):
        # The instance ID. You can obtain the instance ID by calling the ListInstances API.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The source of users for the sub-crowd. Valid values: ● ManualInput: manual input ● UploadFile: file upload
        # 
        # This parameter is required.
        self.source = source
        # A comma-separated list of users in the sub-crowd.
        # 
        # This parameter is required.
        self.users = users

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.source is not None:
            result['Source'] = self.source

        if self.users is not None:
            result['Users'] = self.users

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Users') is not None:
            self.users = m.get('Users')

        return self

