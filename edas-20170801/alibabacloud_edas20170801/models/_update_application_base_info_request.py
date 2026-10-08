# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateApplicationBaseInfoRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        desc: str = None,
        owner: str = None,
    ):
        # The ID of the application.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The name of the application. The name must start with a letter, and can contain letters, digits, underscores (_), and hyphens (-). The name can be up to 36 characters in length.
        self.app_name = app_name
        # The description of the application. The description can be up to 256 characters in length.
        self.desc = desc
        # The owner of the application. The value can be up to 127 characters in length.
        self.owner = owner

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.desc is not None:
            result['Desc'] = self.desc

        if self.owner is not None:
            result['Owner'] = self.owner

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        return self

