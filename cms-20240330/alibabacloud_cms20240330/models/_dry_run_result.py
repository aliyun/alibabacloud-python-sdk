# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class DryRunResult(DaraModel):
    def __init__(
        self,
        exit_code: int = None,
        result: str = None,
        violations: List[main_models.DryRunViolation] = None,
    ):
        # The exit code. A value of 0 indicates that the validation passed. A value of 1 indicates that the request was rejected by business rules. For specific reasons, see violations. A value of 2 indicates that the request structure cannot be parsed and rule validation cannot be performed.
        self.exit_code = exit_code
        # The text representation of the result. A value of ok indicates that the validation passed, and rejected indicates that the request was rejected by business rules. This field is empty when the exit code is 2, which means the request structure cannot be parsed.
        self.result = result
        # The list of violations. Each violation consists of three elements: field, message, and suggestion, which represent the path of the violated field, the violation description, and the remediation suggestion, respectively. This array is empty when the exit code is 0 (passed). All violations are listed when the exit code is 1 (rejected by business rules). The location and cause of the unparseable fields are provided when the exit code is 2 (unparseable request structure).
        self.violations = violations

    def validate(self):
        if self.violations:
            for v1 in self.violations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exit_code is not None:
            result['exitCode'] = self.exit_code

        if self.result is not None:
            result['result'] = self.result

        result['violations'] = []
        if self.violations is not None:
            for k1 in self.violations:
                result['violations'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('exitCode') is not None:
            self.exit_code = m.get('exitCode')

        if m.get('result') is not None:
            self.result = m.get('result')

        self.violations = []
        if m.get('violations') is not None:
            for k1 in m.get('violations'):
                temp_model = main_models.DryRunViolation()
                self.violations.append(temp_model.from_map(k1))

        return self

