# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class DescribeRemediationResponseBody(DaraModel):
    def __init__(
        self,
        remediation: main_models.DescribeRemediationResponseBodyRemediation = None,
        request_id: str = None,
    ):
        # The details of the remediation configuration.
        self.remediation = remediation
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.remediation:
            self.remediation.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.remediation is not None:
            result['Remediation'] = self.remediation.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Remediation') is not None:
            temp_model = main_models.DescribeRemediationResponseBodyRemediation()
            self.remediation = temp_model.from_map(m.get('Remediation'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeRemediationResponseBodyRemediation(DaraModel):
    def __init__(
        self,
        account_id: int = None,
        config_rule_id: str = None,
        invoke_type: str = None,
        last_successful_invocation_id: str = None,
        last_successful_invocation_time: int = None,
        last_successful_invocation_type: str = None,
        remediation_id: str = None,
        remediation_origin_params: str = None,
        remediation_source_type: str = None,
        remediation_template_id: str = None,
        remediation_type: str = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.account_id = account_id
        # The rule ID.
        self.config_rule_id = config_rule_id
        # The execution mode of the remediation template. Valid values:
        # 
        # *   NON_EXECUTION: The remediation template was not executed.
        # *   AUTO_EXECUTION: The remediation template was automatically executed.
        # *   MANUAL_EXECUTION: The remediation template was manually executed.
        # *   NOT_CONFIG: The execution mode was not specified.
        self.invoke_type = invoke_type
        # The record ID of the last successful execution of the remediation template.
        self.last_successful_invocation_id = last_successful_invocation_id
        # The timestamp of the last successful execution of the remediation template. Unit: milliseconds.
        self.last_successful_invocation_time = last_successful_invocation_time
        # The mode of the last successful execution of the remediation template. Valid values:
        # 
        # *   NON_EXECUTION: The remediation template was not executed.
        # *   AUTO_EXECUTION: The remediation template was automatically executed.
        # *   MANUAL_EXECUTION: The remediation template was manually executed.
        # *   NOT_CONFIG: The execution mode was not specified.
        self.last_successful_invocation_type = last_successful_invocation_type
        # The ID of the remediation configuration.
        self.remediation_id = remediation_id
        # The converted configuration of the remediation template. This parameter is returned only for an OOS remediation template.
        # 
        # This parameter is required.
        self.remediation_origin_params = remediation_origin_params
        # The source of the remediation template. Valid values:
        # 
        # *   ALIYUN: official template
        # *   CUSTOM: custom template
        # *   NONE: none
        self.remediation_source_type = remediation_source_type
        # The ID of the remediation template.
        self.remediation_template_id = remediation_template_id
        # The type of the remediation template. Valid values:
        # 
        # *   OOS: Operation Orchestration Service (official remediation)
        # *   FC: Function Compute (custom remediation)
        self.remediation_type = remediation_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id

        if self.invoke_type is not None:
            result['InvokeType'] = self.invoke_type

        if self.last_successful_invocation_id is not None:
            result['LastSuccessfulInvocationId'] = self.last_successful_invocation_id

        if self.last_successful_invocation_time is not None:
            result['LastSuccessfulInvocationTime'] = self.last_successful_invocation_time

        if self.last_successful_invocation_type is not None:
            result['LastSuccessfulInvocationType'] = self.last_successful_invocation_type

        if self.remediation_id is not None:
            result['RemediationId'] = self.remediation_id

        if self.remediation_origin_params is not None:
            result['RemediationOriginParams'] = self.remediation_origin_params

        if self.remediation_source_type is not None:
            result['RemediationSourceType'] = self.remediation_source_type

        if self.remediation_template_id is not None:
            result['RemediationTemplateId'] = self.remediation_template_id

        if self.remediation_type is not None:
            result['RemediationType'] = self.remediation_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')

        if m.get('InvokeType') is not None:
            self.invoke_type = m.get('InvokeType')

        if m.get('LastSuccessfulInvocationId') is not None:
            self.last_successful_invocation_id = m.get('LastSuccessfulInvocationId')

        if m.get('LastSuccessfulInvocationTime') is not None:
            self.last_successful_invocation_time = m.get('LastSuccessfulInvocationTime')

        if m.get('LastSuccessfulInvocationType') is not None:
            self.last_successful_invocation_type = m.get('LastSuccessfulInvocationType')

        if m.get('RemediationId') is not None:
            self.remediation_id = m.get('RemediationId')

        if m.get('RemediationOriginParams') is not None:
            self.remediation_origin_params = m.get('RemediationOriginParams')

        if m.get('RemediationSourceType') is not None:
            self.remediation_source_type = m.get('RemediationSourceType')

        if m.get('RemediationTemplateId') is not None:
            self.remediation_template_id = m.get('RemediationTemplateId')

        if m.get('RemediationType') is not None:
            self.remediation_type = m.get('RemediationType')

        return self

