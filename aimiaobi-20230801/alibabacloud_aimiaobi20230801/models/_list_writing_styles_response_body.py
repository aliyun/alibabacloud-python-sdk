# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class ListWritingStylesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListWritingStylesResponseBodyData] = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: str = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.message is not None:
            result['Message'] = self.message

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListWritingStylesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListWritingStylesResponseBodyData(DaraModel):
    def __init__(
        self,
        distribute_step_template_define: main_models.WritingStyleTemplateDefine = None,
        distribute_writing: bool = None,
        emoji: str = None,
        style_description: str = None,
        style_image: str = None,
        style_key: str = None,
        style_name: str = None,
        template_define: main_models.WritingStyleTemplateDefine = None,
    ):
        self.distribute_step_template_define = distribute_step_template_define
        self.distribute_writing = distribute_writing
        self.emoji = emoji
        self.style_description = style_description
        self.style_image = style_image
        self.style_key = style_key
        self.style_name = style_name
        self.template_define = template_define

    def validate(self):
        if self.distribute_step_template_define:
            self.distribute_step_template_define.validate()
        if self.template_define:
            self.template_define.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.distribute_step_template_define is not None:
            result['DistributeStepTemplateDefine'] = self.distribute_step_template_define.to_map()

        if self.distribute_writing is not None:
            result['DistributeWriting'] = self.distribute_writing

        if self.emoji is not None:
            result['Emoji'] = self.emoji

        if self.style_description is not None:
            result['StyleDescription'] = self.style_description

        if self.style_image is not None:
            result['StyleImage'] = self.style_image

        if self.style_key is not None:
            result['StyleKey'] = self.style_key

        if self.style_name is not None:
            result['StyleName'] = self.style_name

        if self.template_define is not None:
            result['TemplateDefine'] = self.template_define.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistributeStepTemplateDefine') is not None:
            temp_model = main_models.WritingStyleTemplateDefine()
            self.distribute_step_template_define = temp_model.from_map(m.get('DistributeStepTemplateDefine'))

        if m.get('DistributeWriting') is not None:
            self.distribute_writing = m.get('DistributeWriting')

        if m.get('Emoji') is not None:
            self.emoji = m.get('Emoji')

        if m.get('StyleDescription') is not None:
            self.style_description = m.get('StyleDescription')

        if m.get('StyleImage') is not None:
            self.style_image = m.get('StyleImage')

        if m.get('StyleKey') is not None:
            self.style_key = m.get('StyleKey')

        if m.get('StyleName') is not None:
            self.style_name = m.get('StyleName')

        if m.get('TemplateDefine') is not None:
            temp_model = main_models.WritingStyleTemplateDefine()
            self.template_define = temp_model.from_map(m.get('TemplateDefine'))

        return self

