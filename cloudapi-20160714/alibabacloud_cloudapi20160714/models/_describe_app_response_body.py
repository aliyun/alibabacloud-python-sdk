# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAppResponseBody(DaraModel):
    def __init__(
        self,
        app_id: int = None,
        app_name: str = None,
        created_time: str = None,
        description: str = None,
        disabled: bool = None,
        extend: str = None,
        modified_time: str = None,
        request_id: str = None,
    ):
        # The ID of the app.
        self.app_id = app_id
        # The name of the app.
        self.app_name = app_name
        # The time when the app was created.
        self.created_time = created_time
        # The description of the app.
        self.description = description
        self.disabled = disabled
        # 扩展信息
        self.extend = extend
        # The time when the app was modified.
        self.modified_time = modified_time
        # The ID of the request.
        self.request_id = request_id

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

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.description is not None:
            result['Description'] = self.description

        if self.disabled is not None:
            result['Disabled'] = self.disabled

        if self.extend is not None:
            result['Extend'] = self.extend

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')

        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

