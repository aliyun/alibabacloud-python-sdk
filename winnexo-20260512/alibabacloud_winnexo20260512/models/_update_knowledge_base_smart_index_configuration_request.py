# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateKnowledgeBaseSmartIndexConfigurationRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        cron_expression: str = None,
        directory_id: str = None,
        enabled: bool = None,
        expected_revision: int = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        tenant_id: str = None,
        timezone: str = None,
    ):
        # The platform application credential. Pass this parameter when using the application proxy mode, and specify the operator by using opsUserId or opsUserCode based on the application configuration. Do not use real credentials in logs or public examples.
        self.app_token = app_token
        # The automatic execution schedule. Use a five-part cron expression where the minute field must be 0. For example, 0 2 * * * indicates execution at 02:00 every day based on the timezone. Omitting this parameter, setting it to null, or using a blank string indicates manual execution and clears the old automatic schedule, but does not disable the smart index. Maximum length: 100 characters.
        self.cron_expression = cron_expression
        # The business ID of the root directory for the standard enterprise knowledge base of the current tenant. You can obtain this ID from the response of the CreateTenantDirectory operation. You cannot use the internal primary key of the directory, or the IDs of personal spaces, group knowledge bases, subdirectories, or special knowledge bases.
        # 
        # This parameter is required.
        self.directory_id = directory_id
        # Specifies whether to enable the LLM Wiki smart index. Valid values:
        # - true: Enabled. Switching from disabled to enabled creates an asynchronous full build task and a bill.
        # - false: Disabled. If artifacts exist, asynchronous cleanup is initiated.
        # You cannot toggle the switch during task execution, and you cannot re-enable it until cleanup is complete.
        # 
        # This parameter is required.
        self.enabled = enabled
        # The revision obtained from the most recent configuration read. This value must be a non-negative integer. The value is 0 when not configured, and increments by 1 after a successful save. If the version does not match, ERR.SmartIndex.Conflict is returned. You must read the configuration again before saving. This field is not an idempotency key.
        # 
        # This parameter is required.
        self.expected_revision = expected_revision
        # The unique code of the proxied user within the tenant. This parameter is used only when the identity mapping mode of the application credential is source_uid. You cannot use this parameter to bypass tenant or knowledge base permission verification.
        self.ops_user_code = ops_user_code
        # The ID of the proxied WINNEXO platform user. This parameter is used only when the identity mapping mode of the application credential is winnexo_uid. You cannot use this parameter to bypass tenant or knowledge base permission verification.
        self.ops_user_id = ops_user_id
        # The ID of the target tenant. This parameter is used for tenant routing in public requests. The server-side authentication chain verifies access permissions based on this parameter. You cannot use this parameter to access unauthorized tenants.
        self.tenant_id = tenant_id
        # The IANA time zone name used for the execution schedule. Default value: Asia/Shanghai. If this parameter is omitted, set to null, or left as a blank string, the default value is used. The length of a non-empty value must be 1 to 64 characters.
        self.timezone = timezone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_token is not None:
            result['appToken'] = self.app_token

        if self.cron_expression is not None:
            result['cronExpression'] = self.cron_expression

        if self.directory_id is not None:
            result['directoryId'] = self.directory_id

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.expected_revision is not None:
            result['expectedRevision'] = self.expected_revision

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.timezone is not None:
            result['timezone'] = self.timezone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('cronExpression') is not None:
            self.cron_expression = m.get('cronExpression')

        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('expectedRevision') is not None:
            self.expected_revision = m.get('expectedRevision')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')

        return self

