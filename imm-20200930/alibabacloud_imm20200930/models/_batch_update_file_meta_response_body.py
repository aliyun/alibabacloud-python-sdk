# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class BatchUpdateFileMetaResponseBody(DaraModel):
    def __init__(
        self,
        files: List[main_models.BatchUpdateFileMetaResponseBodyFiles] = None,
        request_id: str = None,
    ):
        # The files whose metadata was updated.
        self.files = files
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.files:
            for v1 in self.files:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Files'] = []
        if self.files is not None:
            for k1 in self.files:
                result['Files'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.files = []
        if m.get('Files') is not None:
            for k1 in m.get('Files'):
                temp_model = main_models.BatchUpdateFileMetaResponseBodyFiles()
                self.files.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class BatchUpdateFileMetaResponseBodyFiles(DaraModel):
    def __init__(
        self,
        message: str = None,
        success: bool = None,
        uri: str = None,
    ):
        # The error message returned when the value of the Success parameter is false.
        self.message = message
        # Indicates whether the request was successful. Valid values:
        # 
        # Enumerated values:
        # 
        # *   true
        # *   false
        self.success = success
        # The URI of the file.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.success is not None:
            result['Success'] = self.success

        if self.uri is not None:
            result['URI'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('URI') is not None:
            self.uri = m.get('URI')

        return self

