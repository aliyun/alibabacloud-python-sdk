# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MultiModalGuardForBase64Request(DaraModel):
    def __init__(
        self,
        image_base_64str: str = None,
        service: str = None,
        service_parameters: str = None,
    ):
        self.image_base_64str = image_base_64str
        # Service
        self.service = service
        self.service_parameters = service_parameters

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_base_64str is not None:
            result['ImageBase64Str'] = self.image_base_64str

        if self.service is not None:
            result['Service'] = self.service

        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageBase64Str') is not None:
            self.image_base_64str = m.get('ImageBase64Str')

        if m.get('Service') is not None:
            self.service = m.get('Service')

        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')

        return self

