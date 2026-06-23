# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDataQualityRuleShrinkRequest(DaraModel):
    def __init__(
        self,
        checking_config_shrink: str = None,
        description: str = None,
        enabled: bool = None,
        error_handlers_shrink: str = None,
        name: str = None,
        project_id: int = None,
        sampling_config_shrink: str = None,
        severity: str = None,
        target_shrink: str = None,
        template_code: str = None,
    ):
        # The sample check settings.
        self.checking_config_shrink = checking_config_shrink
        # The description of the rule. The maximum length is 500 characters.
        self.description = description
        # Specifies whether to enable the data quality rule.
        self.enabled = enabled
        # The list of issue handlers for the data quality rule check.
        self.error_handlers_shrink = error_handlers_shrink
        # The name of the rule.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the DataWorks workspace.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The settings required for sample collection.
        self.sampling_config_shrink = sampling_config_shrink
        # The severity of the rule for the business (corresponding to the strong/weak rule on the page). Valid values:
        # - Normal
        # - High
        self.severity = severity
        # The object monitored by the rule.
        self.target_shrink = target_shrink
        # The unique identifier of the rule template that the rule references.
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

        if self.name is not None:
            result['Name'] = self.name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.sampling_config_shrink is not None:
            result['SamplingConfig'] = self.sampling_config_shrink

        if self.severity is not None:
            result['Severity'] = self.severity

        if self.target_shrink is not None:
            result['Target'] = self.target_shrink

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

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SamplingConfig') is not None:
            self.sampling_config_shrink = m.get('SamplingConfig')

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        if m.get('Target') is not None:
            self.target_shrink = m.get('Target')

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        return self

