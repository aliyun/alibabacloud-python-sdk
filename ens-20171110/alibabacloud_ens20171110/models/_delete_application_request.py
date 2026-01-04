# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteApplicationRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        timeout: int = None,
    ):
        # The ID of the application. To obtain the application ID, call the ListApplication operation.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The timeout period for the asynchronous release. Unit: seconds. Default value: 300.
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        return self

