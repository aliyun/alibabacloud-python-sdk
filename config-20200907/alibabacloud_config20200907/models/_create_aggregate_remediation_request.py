# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAggregateRemediationRequest(DaraModel):
    def __init__(
        self,
        aggregator_id: str = None,
        client_token: str = None,
        config_rule_id: str = None,
        invoke_type: str = None,
        params: str = None,
        remediation_template_id: str = None,
        remediation_type: str = None,
        source_type: str = None,
    ):
        # The ID of the account group.
        # 
        # For more information about how to obtain the ID of the account group, see [ListAggregators](https://help.aliyun.com/document_detail/255797.html).
        # 
        # This parameter is required.
        self.aggregator_id = aggregator_id
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The `token` can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The rule ID.
        # 
        # For more information about how to obtain the ID of a rule, see [ListAggregateConfigRules](https://help.aliyun.com/document_detail/264148.html).
        # 
        # This parameter is required.
        self.config_rule_id = config_rule_id
        # The execution mode of the remediation template. Valid values:
        # 
        # *   NON_EXECUTION: The remediation template is not executed.
        # *   AUTO_EXECUTION: The remediation template is automatically executed.
        # *   MANUAL_EXECUTION: The remediation template is manually executed.
        # *   NOT_CONFIG: The execution mode is not specified.
        # 
        # This parameter is required.
        self.invoke_type = invoke_type
        # The configuration of the remediation template.
        # 
        # For more information about how to obtain the configuration of the remediation template, see [ListRemediationTemplates](https://help.aliyun.com/document_detail/416781.html). You can view the `TemplateDefinition` response parameter to obtain the configuration of the remediation template.
        # 
        # This parameter is required.
        self.params = params
        # The ID of the remediation template.
        # 
        # *   If you set the `RemediationType` parameter to `OOS`, set this parameter to the identifier of the relevant official remediation template, such as `ACS-OSS-PutBucketAcl`. For more information about how to obtain the remediation template identifier, see [ListRemediationTemplates](https://help.aliyun.com/document_detail/416781.html).
        # *   If you set the `RemediationType` parameter to `FC`, set this parameter to the Alibaba Cloud Resource Name (ARN) of the relevant Function Compute resource, such as `acs:fc:cn-hangzhou:100931896542****:services/ConfigService.LATEST/functions/test-php`.
        # 
        # This parameter is required.
        self.remediation_template_id = remediation_template_id
        # The type of the remediation template. Valid values:
        # 
        # *   OOS: stands for Operation Orchestration Service and indicates official remediation.
        # *   FC: stands for Function Compute and indicates custom remediation.
        # 
        # This parameter is required.
        self.remediation_type = remediation_type
        # The source of remediation template. Valid values:
        # 
        # *   ALIYUN (default): official template.
        # *   CUSTOM: custom template.
        # *   NONE: none.
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id

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
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')

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

