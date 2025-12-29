# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeTriggerRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        namespace: str = None,
        type: str = None,
        action: str = None,
    ):
        # The application name.
        # 
        # This parameter is required.
        self.name = name
        # The namespace to which the application belongs.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The type of trigger. Valid values:
        # 
        # *   `deployment`: performs actions on Deployments.
        # *   `application`: performs actions on applications that are deployed in Application Center.
        # 
        # Default value: `deployment`.
        # 
        # If you do not set this parameter, triggers are not filtered by type.
        self.type = type
        # The action that the trigger performs. Set the value to redeploy.
        # 
        # `redeploy`: redeploys the resources specified by `project_id`.
        # 
        # If you do not specify this parameter, triggers are not filtered by action.
        self.action = action

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.type is not None:
            result['Type'] = self.type

        if self.action is not None:
            result['action'] = self.action

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('action') is not None:
            self.action = m.get('action')

        return self

