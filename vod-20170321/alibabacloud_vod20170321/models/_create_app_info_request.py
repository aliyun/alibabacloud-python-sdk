# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAppInfoRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        description: str = None,
        resource_group_id: str = None,
    ):
        # The name of the application. The application name must be unique.
        # 
        # *   The name can contain letters, digits, periods (.), hyphens (-), and at signs (@). The name can be up to 128 characters in length.
        # *   The value must be encoded in UTF-8.
        # 
        # This parameter is required.
        self.app_name = app_name
        # The description of the application.
        # 
        # *   The description can contain up to 512 characters in length.
        # *   The value must be encoded in UTF-8.
        self.description = description
        # The resource group ID.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.description is not None:
            result['Description'] = self.description

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

