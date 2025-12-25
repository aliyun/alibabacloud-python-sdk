# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeDefenseTemplateResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        template: main_models.DescribeDefenseTemplateResponseBodyTemplate = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information about the template.
        self.template = template

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.template is not None:
            result['Template'] = self.template.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Template') is not None:
            temp_model = main_models.DescribeDefenseTemplateResponseBodyTemplate()
            self.template = temp_model.from_map(m.get('Template'))

        return self

class DescribeDefenseTemplateResponseBodyTemplate(DaraModel):
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
        # The scenario in which the template is used. For more information, see the description of the **DefenseScene** parameter in the [CreateDefenseRule](~~CreateDefenseRule~~) topic.
        self.defense_scene = defense_scene
        # The sub-scenario in which the template is used. Valid values:
        # 
        # *   **web**: The template is a bot management template that is used for website protection.
        # *   **app**: The template is a bot management template that is used for app protection.
        # *   **basic**: The template is a bot management template that is used for basic protection.
        self.defense_sub_scene = defense_sub_scene
        # The description of the protection rule template.
        self.description = description
        # The most recent time when the protection rule template was modified.
        self.gmt_modified = gmt_modified
        # The ID of the protection rule template.
        self.template_id = template_id
        # The name of the protection rule template.
        self.template_name = template_name
        # The origin of the protection rule template. If the value of this parameter is custom, the protection rule template is created by the user.
        self.template_origin = template_origin
        # The status of the protection rule template. Valid values:
        # 
        # *   **0:** disabled.
        # *   **1:** enabled.
        self.template_status = template_status
        # The type of the protection rule template. Valid values:
        # 
        # *   **user_default:** default template.
        # *   **user_custom:** custom template.
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

