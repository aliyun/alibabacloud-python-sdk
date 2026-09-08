# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sddp20260120 import models as main_models
from darabonba.model import DaraModel

class ListDataMaskingEncryptionAlgorithmsResponseBody(DaraModel):
    def __init__(
        self,
        algorithms: List[main_models.ListDataMaskingEncryptionAlgorithmsResponseBodyAlgorithms] = None,
        request_id: str = None,
    ):
        self.algorithms = algorithms
        self.request_id = request_id

    def validate(self):
        if self.algorithms:
            for v1 in self.algorithms:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Algorithms'] = []
        if self.algorithms is not None:
            for k1 in self.algorithms:
                result['Algorithms'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.algorithms = []
        if m.get('Algorithms') is not None:
            for k1 in m.get('Algorithms'):
                temp_model = main_models.ListDataMaskingEncryptionAlgorithmsResponseBodyAlgorithms()
                self.algorithms.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDataMaskingEncryptionAlgorithmsResponseBodyAlgorithms(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        name: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.name = name

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

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

