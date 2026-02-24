# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRemediationRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        config_rule_id: str = None,
        invoke_type: str = None,
        params: str = None,
        remediation_template_id: str = None,
        remediation_type: str = None,
        source_type: str = None,
    ):
        # A client token to ensure the idempotence of the request. The token must be unique for each request. The `ClientToken` parameter contains only ASCII characters and must not exceed 64 characters in length.
        self.client_token = client_token
        # The rule ID.
        # 
        # For more information, see [ListConfigRules](https://help.aliyun.com/document_detail/169607.html).
        # 
        # This parameter is required.
        self.config_rule_id = config_rule_id
        # The execution mode of the remediation. Valid values:
        # 
        # - NON_EXECUTION: The remediation is not executed.
        # 
        # - AUTO_EXECUTION: The remediation is automatically executed.
        # 
        # - MANUAL_EXECUTION: The remediation is manually executed.
        # 
        # - NOT_CONFIG: The execution mode is not set.
        # 
        # This parameter is required.
        self.invoke_type = invoke_type
        # The remediation parameters.
        # 
        # For more information, see the `TemplateDefinition` parameter in [ListRemediationTemplates](https://help.aliyun.com/document_detail/416781.html).
        # 
        # This parameter is required.
        self.params = params
        # The ID of the remediation template.
        # 
        # - If `RemediationType` is set to `OOS`, set this parameter to `ACS-OSS-PutBucketAcl`. For more information, see [ListRemediationTemplates](https://help.aliyun.com/document_detail/416781.html).
        # 
        # - If `RemediationType` is set to `FC`, set this parameter to the Alibaba Cloud Resource Name (ARN) of the function in Function Compute. Example: `acs:fc:cn-hangzhou:100931896542****:services/ConfigService.LATEST/functions/test-php`.
        # 
        # This parameter is required.
        self.remediation_template_id = remediation_template_id
        # The type of the remediation. Valid values:
        # 
        # - OOS: template-based remediation using OOS.
        # 
        # - FC: custom remediation using FC.
        # 
        # This parameter is required.
        self.remediation_type = remediation_type
        # The source of the remediation template. Valid values:
        # 
        # - ALIYUN (default): an official template.
        # 
        # - CUSTOM: a custom template. This value is required for custom FC remediations.
        # 
        # - NONE: no source.
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id

        if self.invoke_type is not None:
            result['InvokeType'] = self.invoke_type

        if self.params is not None:
            result['Params'] = self.params

        if self.remediation_template_id is not None:
            result['RemediationTemplateId'] = self.remediation_template_id

        if self.remediation_type is not None:
            result['RemediationType'] = self.remediation_type

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')

        if m.get('InvokeType') is not None:
            self.invoke_type = m.get('InvokeType')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('RemediationTemplateId') is not None:
            self.remediation_template_id = m.get('RemediationTemplateId')

        if m.get('RemediationType') is not None:
            self.remediation_type = m.get('RemediationType')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

