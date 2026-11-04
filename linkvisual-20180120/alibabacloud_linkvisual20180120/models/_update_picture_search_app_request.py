# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdatePictureSearchAppRequest(DaraModel):
    def __init__(
        self,
        app_instance_id: str = None,
        description: str = None,
        name: str = None,
    ):
        # Instance ID of the image search application instance. You can call the [QueryPictureSearchApps](206608) operation to query instance ID.
        # 
        # This parameter is required.
        self.app_instance_id = app_instance_id
        # The description of the image search application instance.
        # 
        # The description can contain Chinese characters, uppercase and lowercase letters, digits, underscores (_), and hyphens (-). It can be up to 1,024 characters in length, and each Chinese character counts as two characters.
        # 
        # This parameter is required.
        self.description = description
        # The name of the image search application instance. 
        # 
        # The name can contain Chinese characters, uppercase and lowercase letters, digits, underscores (_), and hyphens (-). It can be up to 64 characters in length, and each Chinese character counts as two characters.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

