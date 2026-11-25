# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddManifestEditTemplateRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        templates: str = None,
    ):
        # The name of the template. Spaces are allowed.
        # 
        # This parameter is required.
        self.name = name
        # The video encoding configuration, such as `{"Codec":"H.264","Bitrate":"5000000"}`.
        self.templates = templates

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.templates is not None:
            result['Templates'] = self.templates

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Templates') is not None:
            self.templates = m.get('Templates')

        return self

