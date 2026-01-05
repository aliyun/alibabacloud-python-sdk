# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDataQualityRuleShrinkRequest(DaraModel):
    def __init__(
        self,
        checking_config_shrink: str = None,
        description: str = None,
        enabled: bool = None,
        error_handlers_shrink: str = None,
        id: int = None,
        name: str = None,
        project_id: int = None,
        sampling_config_shrink: str = None,
        severity: str = None,
        template_code: str = None,
    ):
        # The check settings for sample data.
        self.checking_config_shrink = checking_config_shrink
        # The description of the rule. The description can be up to 500 characters in length.
        self.description = description
        # Specifies whether to enable the rule.
        self.enabled = enabled
        # The operations that you can perform after the rule-based check fails.
        self.error_handlers_shrink = error_handlers_shrink
        # The rule ID.
        # 
        # This parameter is required.
        self.id = id
        # The name of the rule. The name can be up to 255 characters in length and can contain digits, letters, and punctuation marks.
        self.name = name
        # This parameter is required.
        self.project_id = project_id
        # The sampling settings.
        self.sampling_config_shrink = sampling_config_shrink
        # The strength of the rule. Valid values:
        # 
        # *   Normal
        # *   High
        self.severity = severity
        # The ID of the template used by the rule.
        self.template_code = template_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.checking_config_shrink is not None:
            result['CheckingConfig'] = self.checking_config_shrink

        if self.description is not None:
            result['Description'] = self.description

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.error_handlers_shrink is not None:
            result['ErrorHandlers'] = self.error_handlers_shrink

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.sampling_config_shrink is not None:
            result['SamplingConfig'] = self.sampling_config_shrink

        if self.severity is not None:
            result['Severity'] = self.severity

        if self.template_code is not None:
            result['TemplateCode'] = self.template_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckingConfig') is not None:
            self.checking_config_shrink = m.get('CheckingConfig')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('ErrorHandlers') is not None:
            self.error_handlers_shrink = m.get('ErrorHandlers')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SamplingConfig') is not None:
            self.sampling_config_shrink = m.get('SamplingConfig')

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        return self

