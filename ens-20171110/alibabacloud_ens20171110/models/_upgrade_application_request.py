# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpgradeApplicationRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        template: str = None,
        timeout: int = None,
    ):
        # The ID of the application.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The information template for phased update. The value must be a JSON string and contain the following information:
        # 
        # *   Version range that you want to update
        # *   Configuration information of the target version
        # *   Canary release policy for resources
        # *   Intelligent upgrade policy that contains information such as the time window and resource usage limit
        # 
        # This parameter is required.
        self.template = template
        # The timeout period for asynchronous upgrade. Unit: seconds. Default value: 300.
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

        if self.template is not None:
            result['Template'] = self.template

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        return self

