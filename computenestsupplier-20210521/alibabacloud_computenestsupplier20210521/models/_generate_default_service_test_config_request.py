# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateDefaultServiceTestConfigRequest(DaraModel):
    def __init__(
        self,
        service_id: str = None,
        service_version: str = None,
        template_name: str = None,
    ):
        # The service ID.
        # 
        # This parameter is required.
        self.service_id = service_id
        # The service version.
        # 
        # This parameter is required.
        self.service_version = service_version
        # The template name.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

