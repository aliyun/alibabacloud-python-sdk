# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetUploadInfoRequest(DaraModel):
    def __init__(
        self,
        biz_region_id: str = None,
        file_type: str = None,
    ):
        # The ID of the business region where the file is uploaded. If this parameter is not specified, the default OSS region configured for the service is used.
        self.biz_region_id = biz_region_id
        # The type of the file to upload. Currently, only TASK is supported, which indicates an image task file.
        self.file_type = file_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.file_type is not None:
            result['FileType'] = self.file_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        return self

