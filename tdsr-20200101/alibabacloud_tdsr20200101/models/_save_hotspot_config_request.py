# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveHotspotConfigRequest(DaraModel):
    def __init__(
        self,
        param_tag: str = None,
        preview_token: str = None,
    ):
        self.param_tag = param_tag
        self.preview_token = preview_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.param_tag is not None:
            result['ParamTag'] = self.param_tag

        if self.preview_token is not None:
            result['PreviewToken'] = self.preview_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamTag') is not None:
            self.param_tag = m.get('ParamTag')

        if m.get('PreviewToken') is not None:
            self.preview_token = m.get('PreviewToken')

        return self

