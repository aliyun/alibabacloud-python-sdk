# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDownloadUrlRequest(DaraModel):
    def __init__(
        self,
        download_task_id: str = None,
        file_id: str = None,
    ):
        # This parameter is required.
        self.download_task_id = download_task_id
        # This parameter is required.
        self.file_id = file_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.download_task_id is not None:
            result['DownloadTaskId'] = self.download_task_id

        if self.file_id is not None:
            result['FileId'] = self.file_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadTaskId') is not None:
            self.download_task_id = m.get('DownloadTaskId')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        return self

