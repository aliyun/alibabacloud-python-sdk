# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateFCTriggerRequest(DaraModel):
    def __init__(
        self,
        function_arn: str = None,
        notes: str = None,
        role_arn: str = None,
        source_arn: str = None,
        trigger_arn: str = None,
    ):
        # The feature trigger.
        self.function_arn = function_arn
        # The remarks.
        self.notes = notes
        # The assigned RAM role.
        self.role_arn = role_arn
        # The resources and filters for event listening.
        self.source_arn = source_arn
        # The trigger that corresponds to the Function Compute service.
        # 
        # This parameter is required.
        self.trigger_arn = trigger_arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.function_arn is not None:
            result['FunctionARN'] = self.function_arn

        if self.notes is not None:
            result['Notes'] = self.notes

        if self.role_arn is not None:
            result['RoleARN'] = self.role_arn

        if self.source_arn is not None:
            result['SourceARN'] = self.source_arn

        if self.trigger_arn is not None:
            result['TriggerARN'] = self.trigger_arn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FunctionARN') is not None:
            self.function_arn = m.get('FunctionARN')

        if m.get('Notes') is not None:
            self.notes = m.get('Notes')

        if m.get('RoleARN') is not None:
            self.role_arn = m.get('RoleARN')

        if m.get('SourceARN') is not None:
            self.source_arn = m.get('SourceARN')

        if m.get('TriggerARN') is not None:
            self.trigger_arn = m.get('TriggerARN')

        return self

