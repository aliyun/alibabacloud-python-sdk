# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAppInfoRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        # The application ID. Set this parameter to the value of AppId returned by the [CreateApp](https://help.aliyun.com/document_detail/113266.html) or [ListApps](https://help.aliyun.com/document_detail/114000.html) operation.
        # 
        # This parameter is required.
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        return self

