# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class UpdateWorkflowTemplateRequest(DaraModel):
    def __init__(
        self,
        action: str = None,
        collaboration_group_id: str = None,
        definition: Dict[str, Any] = None,
        source_version: str = None,
        template_id: str = None,
        tenant_id: str = None,
        version: str = None,
        version_description: str = None,
    ):
        # The write action. Valid values:
        # - SAVE: Saves the template as a draft without taking effect.
        # - SUBMIT: Saves and submits the template, setting it as the only effective version.
        # Default value: SUBMIT.
        self.action = action
        # The ID of the collaboration workspace.
        # 
        # This parameter is required.
        self.collaboration_group_id = collaboration_group_id
        # The complete JSON definition of the template to overwrite the existing one.
        # 
        # This parameter is required.
        self.definition = definition
        # The submitted version number on which the new version is based. This parameter is mutually exclusive with the version parameter. If not specified, the current effective version is used as the fallback.
        self.source_version = source_version
        # The ID of the template.
        # 
        # This parameter is required.
        self.template_id = template_id
        # The tenant ID. This is a common parameter. If not specified, the default tenant of the caller is used.
        self.tenant_id = tenant_id
        # The draft template version number to write. The format is a lowercase v followed by a positive integer, such as v1. Submitted versions cannot be written. If not specified, a new version is generated.
        self.version = version
        # The version description. The maximum length is 500 characters. When writing a draft, if this parameter is not specified or is null, the original value is retained. An empty string clears the value.
        self.version_description = version_description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['action'] = self.action

        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        if self.definition is not None:
            result['definition'] = self.definition

        if self.source_version is not None:
            result['sourceVersion'] = self.source_version

        if self.template_id is not None:
            result['templateId'] = self.template_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.version is not None:
            result['version'] = self.version

        if self.version_description is not None:
            result['versionDescription'] = self.version_description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')

        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('definition') is not None:
            self.definition = m.get('definition')

        if m.get('sourceVersion') is not None:
            self.source_version = m.get('sourceVersion')

        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('versionDescription') is not None:
            self.version_description = m.get('versionDescription')

        return self

