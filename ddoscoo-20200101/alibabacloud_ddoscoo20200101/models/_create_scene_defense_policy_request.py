# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSceneDefensePolicyRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        name: str = None,
        start_time: int = None,
        template: str = None,
    ):
        # The end time of the policy. This value is a UNIX timestamp. Units: milliseconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The name of the policy.
        # 
        # This parameter is required.
        self.name = name
        # The start time of the policy. This value is a UNIX timestamp. Units: milliseconds.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The template of the policy. Valid values:
        # 
        # *   **promotion**: important activity.
        # *   **bypass**: all traffic forwarded.
        # 
        # This parameter is required.
        self.template = template

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.name is not None:
            result['Name'] = self.name

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.template is not None:
            result['Template'] = self.template

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        return self

