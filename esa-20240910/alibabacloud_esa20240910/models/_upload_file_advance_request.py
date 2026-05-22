# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import BinaryIO

from darabonba.model import DaraModel

class UploadFileAdvanceRequest(DaraModel):
    def __init__(
        self,
        site_id: int = None,
        type: str = None,
        upload_task_name: str = None,
        url_object: BinaryIO = None,
    ):
        # The website ID. You can call the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation to obtain the ID.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The type of the purge or prefetch task. Valid values:
        # 
        # *   **file** (default): purges the cache by file.
        # *   **preload**: prefetches the file.
        # *   **directory**: purges the cache by directory.
        # *   **ignoreParams**: purges the cache by URL with specified parameters ignored.
        # 
        # This parameter is required.
        self.type = type
        # The name of the upload task.
        # 
        # This parameter is required.
        self.upload_task_name = upload_task_name
        # The OSS URL of the file that contains resources to be purged or prefetched.
        # 
        # This parameter is required.
        self.url_object = url_object

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

        if self.url_object is not None:
            result['Url'] = self.url_object

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
            self.url_object = m.get('Url')

        return self

