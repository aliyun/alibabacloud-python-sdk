# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunContractExtractShrinkRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        fields_to_extract_shrink: str = None,
        file_oss_url: str = None,
        region_id: str = None,
    ):
        self.app_id = app_id
        self.fields_to_extract_shrink = fields_to_extract_shrink
        # This parameter is required.
        self.file_oss_url = file_oss_url
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.fields_to_extract_shrink is not None:
            result['fieldsToExtract'] = self.fields_to_extract_shrink

        if self.file_oss_url is not None:
            result['fileOssUrl'] = self.file_oss_url

        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('fieldsToExtract') is not None:
            self.fields_to_extract_shrink = m.get('fieldsToExtract')

        if m.get('fileOssUrl') is not None:
            self.file_oss_url = m.get('fileOssUrl')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self

