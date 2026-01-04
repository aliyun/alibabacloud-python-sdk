# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateApplicationRequest(DaraModel):
    def __init__(
        self,
        template: str = None,
        timeout: int = None,
    ):
        # The edge application template. The value must be a JSON string that contains the following information:
        # 
        # *   Basic information such as the name of the application
        # *   Information such as resource specifications and network security configurations
        # *   Service specifications
        # *   Required resources
        # 
        # This parameter is required.
        self.template = template
        # The timeout period for asynchronous processing. Unit: seconds. Default value: 1800.
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.template is not None:
            result['Template'] = self.template

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        return self

