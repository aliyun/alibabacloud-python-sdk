# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class GetWmEmbedTaskResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetWmEmbedTaskResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetWmEmbedTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetWmEmbedTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        file_url: str = None,
        file_url_exp: str = None,
        filename: str = None,
        out_file_hash_md_5: str = None,
        out_file_size: int = None,
        task_id: str = None,
        task_status: str = None,
    ):
        self.file_url = file_url
        self.file_url_exp = file_url_exp
        self.filename = filename
        self.out_file_hash_md_5 = out_file_hash_md_5
        self.out_file_size = out_file_size
        self.task_id = task_id
        self.task_status = task_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.file_url_exp is not None:
            result['FileUrlExp'] = self.file_url_exp

        if self.filename is not None:
            result['Filename'] = self.filename

        if self.out_file_hash_md_5 is not None:
            result['OutFileHashMd5'] = self.out_file_hash_md_5

        if self.out_file_size is not None:
            result['OutFileSize'] = self.out_file_size

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('FileUrlExp') is not None:
            self.file_url_exp = m.get('FileUrlExp')

        if m.get('Filename') is not None:
            self.filename = m.get('Filename')

        if m.get('OutFileHashMd5') is not None:
            self.out_file_hash_md_5 = m.get('OutFileHashMd5')

        if m.get('OutFileSize') is not None:
            self.out_file_size = m.get('OutFileSize')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        return self

