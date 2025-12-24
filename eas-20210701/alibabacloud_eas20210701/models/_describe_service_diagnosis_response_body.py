# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eas20210701 import models as main_models
from darabonba.model import DaraModel

class DescribeServiceDiagnosisResponseBody(DaraModel):
    def __init__(
        self,
        diagnosis_list: List[main_models.DescribeServiceDiagnosisResponseBodyDiagnosisList] = None,
        request_id: str = None,
    ):
        # The diagnostics list.
        self.diagnosis_list = diagnosis_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.diagnosis_list:
            for v1 in self.diagnosis_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DiagnosisList'] = []
        if self.diagnosis_list is not None:
            for k1 in self.diagnosis_list:
                result['DiagnosisList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.diagnosis_list = []
        if m.get('DiagnosisList') is not None:
            for k1 in m.get('DiagnosisList'):
                temp_model = main_models.DescribeServiceDiagnosisResponseBodyDiagnosisList()
                self.diagnosis_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeServiceDiagnosisResponseBodyDiagnosisList(DaraModel):
    def __init__(
        self,
        advices: List[str] = None,
        causes: List[str] = None,
        error: str = None,
    ):
        # The suggestions about how to handle the errors.
        self.advices = advices
        # The causes of the errors.
        self.causes = causes
        # The error message.
        self.error = error

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advices is not None:
            result['Advices'] = self.advices

        if self.causes is not None:
            result['Causes'] = self.causes

        if self.error is not None:
            result['Error'] = self.error

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Advices') is not None:
            self.advices = m.get('Advices')

        if m.get('Causes') is not None:
            self.causes = m.get('Causes')

        if m.get('Error') is not None:
            self.error = m.get('Error')

        return self

