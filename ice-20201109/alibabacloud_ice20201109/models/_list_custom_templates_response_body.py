# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class ListCustomTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        custom_template_list: List[main_models.ListCustomTemplatesResponseBodyCustomTemplateList] = None,
        request_id: str = None,
        total: int = None,
    ):
        # The queried templates.
        self.custom_template_list = custom_template_list
        # The request ID.
        self.request_id = request_id
        # The total number of templates.
        self.total = total

    def validate(self):
        if self.custom_template_list:
            for v1 in self.custom_template_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CustomTemplateList'] = []
        if self.custom_template_list is not None:
            for k1 in self.custom_template_list:
                result['CustomTemplateList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_template_list = []
        if m.get('CustomTemplateList') is not None:
            for k1 in m.get('CustomTemplateList'):
                temp_model = main_models.ListCustomTemplatesResponseBodyCustomTemplateList()
                self.custom_template_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListCustomTemplatesResponseBodyCustomTemplateList(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        frontend_hint: main_models.ListCustomTemplatesResponseBodyCustomTemplateListFrontendHint = None,
        is_default: bool = None,
        modified_time: str = None,
        status: str = None,
        subtype: int = None,
        subtype_name: str = None,
        template_config: str = None,
        template_id: str = None,
        template_name: str = None,
        type: int = None,
        type_name: str = None,
    ):
        # The time when the template was created.
        self.create_time = create_time
        self.frontend_hint = frontend_hint
        # Indicates whether the template is the default template.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.is_default = is_default
        # The time when the template was last modified.
        self.modified_time = modified_time
        # The template state.
        # 
        # Valid values:
        # 
        # *   Normal
        self.status = status
        # The subtype ID of the template.
        self.subtype = subtype
        # The subtype name of the template.
        self.subtype_name = subtype_name
        # The template parameters.
        self.template_config = template_config
        # The template ID.
        self.template_id = template_id
        # The template name.
        self.template_name = template_name
        # The type ID of the template.
        self.type = type
        # The type name of the template.
        self.type_name = type_name

    def validate(self):
        if self.frontend_hint:
            self.frontend_hint.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.frontend_hint is not None:
            result['FrontendHint'] = self.frontend_hint.to_map()

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.status is not None:
            result['Status'] = self.status

        if self.subtype is not None:
            result['Subtype'] = self.subtype

        if self.subtype_name is not None:
            result['SubtypeName'] = self.subtype_name

        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.type is not None:
            result['Type'] = self.type

        if self.type_name is not None:
            result['TypeName'] = self.type_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('FrontendHint') is not None:
            temp_model = main_models.ListCustomTemplatesResponseBodyCustomTemplateListFrontendHint()
            self.frontend_hint = temp_model.from_map(m.get('FrontendHint'))

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Subtype') is not None:
            self.subtype = m.get('Subtype')

        if m.get('SubtypeName') is not None:
            self.subtype_name = m.get('SubtypeName')

        if m.get('TemplateConfig') is not None:
            self.template_config = m.get('TemplateConfig')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')

        return self

class ListCustomTemplatesResponseBodyCustomTemplateListFrontendHint(DaraModel):
    def __init__(
        self,
        transcode_template_hint: main_models.ListCustomTemplatesResponseBodyCustomTemplateListFrontendHintTranscodeTemplateHint = None,
    ):
        self.transcode_template_hint = transcode_template_hint

    def validate(self):
        if self.transcode_template_hint:
            self.transcode_template_hint.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.transcode_template_hint is not None:
            result['TranscodeTemplateHint'] = self.transcode_template_hint.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TranscodeTemplateHint') is not None:
            temp_model = main_models.ListCustomTemplatesResponseBodyCustomTemplateListFrontendHintTranscodeTemplateHint()
            self.transcode_template_hint = temp_model.from_map(m.get('TranscodeTemplateHint'))

        return self

class ListCustomTemplatesResponseBodyCustomTemplateListFrontendHintTranscodeTemplateHint(DaraModel):
    def __init__(
        self,
        bitrate_control_type: str = None,
    ):
        self.bitrate_control_type = bitrate_control_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bitrate_control_type is not None:
            result['BitrateControlType'] = self.bitrate_control_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BitrateControlType') is not None:
            self.bitrate_control_type = m.get('BitrateControlType')

        return self

