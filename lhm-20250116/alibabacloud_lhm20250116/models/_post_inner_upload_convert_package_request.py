# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PostInnerUploadConvertPackageRequest(DaraModel):
    def __init__(
        self,
        file_content_base_64: str = None,
        file_name: str = None,
        task_id: str = None,
    ):
        # The file content, Base64-encoded.
        self.file_content_base_64 = file_content_base_64
        # The file name.
        self.file_name = file_name
        # The task ID that uniquely identifies a task.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_content_base_64 is not None:
            result['fileContentBase64'] = self.file_content_base_64

        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileContentBase64') is not None:
            self.file_content_base_64 = m.get('fileContentBase64')

        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

