# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class JobDiagnosisSymptoms(DaraModel):
    def __init__(
        self,
        autopilot: main_models.JobDiagnosisSymptom = None,
        others: List[main_models.JobDiagnosisSymptom] = None,
        runtime: List[main_models.JobDiagnosisSymptom] = None,
        startup: List[main_models.JobDiagnosisSymptom] = None,
        state: List[main_models.JobDiagnosisSymptom] = None,
        troubleshooting: List[main_models.JobDiagnosisSymptom] = None,
    ):
        self.autopilot = autopilot
        self.others = others
        self.runtime = runtime
        self.startup = startup
        self.state = state
        self.troubleshooting = troubleshooting

    def validate(self):
        if self.autopilot:
            self.autopilot.validate()
        if self.others:
            for v1 in self.others:
                 if v1:
                    v1.validate()
        if self.runtime:
            for v1 in self.runtime:
                 if v1:
                    v1.validate()
        if self.startup:
            for v1 in self.startup:
                 if v1:
                    v1.validate()
        if self.state:
            for v1 in self.state:
                 if v1:
                    v1.validate()
        if self.troubleshooting:
            for v1 in self.troubleshooting:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.autopilot is not None:
            result['autopilot'] = self.autopilot.to_map()

        result['others'] = []
        if self.others is not None:
            for k1 in self.others:
                result['others'].append(k1.to_map() if k1 else None)

        result['runtime'] = []
        if self.runtime is not None:
            for k1 in self.runtime:
                result['runtime'].append(k1.to_map() if k1 else None)

        result['startup'] = []
        if self.startup is not None:
            for k1 in self.startup:
                result['startup'].append(k1.to_map() if k1 else None)

        result['state'] = []
        if self.state is not None:
            for k1 in self.state:
                result['state'].append(k1.to_map() if k1 else None)

        result['troubleshooting'] = []
        if self.troubleshooting is not None:
            for k1 in self.troubleshooting:
                result['troubleshooting'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autopilot') is not None:
            temp_model = main_models.JobDiagnosisSymptom()
            self.autopilot = temp_model.from_map(m.get('autopilot'))

        self.others = []
        if m.get('others') is not None:
            for k1 in m.get('others'):
                temp_model = main_models.JobDiagnosisSymptom()
                self.others.append(temp_model.from_map(k1))

        self.runtime = []
        if m.get('runtime') is not None:
            for k1 in m.get('runtime'):
                temp_model = main_models.JobDiagnosisSymptom()
                self.runtime.append(temp_model.from_map(k1))

        self.startup = []
        if m.get('startup') is not None:
            for k1 in m.get('startup'):
                temp_model = main_models.JobDiagnosisSymptom()
                self.startup.append(temp_model.from_map(k1))

        self.state = []
        if m.get('state') is not None:
            for k1 in m.get('state'):
                temp_model = main_models.JobDiagnosisSymptom()
                self.state.append(temp_model.from_map(k1))

        self.troubleshooting = []
        if m.get('troubleshooting') is not None:
            for k1 in m.get('troubleshooting'):
                temp_model = main_models.JobDiagnosisSymptom()
                self.troubleshooting.append(temp_model.from_map(k1))

        return self

