# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class AddStoryFilesResponseBody(DaraModel):
    def __init__(
        self,
        files: List[main_models.AddStoryFilesResponseBodyFiles] = None,
        request_id: str = None,
    ):
        # The objects that were added.
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
                temp_model = main_models.AddStoryFilesResponseBodyFiles()
                self.files.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class AddStoryFilesResponseBodyFiles(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        uri: str = None,
    ):
        # The error code.
        self.error_code = error_code
        # The error message that is returned.
        self.error_message = error_message
        # The URI of the object.
        # 
        # The OSS URI follows the `oss://{bucketname}/{objectname}` format, where `bucketname` is the name of the bucket in the same region as the current project and `objectname` is the path of the object with the extension included.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.uri is not None:
            result['URI'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('URI') is not None:
            self.uri = m.get('URI')

        return self

