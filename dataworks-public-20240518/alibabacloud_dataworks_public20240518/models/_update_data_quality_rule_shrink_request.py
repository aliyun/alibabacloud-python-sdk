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
        # The sample verification settings.
        self.checking_config_shrink = checking_config_shrink
        # The rule description. The maximum length is 500 characters.
        self.description = description
        # Specifies whether the rule is enabled.
        self.enabled = enabled
        # The list of issue handlers for data quality rule verification.
        self.error_handlers_shrink = error_handlers_shrink
        # The rule ID.
        # 
        # This parameter is required.
        self.id = id
        # The rule name. The name can be a combination of digits, English letters, Chinese characters, and half-width or full-width punctuation. The maximum length is 255 characters.
        self.name = name
        # The ID of the DataWorks workspace. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace Settings page to obtain the workspace ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The settings required for sample collection.
        self.sampling_config_shrink = sampling_config_shrink
        # The severity level of the rule for the business (corresponding to strong/weak rules on the page). Valid values:
        # - Normal
        # - High
        self.severity = severity
        # The unique identifier of the rule template referenced by the rule.
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

