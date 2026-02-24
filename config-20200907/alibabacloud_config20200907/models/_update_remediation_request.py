# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateRemediationRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        invoke_type: str = None,
        params: str = None,
        remediation_id: str = None,
        remediation_template_id: str = None,
        remediation_type: str = None,
        source_type: str = None,
    ):
        # A client token that is used to ensure the idempotence of the request. Generate a token that is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The execution mode of the remediation. Valid values:
        # 
        # - NON_EXECUTION: The remediation is not executed.
        # 
        # - AUTO_EXECUTION: The remediation is automatically executed.
        # 
        # - MANUAL_EXECUTION: The remediation is manually executed.
        # 
        # - NOT_CONFIG: The execution mode is not specified.
        self.invoke_type = invoke_type
        # The parameters of the remediation setting.
        self.params = params
        # The ID of the remediation setting.
        # 
        # For more information about how to obtain the ID of a remediation setting, see [ListRemediations](https://help.aliyun.com/document_detail/270772.html).
        # 
        # This parameter is required.
        self.remediation_id = remediation_id
        # The ID of the remediation template.
        # 
        # For more information about how to obtain the ID of a remediation template, see [ListRemediationTemplates](https://help.aliyun.com/document_detail/270066.html).
        self.remediation_template_id = remediation_template_id
        # The type of the remediation. Valid values:
        # 
        # - OOS: Operation Orchestration Service (template-based remediation).
        # 
        # - FC: Function Compute (custom remediation).
        self.remediation_type = remediation_type
        # The source of the remediation. Valid values:
        # 
        # - ALIYUN: official remediation.
        # 
        # - CUSTOM: custom remediation.
        # 
        # - NONE: none.
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

        if self.invoke_type is not None:
            result['InvokeType'] = self.invoke_type

        if self.params is not None:
            result['Params'] = self.params

        if self.remediation_id is not None:
            result['RemediationId'] = self.remediation_id

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

        if m.get('InvokeType') is not None:
            self.invoke_type = m.get('InvokeType')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('RemediationId') is not None:
            self.remediation_id = m.get('RemediationId')

        if m.get('RemediationTemplateId') is not None:
            self.remediation_template_id = m.get('RemediationTemplateId')

        if m.get('RemediationType') is not None:
            self.remediation_type = m.get('RemediationType')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

