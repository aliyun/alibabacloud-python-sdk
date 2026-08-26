# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDataAgentThemeUploadSignatureRequest(DaraModel):
    def __init__(
        self,
        theme_id: str = None,
    ):
        # The theme UUID. By default, you do not need to specify this parameter because the backend automatically generates and returns a UUID. Specify this parameter to regenerate a signature only when the previous signature has expired.
        self.theme_id = theme_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.theme_id is not None:
            result['ThemeId'] = self.theme_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ThemeId') is not None:
            self.theme_id = m.get('ThemeId')

        return self

