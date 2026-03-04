# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitYikeAIAppJobRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_params: str = None,
        folder_id: str = None,
        production_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.app_params = app_params
        self.folder_id = folder_id
        self.production_id = production_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_params is not None:
            result['AppParams'] = self.app_params

        if self.folder_id is not None:
            result['FolderId'] = self.folder_id

        if self.production_id is not None:
            result['ProductionId'] = self.production_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppParams') is not None:
            self.app_params = m.get('AppParams')

        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')

        if m.get('ProductionId') is not None:
            self.production_id = m.get('ProductionId')

        return self

