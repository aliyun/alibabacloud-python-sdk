# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteLogPathRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        path: str = None,
    ):
        # The ID of the application. You can call the ListApplication operation to query the application ID. For more information, see [ListApplication](https://help.aliyun.com/document_detail/149390.html).
        # 
        # This parameter is required.
        self.app_id = app_id
        # The absolute path of the log directory that you want to remove. The value must start and end with a forward slash (`/`) and must contain `/log` or `/logs`. The following directories are the default log directories in Enterprise Distributed Application Service (EDAS):
        # 
        # - /home/admin/edas-container/logs/
        # 
        # - /home/admin/taobao-tomcat-7.0.59/logs/
        # 
        # - /home/admin/taobao-tomcat-production-7.0.59.3/logs/
        # 
        # - /home/admin/taobao-tomcat-production-7.0.70/logs/
        # 
        # - /home/admin/edas-agent/logs/
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.path is not None:
            result['Path'] = self.path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        return self

