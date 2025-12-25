# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeDefenseTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        templates: List[main_models.DescribeDefenseTemplatesResponseBodyTemplates] = None,
        total_count: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The protection templates.
        self.templates = templates
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.templates:
            for v1 in self.templates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Templates'] = []
        if self.templates is not None:
            for k1 in self.templates:
                result['Templates'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.templates = []
        if m.get('Templates') is not None:
            for k1 in m.get('Templates'):
                temp_model = main_models.DescribeDefenseTemplatesResponseBodyTemplates()
                self.templates.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDefenseTemplatesResponseBodyTemplates(DaraModel):
    def __init__(
        self,
        defense_scene: str = None,
        defense_sub_scene: str = None,
        description: str = None,
        gmt_modified: int = None,
        template_id: int = None,
        template_name: str = None,
        template_origin: str = None,
        template_status: int = None,
        template_type: str = None,
    ):
        # The scenario in which the protection template is used.
        # 
        # *   **waf_group**: basic protection.
        # *   **antiscan**: scan protection.
        # *   **ip_blacklist**: IP address blacklist.
        # *   **custom_acl**: custom rule.
        # *   **whitelist**: whitelist.
        # *   **region_block**: region blacklist.
        # *   **custom_response**: custom response.
        # *   **cc**: HTTP flood protection.
        # *   **tamperproof**: website tamper-proofing.
        # *   **dlp**: data leakage prevention.
        self.defense_scene = defense_scene
        # The sub-scenario in which the protection template is used. Valid values:
        # 
        # *   **web**: bot management for website protection.
        # *   **app**: bot management for app protection.
        # *   **basic**: bot management for basic protection.
        self.defense_sub_scene = defense_sub_scene
        # The description of the protection template.
        self.description = description
        # The time when the protection template was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.gmt_modified = gmt_modified
        # The ID of the protection template.
        self.template_id = template_id
        # The name of the protection template.
        self.template_name = template_name
        # The origin of the protection template. The value custom indicates that the protection template is a custom template created by the user.
        self.template_origin = template_origin
        # The status of the protection template. Valid values:
        # 
        # *   **0**: disabled.
        # *   **1**: enabled.
        self.template_status = template_status
        # The type of the protection template. Valid values:
        # 
        # *   **user_default**: default template.
        # *   **user_custom**: custom template.
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.defense_scene is not None:
            result['DefenseScene'] = self.defense_scene

        if self.defense_sub_scene is not None:
            result['DefenseSubScene'] = self.defense_sub_scene

        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_origin is not None:
            result['TemplateOrigin'] = self.template_origin

        if self.template_status is not None:
            result['TemplateStatus'] = self.template_status

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefenseScene') is not None:
            self.defense_scene = m.get('DefenseScene')

        if m.get('DefenseSubScene') is not None:
            self.defense_sub_scene = m.get('DefenseSubScene')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateOrigin') is not None:
            self.template_origin = m.get('TemplateOrigin')

        if m.get('TemplateStatus') is not None:
            self.template_status = m.get('TemplateStatus')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        return self

