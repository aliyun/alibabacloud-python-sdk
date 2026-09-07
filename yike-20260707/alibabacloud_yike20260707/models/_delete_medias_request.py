# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteMediasRequest(DaraModel):
    def __init__(
        self,
        biz_config: str = None,
        delete_physical_files: bool = None,
        input_urls: str = None,
        media_ids: str = None,
    ):
        self.biz_config = biz_config
        # Specifies whether to delete the physical files at the same time.
        self.delete_physical_files = delete_physical_files
        # Not supported.
        self.input_urls = input_urls
        # The media asset IDs, separated by commas. Invalid IDs are added to IgnoredList.
        self.media_ids = media_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_config is not None:
            result['BizConfig'] = self.biz_config

        if self.delete_physical_files is not None:
            result['DeletePhysicalFiles'] = self.delete_physical_files

        if self.input_urls is not None:
            result['InputURLs'] = self.input_urls

        if self.media_ids is not None:
            result['MediaIds'] = self.media_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizConfig') is not None:
            self.biz_config = m.get('BizConfig')

        if m.get('DeletePhysicalFiles') is not None:
            self.delete_physical_files = m.get('DeletePhysicalFiles')

        if m.get('InputURLs') is not None:
            self.input_urls = m.get('InputURLs')

        if m.get('MediaIds') is not None:
            self.media_ids = m.get('MediaIds')

        return self

