# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eas20210701 import models as main_models
from darabonba.model import DaraModel

class DescribeServiceInstanceDiagnosisResponseBody(DaraModel):
    def __init__(
        self,
        diagnosis: main_models.DescribeServiceInstanceDiagnosisResponseBodyDiagnosis = None,
        request_id: str = None,
    ):
        # The diagnostics information.
        self.diagnosis = diagnosis
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.diagnosis:
            self.diagnosis.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.diagnosis is not None:
            result['Diagnosis'] = self.diagnosis.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Diagnosis') is not None:
            temp_model = main_models.DescribeServiceInstanceDiagnosisResponseBodyDiagnosis()
            self.diagnosis = temp_model.from_map(m.get('Diagnosis'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeServiceInstanceDiagnosisResponseBodyDiagnosis(DaraModel):
    def __init__(
        self,
        advices: List[str] = None,
        causes: List[str] = None,
        error: str = None,
    ):
        # The solutions to the errors.
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

