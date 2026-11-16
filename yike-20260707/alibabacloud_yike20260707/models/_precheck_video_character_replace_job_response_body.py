# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yike20260707 import models as main_models
from darabonba.model import DaraModel

class PrecheckVideoCharacterReplaceJobResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.PrecheckVideoCharacterReplaceJobResponseBodyResult] = None,
        status: str = None,
    ):
        # The request ID, which is used to locate and troubleshoot the request.
        self.request_id = request_id
        # The list of items that fail the validation. This is an empty array if the validation passes.
        self.result = result
        # The pre-validation status. A value of Success indicates that the validation passes. A value of Failed indicates that one or more items fail the validation.
        self.status = status

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.PrecheckVideoCharacterReplaceJobResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class PrecheckVideoCharacterReplaceJobResponseBodyResult(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        key: str = None,
    ):
        # The validation error code of the input item. For example, ImageCheckFailed indicates that the image validation fails, and AudioCheckFailed indicates that the audio validation fails.
        self.error_code = error_code
        # The name of the input parameter that fails the validation. This name is consistent with the corresponding field name in AppParams.
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.key is not None:
            result['Key'] = self.key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        return self

