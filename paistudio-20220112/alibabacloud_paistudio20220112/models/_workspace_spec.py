# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class WorkspaceSpec(DaraModel):
    def __init__(
        self,
        code: str = None,
        code_type: str = None,
        is_guaranteed_valid: bool = None,
        is_over_sold_valid: bool = None,
        reason: str = None,
        spec: main_models.ResourceAmount = None,
        spec_name: str = None,
    ):
        self.code = code
        self.code_type = code_type
        self.is_guaranteed_valid = is_guaranteed_valid
        self.is_over_sold_valid = is_over_sold_valid
        self.reason = reason
        self.spec = spec
        self.spec_name = spec_name

    def validate(self):
        if self.spec:
            self.spec.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.code_type is not None:
            result['CodeType'] = self.code_type

        if self.is_guaranteed_valid is not None:
            result['IsGuaranteedValid'] = self.is_guaranteed_valid

        if self.is_over_sold_valid is not None:
            result['IsOverSoldValid'] = self.is_over_sold_valid

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.spec is not None:
            result['Spec'] = self.spec.to_map()

        if self.spec_name is not None:
            result['SpecName'] = self.spec_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CodeType') is not None:
            self.code_type = m.get('CodeType')

        if m.get('IsGuaranteedValid') is not None:
            self.is_guaranteed_valid = m.get('IsGuaranteedValid')

        if m.get('IsOverSoldValid') is not None:
            self.is_over_sold_valid = m.get('IsOverSoldValid')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Spec') is not None:
            temp_model = main_models.ResourceAmount()
            self.spec = temp_model.from_map(m.get('Spec'))

        if m.get('SpecName') is not None:
            self.spec_name = m.get('SpecName')

        return self

