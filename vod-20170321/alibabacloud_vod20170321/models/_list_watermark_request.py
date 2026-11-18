# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListWatermarkRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        # The application ID. Default value: **app-1000000**.
        # 
        # If the multi-application system is enabled, you can specify an application ID to query the image and text watermark templates of a specific application. If you do not specify this parameter, the system returns the image and text watermark templates of all applications by default. For more information, see [Multi-application](https://help.aliyun.com/document_detail/113600.html).
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

