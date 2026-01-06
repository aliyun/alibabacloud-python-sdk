# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Adb4MysqlSparkDiagnosisInfo(DaraModel):
    def __init__(
        self,
        diagnosis_code: str = None,
        diagnosis_code_label: str = None,
        diagnosis_msg: str = None,
        diagnosis_type: str = None,
    ):
        self.diagnosis_code = diagnosis_code
        self.diagnosis_code_label = diagnosis_code_label
        self.diagnosis_msg = diagnosis_msg
        self.diagnosis_type = diagnosis_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.diagnosis_code is not None:
            result['DiagnosisCode'] = self.diagnosis_code

        if self.diagnosis_code_label is not None:
            result['DiagnosisCodeLabel'] = self.diagnosis_code_label

        if self.diagnosis_msg is not None:
            result['DiagnosisMsg'] = self.diagnosis_msg

        if self.diagnosis_type is not None:
            result['DiagnosisType'] = self.diagnosis_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiagnosisCode') is not None:
            self.diagnosis_code = m.get('DiagnosisCode')

        if m.get('DiagnosisCodeLabel') is not None:
            self.diagnosis_code_label = m.get('DiagnosisCodeLabel')

        if m.get('DiagnosisMsg') is not None:
            self.diagnosis_msg = m.get('DiagnosisMsg')

        if m.get('DiagnosisType') is not None:
            self.diagnosis_type = m.get('DiagnosisType')

        return self

