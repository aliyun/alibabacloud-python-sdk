# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadAppSiteValidationFileRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        domain: str = None,
        file: str = None,
        file_content: str = None,
        file_type: str = None,
        site_host: str = None,
    ):
        self.biz_id = biz_id
        self.domain = domain
        self.file = file
        self.file_content = file_content
        self.file_type = file_type
        self.site_host = site_host

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.file is not None:
            result['File'] = self.file

        if self.file_content is not None:
            result['FileContent'] = self.file_content

        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.site_host is not None:
            result['SiteHost'] = self.site_host

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('File') is not None:
            self.file = m.get('File')

        if m.get('FileContent') is not None:
            self.file_content = m.get('FileContent')

        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('SiteHost') is not None:
            self.site_host = m.get('SiteHost')

        return self

