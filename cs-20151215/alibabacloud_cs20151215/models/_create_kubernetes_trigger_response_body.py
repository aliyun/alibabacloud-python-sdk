# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateKubernetesTriggerResponseBody(DaraModel):
    def __init__(
        self,
        action: str = None,
        cluster_id: str = None,
        id: str = None,
        project_id: str = None,
        type: str = None,
    ):
        # The action that the trigger performs. For example, a value of `redeploy` indicates that the trigger redeploys the application.
        self.action = action
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The ID of the trigger.
        self.id = id
        # The name of the trigger project.
        self.project_id = project_id
        # The type of trigger.
        # 
        # Valid values:
        # 
        # *   `deployment`: performs actions on Deployments.
        # *   `application`: performs actions on applications that are deployed in Application Center.
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

        if self.id is not None:
            result['id'] = self.id

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

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('project_id') is not None:
            self.project_id = m.get('project_id')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

