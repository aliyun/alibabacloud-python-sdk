# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class UpdateWorkflowTemplateRequest(DaraModel):
    def __init__(
        self,
        action: str = None,
        app_token: str = None,
        collaboration_group_id: str = None,
        definition: Dict[str, Any] = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        source_version: str = None,
        template_id: str = None,
        tenant_id: str = None,
        version: str = None,
        version_description: str = None,
    ):
        # The write action. Valid values: SAVE (saves the template as a draft without taking effect, and allows node names and executors to be left empty) and SUBMIT (requires complete nodes, and saves and submits the template as the only effective version). Default value: SUBMIT.
        self.action = action
        # The platform application token issued by the console. If specified, the operation is executed as the user specified by opsUserId or opsUserCode.
        self.app_token = app_token
        # The collaboration workspace ID.
        # 
        # This parameter is required.
        self.collaboration_group_id = collaboration_group_id
        # The complete JSON definition of the template for full overwriting.
        # 
        # This parameter is required.
        self.definition = definition
        # The proxy user code, which is unique within the tenant. This parameter is used only when the application credential is configured as source_uid.
        self.ops_user_code = ops_user_code
        # The proxy user ID, which is the WINNEXO platform user ID. This parameter is used only when the application credential is configured as winnexo_uid.
        self.ops_user_id = ops_user_id
        # The submitted version number on which the new version is based. This parameter is mutually exclusive with version. If not specified, the current effective version is used as the fallback.
        self.source_version = source_version
        # The template ID.
        # 
        # This parameter is required.
        self.template_id = template_id
        # The tenant ID. This is a common parameter. If not specified, the default tenant of the caller is used.
        self.tenant_id = tenant_id
        # The version number to which the returned content belongs.
        self.version = version
        # The change description for this version. An empty value indicates that no description is provided.
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

        if self.app_token is not None:
            result['appToken'] = self.app_token

        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        if self.definition is not None:
            result['definition'] = self.definition

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

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

        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('definition') is not None:
            self.definition = m.get('definition')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

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

