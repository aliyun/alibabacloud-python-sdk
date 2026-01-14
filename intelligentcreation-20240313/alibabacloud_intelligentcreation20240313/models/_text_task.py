# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_intelligentcreation20240313 import models as main_models
from darabonba.model import DaraModel

class TextTask(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_name: str = None,
        content_requirement: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        introduction: str = None,
        nums: int = None,
        point: str = None,
        reference_tag: main_models.ReferenceTag = None,
        related_rag_ids: List[int] = None,
        style: str = None,
        target: str = None,
        text_ids: List[int] = None,
        text_mode_type: str = None,
        text_task_id: int = None,
        text_task_status: str = None,
        texts: List[main_models.Text] = None,
        theme: str = None,
        theme_desc: str = None,
    ):
        self.agent_id = agent_id
        self.agent_name = agent_name
        self.content_requirement = content_requirement
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.introduction = introduction
        # This parameter is required.
        self.nums = nums
        self.point = point
        self.reference_tag = reference_tag
        self.related_rag_ids = related_rag_ids
        # This parameter is required.
        self.style = style
        self.target = target
        self.text_ids = text_ids
        # This parameter is required.
        self.text_mode_type = text_mode_type
        self.text_task_id = text_task_id
        self.text_task_status = text_task_status
        self.texts = texts
        self.theme = theme
        self.theme_desc = theme_desc

    def validate(self):
        if self.reference_tag:
            self.reference_tag.validate()
        if self.texts:
            for v1 in self.texts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.agent_name is not None:
            result['agentName'] = self.agent_name

        if self.content_requirement is not None:
            result['contentRequirement'] = self.content_requirement

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.introduction is not None:
            result['introduction'] = self.introduction

        if self.nums is not None:
            result['nums'] = self.nums

        if self.point is not None:
            result['point'] = self.point

        if self.reference_tag is not None:
            result['referenceTag'] = self.reference_tag.to_map()

        if self.related_rag_ids is not None:
            result['relatedRagIds'] = self.related_rag_ids

        if self.style is not None:
            result['style'] = self.style

        if self.target is not None:
            result['target'] = self.target

        if self.text_ids is not None:
            result['textIds'] = self.text_ids

        if self.text_mode_type is not None:
            result['textModeType'] = self.text_mode_type

        if self.text_task_id is not None:
            result['textTaskId'] = self.text_task_id

        if self.text_task_status is not None:
            result['textTaskStatus'] = self.text_task_status

        result['texts'] = []
        if self.texts is not None:
            for k1 in self.texts:
                result['texts'].append(k1.to_map() if k1 else None)

        if self.theme is not None:
            result['theme'] = self.theme

        if self.theme_desc is not None:
            result['themeDesc'] = self.theme_desc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('agentName') is not None:
            self.agent_name = m.get('agentName')

        if m.get('contentRequirement') is not None:
            self.content_requirement = m.get('contentRequirement')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('introduction') is not None:
            self.introduction = m.get('introduction')

        if m.get('nums') is not None:
            self.nums = m.get('nums')

        if m.get('point') is not None:
            self.point = m.get('point')

        if m.get('referenceTag') is not None:
            temp_model = main_models.ReferenceTag()
            self.reference_tag = temp_model.from_map(m.get('referenceTag'))

        if m.get('relatedRagIds') is not None:
            self.related_rag_ids = m.get('relatedRagIds')

        if m.get('style') is not None:
            self.style = m.get('style')

        if m.get('target') is not None:
            self.target = m.get('target')

        if m.get('textIds') is not None:
            self.text_ids = m.get('textIds')

        if m.get('textModeType') is not None:
            self.text_mode_type = m.get('textModeType')

        if m.get('textTaskId') is not None:
            self.text_task_id = m.get('textTaskId')

        if m.get('textTaskStatus') is not None:
            self.text_task_status = m.get('textTaskStatus')

        self.texts = []
        if m.get('texts') is not None:
            for k1 in m.get('texts'):
                temp_model = main_models.Text()
                self.texts.append(temp_model.from_map(k1))

        if m.get('theme') is not None:
            self.theme = m.get('theme')

        if m.get('themeDesc') is not None:
            self.theme_desc = m.get('themeDesc')

        return self

