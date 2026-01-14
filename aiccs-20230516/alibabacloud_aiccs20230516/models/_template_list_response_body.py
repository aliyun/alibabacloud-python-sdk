# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_aiccs20230516 import models as main_models
from darabonba.model import DaraModel

class TemplateListResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        model: List[main_models.TemplateListResponseBodyModel] = None,
        request_id: str = None,
        success: bool = None,
        timestamp: int = None,
    ):
        self.code = code
        self.message = message
        self.model = model
        self.request_id = request_id
        self.success = success
        self.timestamp = timestamp

    def validate(self):
        if self.model:
            for v1 in self.model:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        result['Model'] = []
        if self.model is not None:
            for k1 in self.model:
                result['Model'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        self.model = []
        if m.get('Model') is not None:
            for k1 in m.get('Model'):
                temp_model = main_models.TemplateListResponseBodyModel()
                self.model.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

class TemplateListResponseBodyModel(DaraModel):
    def __init__(
        self,
        intent_tags: List[Dict[str, Any]] = None,
        personality_tags: List[str] = None,
        properties: str = None,
        template_id: int = None,
        template_name: str = None,
        template_type: int = None,
    ):
        # 意向标签
        self.intent_tags = intent_tags
        # 个性标签
        self.personality_tags = personality_tags
        # 话术所需参数
        self.properties = properties
        # AI话术ID
        self.template_id = template_id
        # 话术模板名称
        self.template_name = template_name
        # 模板类型
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.intent_tags is not None:
            result['IntentTags'] = self.intent_tags

        if self.personality_tags is not None:
            result['PersonalityTags'] = self.personality_tags

        if self.properties is not None:
            result['Properties'] = self.properties

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntentTags') is not None:
            self.intent_tags = m.get('IntentTags')

        if m.get('PersonalityTags') is not None:
            self.personality_tags = m.get('PersonalityTags')

        if m.get('Properties') is not None:
            self.properties = m.get('Properties')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        return self

