# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class ListRemediationTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        remediation_templates: List[main_models.ListRemediationTemplatesResponseBodyRemediationTemplates] = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The page number. Pages start from page 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 100.
        self.page_size = page_size
        # The queried remediation templates.
        self.remediation_templates = remediation_templates
        # The ID of the request.
        self.request_id = request_id
        # The total number of remediation templates.
        self.total_count = total_count

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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['RemediationTemplates'] = []
        if self.remediation_templates is not None:
            for k1 in self.remediation_templates:
                result['RemediationTemplates'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.remediation_templates = []
        if m.get('RemediationTemplates') is not None:
            for k1 in m.get('RemediationTemplates'):
                temp_model = main_models.ListRemediationTemplatesResponseBodyRemediationTemplates()
                self.remediation_templates.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListRemediationTemplatesResponseBodyRemediationTemplates(DaraModel):
    def __init__(
        self,
        remediation_type: str = None,
        template_definition: str = None,
        template_description: str = None,
        template_identifier: str = None,
        template_name: str = None,
    ):
        # The type of the remediation template. Valid value: OOS, which indicates Operation Orchestration Service.
        self.remediation_type = remediation_type
        # The definition of the remediation template.
        self.template_definition = template_definition
        # The description of the remediation template.
        self.template_description = template_description
        # The ID of the remediation template.
        self.template_identifier = template_identifier
        # The name of the remediation template.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

