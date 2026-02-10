# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMaliciousFileWhitelistConfigRequest(DaraModel):
    def __init__(
        self,
        event_name: str = None,
        field: str = None,
        field_value: str = None,
        operator: str = None,
        remark: str = None,
        source: str = None,
        target_type: str = None,
        target_value: str = None,
    ):
        # Alert name:
        # - ALL: All alerts
        self.event_name = event_name
        # Field used for whitelist in sensitive file alerts.
        self.field = field
        # Expected value of the field to be whitelisted.
        self.field_value = field_value
        # Rule judgment operator:
        # - strEqual: String equals
        self.operator = operator
        # Remarks.
        self.remark = remark
        # Business source:
        # - agentless: Agentless detection
        self.source = source
        # Effective target type:
        # - ALL: All assets
        # - SELECTION_KEY: Assets selected via the asset selection component
        self.target_type = target_type
        # Target effective scope:
        # - ALL: All assets
        # - Other: Key of the asset range selected by the asset selection component
        self.target_value = target_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.field is not None:
            result['Field'] = self.field

        if self.field_value is not None:
            result['FieldValue'] = self.field_value

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.source is not None:
            result['Source'] = self.source

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.target_value is not None:
            result['TargetValue'] = self.target_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('Field') is not None:
            self.field = m.get('Field')

        if m.get('FieldValue') is not None:
            self.field_value = m.get('FieldValue')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('TargetValue') is not None:
            self.target_value = m.get('TargetValue')

        return self

