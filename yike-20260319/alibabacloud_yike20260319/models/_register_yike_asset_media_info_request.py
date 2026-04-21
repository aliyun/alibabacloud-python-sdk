# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RegisterYikeAssetMediaInfoRequest(DaraModel):
    def __init__(
        self,
        folder_id: str = None,
        input_url: str = None,
        media_type: str = None,
        production_id: str = None,
    ):
        self.folder_id = folder_id
        # This parameter is required.
        self.input_url = input_url
        # This parameter is required.
        self.media_type = media_type
        self.production_id = production_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id

        if self.input_url is not None:
            result['InputURL'] = self.input_url

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        if self.production_id is not None:
            result['ProductionId'] = self.production_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')

        if m.get('InputURL') is not None:
            self.input_url = m.get('InputURL')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        if m.get('ProductionId') is not None:
            self.production_id = m.get('ProductionId')

        return self

