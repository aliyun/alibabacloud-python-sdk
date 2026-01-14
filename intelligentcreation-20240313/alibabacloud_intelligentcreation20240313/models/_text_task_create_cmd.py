# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_intelligentcreation20240313 import models as main_models
from darabonba.model import DaraModel

class TextTaskCreateCmd(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        content_requirement: str = None,
        idempotent_id: str = None,
        industry: str = None,
        introduction: str = None,
        number: int = None,
        point: str = None,
        reference_tag: main_models.ReferenceTag = None,
        related_rag_ids: List[int] = None,
        stream_api: bool = None,
        style: str = None,
        target: str = None,
        text_mode_type: str = None,
        theme: str = None,
        themes: List[str] = None,
    ):
        self.agent_id = agent_id
        self.content_requirement = content_requirement
        self.idempotent_id = idempotent_id
        self.industry = industry
        self.introduction = introduction
        # This parameter is required.
        self.number = number
        self.point = point
        self.reference_tag = reference_tag
        self.related_rag_ids = related_rag_ids
        self.stream_api = stream_api
        # This parameter is required.
        self.style = style
        self.target = target
        # This parameter is required.
        self.text_mode_type = text_mode_type
        self.theme = theme
        self.themes = themes

    def validate(self):
        if self.reference_tag:
            self.reference_tag.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.content_requirement is not None:
            result['contentRequirement'] = self.content_requirement

        if self.idempotent_id is not None:
            result['idempotentId'] = self.idempotent_id

        if self.industry is not None:
            result['industry'] = self.industry

        if self.introduction is not None:
            result['introduction'] = self.introduction

        if self.number is not None:
            result['number'] = self.number

        if self.point is not None:
            result['point'] = self.point

        if self.reference_tag is not None:
            result['referenceTag'] = self.reference_tag.to_map()

        if self.related_rag_ids is not None:
            result['relatedRagIds'] = self.related_rag_ids

        if self.stream_api is not None:
            result['streamApi'] = self.stream_api

        if self.style is not None:
            result['style'] = self.style

        if self.target is not None:
            result['target'] = self.target

        if self.text_mode_type is not None:
            result['textModeType'] = self.text_mode_type

        if self.theme is not None:
            result['theme'] = self.theme

        if self.themes is not None:
            result['themes'] = self.themes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('contentRequirement') is not None:
            self.content_requirement = m.get('contentRequirement')

        if m.get('idempotentId') is not None:
            self.idempotent_id = m.get('idempotentId')

        if m.get('industry') is not None:
            self.industry = m.get('industry')

        if m.get('introduction') is not None:
            self.introduction = m.get('introduction')

        if m.get('number') is not None:
            self.number = m.get('number')

        if m.get('point') is not None:
            self.point = m.get('point')

        if m.get('referenceTag') is not None:
            temp_model = main_models.ReferenceTag()
            self.reference_tag = temp_model.from_map(m.get('referenceTag'))

        if m.get('relatedRagIds') is not None:
            self.related_rag_ids = m.get('relatedRagIds')

        if m.get('streamApi') is not None:
            self.stream_api = m.get('streamApi')

        if m.get('style') is not None:
            self.style = m.get('style')

        if m.get('target') is not None:
            self.target = m.get('target')

        if m.get('textModeType') is not None:
            self.text_mode_type = m.get('textModeType')

        if m.get('theme') is not None:
            self.theme = m.get('theme')

        if m.get('themes') is not None:
            self.themes = m.get('themes')

        return self

