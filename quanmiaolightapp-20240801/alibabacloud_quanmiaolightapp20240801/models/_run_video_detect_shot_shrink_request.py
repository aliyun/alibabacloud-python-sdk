# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunVideoDetectShotShrinkRequest(DaraModel):
    def __init__(
        self,
        intelli_simp_prompt: str = None,
        intelli_simp_prompt_template_id: str = None,
        language: str = None,
        model_custom_prompt_template_id: str = None,
        model_id: str = None,
        model_vl_custom_prompt_template_id: str = None,
        options_shrink: str = None,
        original_session_id: str = None,
        pre_model_id: str = None,
        prompt: str = None,
        recognition_options_shrink: str = None,
        task_id: str = None,
        video_url: str = None,
        vl_prompt: str = None,
    ):
        self.intelli_simp_prompt = intelli_simp_prompt
        self.intelli_simp_prompt_template_id = intelli_simp_prompt_template_id
        self.language = language
        self.model_custom_prompt_template_id = model_custom_prompt_template_id
        self.model_id = model_id
        self.model_vl_custom_prompt_template_id = model_vl_custom_prompt_template_id
        # This parameter is required.
        self.options_shrink = options_shrink
        self.original_session_id = original_session_id
        self.pre_model_id = pre_model_id
        self.prompt = prompt
        # This parameter is required.
        self.recognition_options_shrink = recognition_options_shrink
        self.task_id = task_id
        # This parameter is required.
        self.video_url = video_url
        self.vl_prompt = vl_prompt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.intelli_simp_prompt is not None:
            result['intelliSimpPrompt'] = self.intelli_simp_prompt

        if self.intelli_simp_prompt_template_id is not None:
            result['intelliSimpPromptTemplateId'] = self.intelli_simp_prompt_template_id

        if self.language is not None:
            result['language'] = self.language

        if self.model_custom_prompt_template_id is not None:
            result['modelCustomPromptTemplateId'] = self.model_custom_prompt_template_id

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.model_vl_custom_prompt_template_id is not None:
            result['modelVlCustomPromptTemplateId'] = self.model_vl_custom_prompt_template_id

        if self.options_shrink is not None:
            result['options'] = self.options_shrink

        if self.original_session_id is not None:
            result['originalSessionId'] = self.original_session_id

        if self.pre_model_id is not None:
            result['preModelId'] = self.pre_model_id

        if self.prompt is not None:
            result['prompt'] = self.prompt

        if self.recognition_options_shrink is not None:
            result['recognitionOptions'] = self.recognition_options_shrink

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.video_url is not None:
            result['videoUrl'] = self.video_url

        if self.vl_prompt is not None:
            result['vlPrompt'] = self.vl_prompt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('intelliSimpPrompt') is not None:
            self.intelli_simp_prompt = m.get('intelliSimpPrompt')

        if m.get('intelliSimpPromptTemplateId') is not None:
            self.intelli_simp_prompt_template_id = m.get('intelliSimpPromptTemplateId')

        if m.get('language') is not None:
            self.language = m.get('language')

        if m.get('modelCustomPromptTemplateId') is not None:
            self.model_custom_prompt_template_id = m.get('modelCustomPromptTemplateId')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('modelVlCustomPromptTemplateId') is not None:
            self.model_vl_custom_prompt_template_id = m.get('modelVlCustomPromptTemplateId')

        if m.get('options') is not None:
            self.options_shrink = m.get('options')

        if m.get('originalSessionId') is not None:
            self.original_session_id = m.get('originalSessionId')

        if m.get('preModelId') is not None:
            self.pre_model_id = m.get('preModelId')

        if m.get('prompt') is not None:
            self.prompt = m.get('prompt')

        if m.get('recognitionOptions') is not None:
            self.recognition_options_shrink = m.get('recognitionOptions')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('videoUrl') is not None:
            self.video_url = m.get('videoUrl')

        if m.get('vlPrompt') is not None:
            self.vl_prompt = m.get('vlPrompt')

        return self

