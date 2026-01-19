# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAppSecurityResponseBody(DaraModel):
    def __init__(
        self,
        app_code: str = None,
        app_key: str = None,
        app_secret: str = None,
        created_time: str = None,
        modified_time: str = None,
        request_id: str = None,
    ):
        # The AppCode of the app.
        self.app_code = app_code
        # The key of the app.
        self.app_key = app_key
        # The password of the app.
        self.app_secret = app_secret
        # The creation time (UTC) of the key, which is the same as the app creation time.
        self.created_time = created_time
        # The modification time (UTC) of the key.
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
        if self.app_code is not None:
            result['AppCode'] = self.app_code

        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

