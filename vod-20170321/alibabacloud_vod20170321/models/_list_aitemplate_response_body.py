# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class ListAITemplateResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        template_info_list: List[main_models.ListAITemplateResponseBodyTemplateInfoList] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information about the AI templates.
        self.template_info_list = template_info_list

    def validate(self):
        if self.template_info_list:
            for v1 in self.template_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TemplateInfoList'] = []
        if self.template_info_list is not None:
            for k1 in self.template_info_list:
                result['TemplateInfoList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.template_info_list = []
        if m.get('TemplateInfoList') is not None:
            for k1 in m.get('TemplateInfoList'):
                temp_model = main_models.ListAITemplateResponseBodyTemplateInfoList()
                self.template_info_list.append(temp_model.from_map(k1))

        return self

class ListAITemplateResponseBodyTemplateInfoList(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        is_default: str = None,
        modify_time: str = None,
        source: str = None,
        template_config: str = None,
        template_id: str = None,
        template_name: str = None,
        template_type: str = None,
    ):
        # The time when the AI template was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.creation_time = creation_time
        # Indicates whether the template is the default AI template. Valid values:
        # 
        # *   **Default**
        # *   **NotDefault**
        self.is_default = is_default
        # The time when the AI template was modified. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.modify_time = modify_time
        # The source of the AI template. Valid values:
        # 
        # *   **System**
        # *   **Custom**
        self.source = source
        # The detailed configurations of the AI template. The value is a JSON string. For more information, see [AITemplateConfig](~~89863#title-vd3-499-o36~~).
        self.template_config = template_config
        # The ID of the AI template.
        self.template_id = template_id
        # The name of the AI template.
        self.template_name = template_name
        # The type of the AI template. Valid values:
        # 
        # *   **AIMediaAudit**: automated review
        # *   **AIImage**: smart thumbnail
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.source is not None:
            result['Source'] = self.source

        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('TemplateConfig') is not None:
            self.template_config = m.get('TemplateConfig')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        return self

