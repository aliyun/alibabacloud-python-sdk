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
        # The application ID. This is the value of the AppId parameter returned by the [CreateApp](https://help.aliyun.com/document_detail/113266.html) or [GetAppInfos](https://help.aliyun.com/document_detail/114000.html) operation.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The new application name.
        # - The name can be up to 128 characters in length and can contain Chinese characters, letters, digits, periods (.), hyphens (-), and at signs (@).
        # - UTF-8 encoding.
        self.app_name = app_name
        # The new application description.
        # - The description can be up to 512 characters in length.
        # - UTF-8 encoding.
        self.description = description
        # The new application status. Valid values:
        # - **Normal**: Normal.
        # - **Disable**: Disabled.
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

