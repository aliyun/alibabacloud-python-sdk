# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateLiveMessageAppResponseBody(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_key: str = None,
        app_sign: str = None,
        data_center: str = None,
        request_id: str = None,
    ):
        # The application ID. The ID is used in subsequent operations, such as joining a group.
        self.app_id = app_id
        # The AppKey for authentication of this application.
        self.app_key = app_key
        # The application signature. The signature is required when you use the interactive messaging SDK.
        self.app_sign = app_sign
        # The data center in which the interactive messaging application was created.
        self.data_center = data_center
        # The request ID.
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

        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.app_sign is not None:
            result['AppSign'] = self.app_sign

        if self.data_center is not None:
            result['DataCenter'] = self.data_center

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('AppSign') is not None:
            self.app_sign = m.get('AppSign')

        if m.get('DataCenter') is not None:
            self.data_center = m.get('DataCenter')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

