# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAppInfoRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        description: str = None,
        status: str = None,
    ):
        # The ID of the application.
        # 
        # *   Default value: **app-1000000**.
        # *   For more information, see [Overview](https://help.aliyun.com/document_detail/113600.html).
        # 
        # This parameter is required.
        self.app_id = app_id
        # The name of the application.
        # 
        # *   The name can contain up to 128 characters in length, including Chinese letters, digits, and periods (.), dash (-), and at character (@).
        # *   The name can contain only UTF-8 characters.
        self.app_name = app_name
        # The description of the application.
        # 
        # *   The description can contain up to 512 characters in length.
        # *   The description can contain only UTF-8 characters.
        self.description = description
        # The status of the application. Valid values:
        # 
        # *   **Normal**
        # *   **Disable**
        self.status = status

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

        if self.description is not None:
            result['Description'] = self.description

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

