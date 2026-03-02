# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class JobDiagnosis(DaraModel):
    def __init__(
        self,
        diagnose_id: str = None,
        diagnose_time: int = None,
        namespace: str = None,
        risk_level: str = None,
        symptoms: main_models.JobDiagnosisSymptoms = None,
        workspace: str = None,
    ):
        # The diagnostic task ID.
        self.diagnose_id = diagnose_id
        # The time when the deployment is diagnosed.
        self.diagnose_time = diagnose_time
        # The namespace.
        self.namespace = namespace
        # The severity level of the risk.
        # 
        # Valid values:
        # 
        # *   RISK_LEVEL_HIGH
        # *   RISK_LEVEL_MID
        # *   RISK_LEVEL_LOW
        self.risk_level = risk_level
        # The diagnostic details.
        self.symptoms = symptoms
        # The workspace to which the deployment belongs.
        self.workspace = workspace

    def validate(self):
        if self.symptoms:
            self.symptoms.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.diagnose_id is not None:
            result['diagnoseId'] = self.diagnose_id

        if self.diagnose_time is not None:
            result['diagnoseTime'] = self.diagnose_time

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.risk_level is not None:
            result['riskLevel'] = self.risk_level

        if self.symptoms is not None:
            result['symptoms'] = self.symptoms.to_map()

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('diagnoseId') is not None:
            self.diagnose_id = m.get('diagnoseId')

        if m.get('diagnoseTime') is not None:
            self.diagnose_time = m.get('diagnoseTime')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('riskLevel') is not None:
            self.risk_level = m.get('riskLevel')

        if m.get('symptoms') is not None:
            temp_model = main_models.JobDiagnosisSymptoms()
            self.symptoms = temp_model.from_map(m.get('symptoms'))

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

