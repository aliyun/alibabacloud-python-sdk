# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPromptTestResultRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        resource_type: str = None,
        service_code: str = None,
        text: str = None,
        type: str = None,
    ):
        self.config = config
        self.resource_type = resource_type
        self.service_code = service_code
        self.text = text
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.service_code is not None:
            result['ServiceCode'] = self.service_code

        if self.text is not None:
            result['Text'] = self.text

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

