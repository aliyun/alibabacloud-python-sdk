# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadMaterialFileForAdminRequest(DaraModel):
    def __init__(
        self,
        belong_id: str = None,
        biz_id: str = None,
        file_url: str = None,
        name: str = None,
    ):
        # The ID of the owner.
        self.belong_id = belong_id
        # The business instance ID.
        # 
        # This parameter is required.
        self.biz_id = biz_id
        # The file URL.
        # 
        # This parameter is required.
        self.file_url = file_url
        # The file name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.belong_id is not None:
            result['BelongId'] = self.belong_id

        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BelongId') is not None:
            self.belong_id = m.get('BelongId')

        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

