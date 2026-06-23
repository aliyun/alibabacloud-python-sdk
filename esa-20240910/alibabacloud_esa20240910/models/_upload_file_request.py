# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadFileRequest(DaraModel):
    def __init__(
        self,
        site_id: int = None,
        type: str = None,
        upload_task_name: str = None,
        url: str = None,
    ):
        # The site ID, which can be obtained by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The type of the refresh or prefetch task. Valid values:
        # - **file** (default): file refresh.
        # - **preload**: file prefetch.
        # - **directory**: directory refresh.
        # - **ignoreParams**: parameter-ignored refresh.
        # 
        # This parameter is required.
        self.type = type
        # The name of the upload task.
        # 
        # This parameter is required.
        self.upload_task_name = upload_task_name
        # The URL of the refresh or prefetch file stored in OSS. The Url parameter accepts URLs in two formats:
        # 
        # - Transit URL (recommended): automatically generated through the file transfer feature of the ESA console or SDK.
        # 
        # - OSS pre-signed HTTPS URL: generated after you upload the file to an authorized OSS bucket. The isFileTransferUrl field specifies whether to use the transit URL mode.
        # 
        # This parameter is required.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.type is not None:
            result['Type'] = self.type

        if self.upload_task_name is not None:
            result['UploadTaskName'] = self.upload_task_name

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UploadTaskName') is not None:
            self.upload_task_name = m.get('UploadTaskName')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

