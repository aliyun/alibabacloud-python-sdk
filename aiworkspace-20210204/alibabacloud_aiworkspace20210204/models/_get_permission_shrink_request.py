# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPermissionShrinkRequest(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        creator: str = None,
        labels_shrink: str = None,
        option: str = None,
        resource: str = None,
    ):
        # The accessibility. Valid values:
        # 
        # *   PUBLIC: All members in the workspace can access the workspace.
        # *   PRIVATE: Only the creator can access the workspace.
        self.accessibility = accessibility
        # The UID of the Alibaba Cloud account that is used to create the workspace.
        self.creator = creator
        self.labels_shrink = labels_shrink
        # The configuration. Separate multiple configurations with commas (,). Valid values:
        # 
        # *   ResourceEmpty: The Resource parameter is not configured.
        # *   DisableRam: The RAM check is not performed.
        self.option = option
        # The resource.
        self.resource = resource

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.labels_shrink is not None:
            result['Labels'] = self.labels_shrink

        if self.option is not None:
            result['Option'] = self.option

        if self.resource is not None:
            result['Resource'] = self.resource

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('Labels') is not None:
            self.labels_shrink = m.get('Labels')

        if m.get('Option') is not None:
            self.option = m.get('Option')

        if m.get('Resource') is not None:
            self.resource = m.get('Resource')

        return self

