# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetScenePreviewResourceRequest(DaraModel):
    def __init__(
        self,
        draft: bool = None,
        preview_token: str = None,
    ):
        self.draft = draft
        # This parameter is required.
        self.preview_token = preview_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.draft is not None:
            result['Draft'] = self.draft

        if self.preview_token is not None:
            result['PreviewToken'] = self.preview_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Draft') is not None:
            self.draft = m.get('Draft')

        if m.get('PreviewToken') is not None:
            self.preview_token = m.get('PreviewToken')

        return self

