# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitConvertImageToWordJobShrinkRequest(DaraModel):
    def __init__(
        self,
        image_name_extension: str = None,
        image_names_shrink: str = None,
        image_urls_shrink: str = None,
        oss_bucket: str = None,
        oss_endpoint: str = None,
    ):
        self.image_name_extension = image_name_extension
        self.image_names_shrink = image_names_shrink
        self.image_urls_shrink = image_urls_shrink
        self.oss_bucket = oss_bucket
        self.oss_endpoint = oss_endpoint

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_name_extension is not None:
            result['ImageNameExtension'] = self.image_name_extension

        if self.image_names_shrink is not None:
            result['ImageNames'] = self.image_names_shrink

        if self.image_urls_shrink is not None:
            result['ImageUrls'] = self.image_urls_shrink

        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket

        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageNameExtension') is not None:
            self.image_name_extension = m.get('ImageNameExtension')

        if m.get('ImageNames') is not None:
            self.image_names_shrink = m.get('ImageNames')

        if m.get('ImageUrls') is not None:
            self.image_urls_shrink = m.get('ImageUrls')

        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')

        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')

        return self

