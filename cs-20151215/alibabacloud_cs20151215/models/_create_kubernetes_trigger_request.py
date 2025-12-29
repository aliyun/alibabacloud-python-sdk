# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateKubernetesTriggerRequest(DaraModel):
    def __init__(
        self,
        action: str = None,
        cluster_id: str = None,
        project_id: str = None,
        type: str = None,
    ):
        # The action that the trigger performs. Set the value to redeploy.
        # 
        # `redeploy`: redeploys the resources specified by `project_id`.
        # 
        # This parameter is required.
        self.action = action
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The name of the trigger project.
        # 
        # The name consists of the namespace where the application is deployed and the name of the application. The format is `${namespace}/${name}`.
        # 
        # Example: `default/test-app`.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The type of trigger. Valid values:
        # 
        # *   `deployment`: performs actions on Deployments.
        # *   `application`: performs actions on applications that are deployed in Application Center.
        # 
        # Default value: `deployment`.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['action'] = self.action

        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id

        if self.project_id is not None:
            result['project_id'] = self.project_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')

        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')

        if m.get('project_id') is not None:
            self.project_id = m.get('project_id')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

