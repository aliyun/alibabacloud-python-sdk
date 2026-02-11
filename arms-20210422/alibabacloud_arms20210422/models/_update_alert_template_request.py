# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAlertTemplateRequest(DaraModel):
    def __init__(
        self,
        annotations: str = None,
        id: int = None,
        labels: str = None,
        match_expressions: str = None,
        message: str = None,
        name: str = None,
        region_id: str = None,
        rule: str = None,
        status: bool = None,
        type: str = None,
    ):
        self.annotations = annotations
        # This parameter is required.
        self.id = id
        self.labels = labels
        self.match_expressions = match_expressions
        # This parameter is required.
        self.message = message
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.region_id = region_id
        # This parameter is required.
        self.rule = rule
        # This parameter is required.
        self.status = status
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.annotations is not None:
            result['Annotations'] = self.annotations

        if self.id is not None:
            result['Id'] = self.id

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.match_expressions is not None:
            result['MatchExpressions'] = self.match_expressions

        if self.message is not None:
            result['Message'] = self.message

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.rule is not None:
            result['Rule'] = self.rule

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Annotations') is not None:
            self.annotations = m.get('Annotations')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('MatchExpressions') is not None:
            self.match_expressions = m.get('MatchExpressions')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

