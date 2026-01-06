# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateExperimentRequest(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        name: str = None,
    ):
        # The accessibility of the experiment in the workspace. Valid values:
        # 
        # *   PRIVATE: The experiment is accessible only to you and the administrator of the workspace.
        # *   PUBLIC: The experiment is accessible to all users in the workspace.
        self.accessibility = accessibility
        # The experiment name. The name must meet the following requirements:
        # 
        # *   The name must start with a letter.
        # *   The name can contain letters, digits, underscores (_), and hyphens (-).
        # *   The name must be 1 to 63 characters in length.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

