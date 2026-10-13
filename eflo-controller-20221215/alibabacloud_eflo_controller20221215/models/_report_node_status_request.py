# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReportNodeStatusRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        diagnosis_type: str = None,
        node_id: str = None,
    ):
        # The detailed description of the exception.
        # 
        # This parameter is required.
        self.description = description
        # The diagnosis type. Valid values:
        # - QUICK: quick diagnosis
        # - COMPREHENSIVE: comprehensive diagnosis
        # 
        # This parameter is required.
        self.diagnosis_type = diagnosis_type
        # The node ID.
        # 
        # This parameter is required.
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.diagnosis_type is not None:
            result['DiagnosisType'] = self.diagnosis_type

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DiagnosisType') is not None:
            self.diagnosis_type = m.get('DiagnosisType')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        return self

