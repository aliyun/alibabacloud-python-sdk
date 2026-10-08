# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartK8sApplicationRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        replicas: int = None,
        timeout: int = None,
    ):
        # The ID of the application. You can call the ListApplication operation to obtain the application ID. For more information, see [ListApplication](https://help.aliyun.com/document_detail/149390.html).
        # 
        # This parameter is required.
        self.app_id = app_id
        # The number of application instances to start.
        self.replicas = replicas
        # The timeout period for the change process, in seconds. Valid values: 1 to 1800. Default value: 600.
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

        if self.replicas is not None:
            result['Replicas'] = self.replicas

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        return self

