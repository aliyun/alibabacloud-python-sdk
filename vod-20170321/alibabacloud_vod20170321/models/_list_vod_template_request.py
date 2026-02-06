# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListVodTemplateRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        template_type: str = None,
    ):
        # The ID of the application. Set the value to **app-1000000**. For more information, see [Overview](https://help.aliyun.com/document_detail/113600.html).
        self.app_id = app_id
        # The type of the template. Set the value to **Snapshot**.
        # 
        # This parameter is required.
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        return self

