# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateWorkflowInstanceShrinkRequest(DaraModel):
    def __init__(
        self,
        acceptance_criteria: str = None,
        app_token: str = None,
        business_id: str = None,
        collaboration_group_id: str = None,
        initiator: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        priority: str = None,
        template_id: str = None,
        tenant_id: str = None,
        title: str = None,
        variables_shrink: str = None,
    ):
        # The required acceptance criteria for the workflow.
        # 
        # This parameter is required.
        self.acceptance_criteria = acceptance_criteria
        # 平台应用 Token（控制台签发）。传入后将以 opsUserId 或 opsUserCode 指定的用户身份执行
        self.app_token = app_token
        # The unique requirement ID in the workspace. Repeated requests are idempotent.
        # 
        # This parameter is required.
        self.business_id = business_id
        # The collaboration workspace ID.
        # 
        # This parameter is required.
        self.collaboration_group_id = collaboration_group_id
        # The display label of the external initiator.
        self.initiator = initiator
        # 代理用户编码（租户内唯一），仅当应用凭证配置为 source_uid 时使用
        self.ops_user_code = ops_user_code
        # 代理用户ID（WINNEXO 平台用户ID），仅当应用凭证配置为 winnexo_uid 时使用
        self.ops_user_id = ops_user_id
        # The work item priority.
        self.priority = priority
        # The workflow template ID. Maximum length: 64 characters.
        # 
        # This parameter is required.
        self.template_id = template_id
        # The tenant ID. This is a common parameter explicitly passed by using --tenant-id in winnexo-cli.
        self.tenant_id = tenant_id
        # The requirement title.
        # 
        # This parameter is required.
        self.title = title
        # The business variable object. The tags field can be a list of string tags.
        self.variables_shrink = variables_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acceptance_criteria is not None:
            result['acceptanceCriteria'] = self.acceptance_criteria

        if self.app_token is not None:
            result['appToken'] = self.app_token

        if self.business_id is not None:
            result['businessId'] = self.business_id

        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        if self.initiator is not None:
            result['initiator'] = self.initiator

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

        if self.priority is not None:
            result['priority'] = self.priority

        if self.template_id is not None:
            result['templateId'] = self.template_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.title is not None:
            result['title'] = self.title

        if self.variables_shrink is not None:
            result['variables'] = self.variables_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acceptanceCriteria') is not None:
            self.acceptance_criteria = m.get('acceptanceCriteria')

        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('businessId') is not None:
            self.business_id = m.get('businessId')

        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('initiator') is not None:
            self.initiator = m.get('initiator')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('priority') is not None:
            self.priority = m.get('priority')

        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('variables') is not None:
            self.variables_shrink = m.get('variables')

        return self

