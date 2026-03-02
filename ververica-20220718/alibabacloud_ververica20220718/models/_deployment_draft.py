# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class DeploymentDraft(DaraModel):
    def __init__(
        self,
        artifact: main_models.Artifact = None,
        created_at: int = None,
        creator: str = None,
        creator_name: str = None,
        deployment_draft_id: str = None,
        engine_version: str = None,
        execution_mode: str = None,
        labels: Dict[str, Any] = None,
        local_variables: List[main_models.LocalVariable] = None,
        lock: main_models.Lock = None,
        modified_at: int = None,
        modifier: str = None,
        modifier_name: str = None,
        name: str = None,
        namespace: str = None,
        parent_id: str = None,
        referenced_deployment_id: str = None,
        workspace: str = None,
    ):
        # The script of the SQL deployment.
        self.artifact = artifact
        # The time when the draft was created.
        self.created_at = created_at
        # The ID of the account that is used to create the draft.
        self.creator = creator
        # The name of the account that is used to create the draft.
        self.creator_name = creator_name
        # The draft ID.
        self.deployment_draft_id = deployment_draft_id
        # The engine version of the deployment.
        self.engine_version = engine_version
        # The execution mode.
        self.execution_mode = execution_mode
        # The labels of the deployment.
        self.labels = labels
        # The variables.
        self.local_variables = local_variables
        # The lock of the draft.
        self.lock = lock
        # The time when the draft was modified.
        self.modified_at = modified_at
        # The ID of the account that is used to modify the draft.
        self.modifier = modifier
        # The name of the account that is used to modify the draft.
        self.modifier_name = modifier_name
        # The name of the draft.
        self.name = name
        # The name of the namespace.
        self.namespace = namespace
        # The ID of the parent folder.
        self.parent_id = parent_id
        # The ID of the associated deployment.
        self.referenced_deployment_id = referenced_deployment_id
        # The workspace.
        self.workspace = workspace

    def validate(self):
        if self.artifact:
            self.artifact.validate()
        if self.local_variables:
            for v1 in self.local_variables:
                 if v1:
                    v1.validate()
        if self.lock:
            self.lock.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.artifact is not None:
            result['artifact'] = self.artifact.to_map()

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.creator is not None:
            result['creator'] = self.creator

        if self.creator_name is not None:
            result['creatorName'] = self.creator_name

        if self.deployment_draft_id is not None:
            result['deploymentDraftId'] = self.deployment_draft_id

        if self.engine_version is not None:
            result['engineVersion'] = self.engine_version

        if self.execution_mode is not None:
            result['executionMode'] = self.execution_mode

        if self.labels is not None:
            result['labels'] = self.labels

        result['localVariables'] = []
        if self.local_variables is not None:
            for k1 in self.local_variables:
                result['localVariables'].append(k1.to_map() if k1 else None)

        if self.lock is not None:
            result['lock'] = self.lock.to_map()

        if self.modified_at is not None:
            result['modifiedAt'] = self.modified_at

        if self.modifier is not None:
            result['modifier'] = self.modifier

        if self.modifier_name is not None:
            result['modifierName'] = self.modifier_name

        if self.name is not None:
            result['name'] = self.name

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.parent_id is not None:
            result['parentId'] = self.parent_id

        if self.referenced_deployment_id is not None:
            result['referencedDeploymentId'] = self.referenced_deployment_id

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('artifact') is not None:
            temp_model = main_models.Artifact()
            self.artifact = temp_model.from_map(m.get('artifact'))

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('creator') is not None:
            self.creator = m.get('creator')

        if m.get('creatorName') is not None:
            self.creator_name = m.get('creatorName')

        if m.get('deploymentDraftId') is not None:
            self.deployment_draft_id = m.get('deploymentDraftId')

        if m.get('engineVersion') is not None:
            self.engine_version = m.get('engineVersion')

        if m.get('executionMode') is not None:
            self.execution_mode = m.get('executionMode')

        if m.get('labels') is not None:
            self.labels = m.get('labels')

        self.local_variables = []
        if m.get('localVariables') is not None:
            for k1 in m.get('localVariables'):
                temp_model = main_models.LocalVariable()
                self.local_variables.append(temp_model.from_map(k1))

        if m.get('lock') is not None:
            temp_model = main_models.Lock()
            self.lock = temp_model.from_map(m.get('lock'))

        if m.get('modifiedAt') is not None:
            self.modified_at = m.get('modifiedAt')

        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')

        if m.get('modifierName') is not None:
            self.modifier_name = m.get('modifierName')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')

        if m.get('referencedDeploymentId') is not None:
            self.referenced_deployment_id = m.get('referencedDeploymentId')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

