# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitDigitalDocStructureJobRequest(DaraModel):
    def __init__(
        self,
        file_name: str = None,
        file_name_extension: str = None,
        file_url: str = None,
        image_strategy: str = None,
        oss_bucket: str = None,
        oss_endpoint: str = None,
        reveal_markdown: bool = None,
        use_url_response_body: bool = None,
    ):
        self.file_name = file_name
        self.file_name_extension = file_name_extension
        self.file_url = file_url
        self.image_strategy = image_strategy
        self.oss_bucket = oss_bucket
        self.oss_endpoint = oss_endpoint
        self.reveal_markdown = reveal_markdown
        self.use_url_response_body = use_url_response_body

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_name_extension is not None:
            result['FileNameExtension'] = self.file_name_extension

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.image_strategy is not None:
            result['ImageStrategy'] = self.image_strategy

        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket

        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint

        if self.reveal_markdown is not None:
            result['RevealMarkdown'] = self.reveal_markdown

        if self.use_url_response_body is not None:
            result['UseUrlResponseBody'] = self.use_url_response_body

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('ImageStrategy') is not None:
            self.image_strategy = m.get('ImageStrategy')

        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')

        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')

        if m.get('RevealMarkdown') is not None:
            self.reveal_markdown = m.get('RevealMarkdown')

        if m.get('UseUrlResponseBody') is not None:
            self.use_url_response_body = m.get('UseUrlResponseBody')

        return self

