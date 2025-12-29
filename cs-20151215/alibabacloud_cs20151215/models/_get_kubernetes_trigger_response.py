# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class GetKubernetesTriggerResponse(DaraModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[main_models.GetKubernetesTriggerResponseBody] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            for v1 in self.body:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.headers is not None:
            result['headers'] = self.headers

        if self.status_code is not None:
            result['statusCode'] = self.status_code

        result['body'] = []
        if self.body is not None:
            for k1 in self.body:
                result['body'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')

        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')

        self.body = []
        if m.get('body') is not None:
            for k1 in m.get('body'):
                temp_model = main_models.GetKubernetesTriggerResponseBody()
                self.body.append(temp_model.from_map(k1))

        return self

class GetKubernetesTriggerResponseBody(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        cluster_id: str = None,
        project_id: str = None,
        type: str = None,
        action: str = None,
        token: str = None,
    ):
        # The ID of the trigger.
        self.id = id
        # The name of the trigger.
        self.name = name
        # The ID of the associated cluster.
        self.cluster_id = cluster_id
        # The name of the project.
        # 
        # The name consists of the namespace where the application is deployed and the name of the application. The format is `${namespace}/${name}`. Example: default/test-app.
        self.project_id = project_id
        # The type of trigger.
        # 
        # Valid values:
        # 
        # *   `deployment`: performs actions on Deployments.
        # *   `application`: performs actions on applications that are deployed in Application Center.
        # 
        # Default value: `deployment`.
        self.type = type
        # The action that the trigger performs. The value is set to redeploy.
        # 
        # `redeploy`: redeploys the resource specified by project_id.
        self.action = action
        # Token
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id

        if self.project_id is not None:
            result['project_id'] = self.project_id

        if self.type is not None:
            result['type'] = self.type

        if self.action is not None:
            result['action'] = self.action

        if self.token is not None:
            result['token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')

        if m.get('project_id') is not None:
            self.project_id = m.get('project_id')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('action') is not None:
            self.action = m.get('action')

        if m.get('token') is not None:
            self.token = m.get('token')

        return self

