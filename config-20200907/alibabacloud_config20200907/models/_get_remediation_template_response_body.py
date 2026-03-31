# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class GetRemediationTemplateResponseBody(DaraModel):
    def __init__(
        self,
        remediation_templates: List[main_models.GetRemediationTemplateResponseBodyRemediationTemplates] = None,
        request_id: str = None,
    ):
        # The information about the automatic remediation template.
        self.remediation_templates = remediation_templates
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.remediation_templates:
            for v1 in self.remediation_templates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RemediationTemplates'] = []
        if self.remediation_templates is not None:
            for k1 in self.remediation_templates:
                result['RemediationTemplates'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.remediation_templates = []
        if m.get('RemediationTemplates') is not None:
            for k1 in m.get('RemediationTemplates'):
                temp_model = main_models.GetRemediationTemplateResponseBodyRemediationTemplates()
                self.remediation_templates.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetRemediationTemplateResponseBodyRemediationTemplates(DaraModel):
    def __init__(
        self,
        managed_rule_identifier: str = None,
        remediation_type: str = None,
        template_definition: str = None,
        template_description: str = None,
        template_identifier: str = None,
        template_name: str = None,
    ):
        # The ID of the supported rule template.
        # 
        # This parameter is required.
        self.managed_rule_identifier = managed_rule_identifier
        # The type of the automatic remediation template. The value is set to OOS.
        self.remediation_type = remediation_type
        # The parameters of the automatic remediation template.
        self.template_definition = template_definition
        # The description of the automatic remediation template.
        # 
        # This parameter is required.
        self.template_description = template_description
        # The ID of the automatic remediation template.
        self.template_identifier = template_identifier
        # The name of the automatic remediation template.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.managed_rule_identifier is not None:
            result['ManagedRuleIdentifier'] = self.managed_rule_identifier

        if self.remediation_type is not None:
            result['RemediationType'] = self.remediation_type

        if self.template_definition is not None:
            result['TemplateDefinition'] = self.template_definition

        if self.template_description is not None:
            result['TemplateDescription'] = self.template_description

        if self.template_identifier is not None:
            result['TemplateIdentifier'] = self.template_identifier

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ManagedRuleIdentifier') is not None:
            self.managed_rule_identifier = m.get('ManagedRuleIdentifier')

        if m.get('RemediationType') is not None:
            self.remediation_type = m.get('RemediationType')

        if m.get('TemplateDefinition') is not None:
            self.template_definition = m.get('TemplateDefinition')

        if m.get('TemplateDescription') is not None:
            self.template_description = m.get('TemplateDescription')

        if m.get('TemplateIdentifier') is not None:
            self.template_identifier = m.get('TemplateIdentifier')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

