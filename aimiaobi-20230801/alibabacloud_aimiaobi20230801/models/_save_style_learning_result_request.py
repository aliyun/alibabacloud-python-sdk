# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SaveStyleLearningResultRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        aigc_result: str = None,
        custom_text_id_list: List[int] = None,
        material_id_list: List[int] = None,
        rewrite_result: str = None,
        style_name: str = None,
        task_id: str = None,
    ):
        self.agent_key = agent_key
        self.aigc_result = aigc_result
        self.custom_text_id_list = custom_text_id_list
        self.material_id_list = material_id_list
        self.rewrite_result = rewrite_result
        self.style_name = style_name
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.aigc_result is not None:
            result['AigcResult'] = self.aigc_result

        if self.custom_text_id_list is not None:
            result['CustomTextIdList'] = self.custom_text_id_list

        if self.material_id_list is not None:
            result['MaterialIdList'] = self.material_id_list

        if self.rewrite_result is not None:
            result['RewriteResult'] = self.rewrite_result

        if self.style_name is not None:
            result['StyleName'] = self.style_name

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('AigcResult') is not None:
            self.aigc_result = m.get('AigcResult')

        if m.get('CustomTextIdList') is not None:
            self.custom_text_id_list = m.get('CustomTextIdList')

        if m.get('MaterialIdList') is not None:
            self.material_id_list = m.get('MaterialIdList')

        if m.get('RewriteResult') is not None:
            self.rewrite_result = m.get('RewriteResult')

        if m.get('StyleName') is not None:
            self.style_name = m.get('StyleName')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

