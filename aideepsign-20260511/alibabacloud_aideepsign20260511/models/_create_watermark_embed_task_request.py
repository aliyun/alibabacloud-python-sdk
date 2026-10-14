# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateWatermarkEmbedTaskRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        file_type: str = None,
        file_url: str = None,
        level: str = None,
        reserved: str = None,
        watermark_content: str = None,
    ):
        # A reserved idempotency field. This field is not supported. Passing a value does not cause an error, but it does not produce an idempotency effect.
        self.client_token = client_token
        # The file type. Valid values:
        # - image: image.
        # - video: video.
        # 
        # The value must match the actual file type.
        # 
        # This parameter is required.
        self.file_type = file_type
        # The URL of the file to be processed. Images and videos are supported. Only the HTTP and HTTPS protocols are supported. Videos must be no longer than 10 minutes and no larger than 100 MB.
        self.file_url = file_url
        # The embedding strength. Valid values: 0 to 5. A higher strength provides better robustness but lower visual quality.
        # 
        # This parameter is required.
        self.level = level
        # A reserved field. No valid values are available. Do not specify this parameter.
        self.reserved = reserved
        # The watermark content. The embedded content can be restored to the original text by calling the extraction operation.
        self.watermark_content = watermark_content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.level is not None:
            result['Level'] = self.level

        if self.reserved is not None:
            result['Reserved'] = self.reserved

        if self.watermark_content is not None:
            result['WatermarkContent'] = self.watermark_content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Reserved') is not None:
            self.reserved = m.get('Reserved')

        if m.get('WatermarkContent') is not None:
            self.watermark_content = m.get('WatermarkContent')

        return self

