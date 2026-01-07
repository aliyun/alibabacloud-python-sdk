# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quanmiaolightapp20240801 import models as main_models
from darabonba.model import DaraModel

class RunHotTopicSummaryRequest(DaraModel):
    def __init__(
        self,
        hot_topic_version: str = None,
        step_for_custom_summary_style_config: main_models.RunHotTopicSummaryRequestStepForCustomSummaryStyleConfig = None,
        topic_ids: List[str] = None,
    ):
        # This parameter is required.
        self.hot_topic_version = hot_topic_version
        # This parameter is required.
        self.step_for_custom_summary_style_config = step_for_custom_summary_style_config
        # This parameter is required.
        self.topic_ids = topic_ids

    def validate(self):
        if self.step_for_custom_summary_style_config:
            self.step_for_custom_summary_style_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hot_topic_version is not None:
            result['hotTopicVersion'] = self.hot_topic_version

        if self.step_for_custom_summary_style_config is not None:
            result['stepForCustomSummaryStyleConfig'] = self.step_for_custom_summary_style_config.to_map()

        if self.topic_ids is not None:
            result['topicIds'] = self.topic_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hotTopicVersion') is not None:
            self.hot_topic_version = m.get('hotTopicVersion')

        if m.get('stepForCustomSummaryStyleConfig') is not None:
            temp_model = main_models.RunHotTopicSummaryRequestStepForCustomSummaryStyleConfig()
            self.step_for_custom_summary_style_config = temp_model.from_map(m.get('stepForCustomSummaryStyleConfig'))

        if m.get('topicIds') is not None:
            self.topic_ids = m.get('topicIds')

        return self

class RunHotTopicSummaryRequestStepForCustomSummaryStyleConfig(DaraModel):
    def __init__(
        self,
        summary_image_count: int = None,
        summary_model: str = None,
        summary_prompt: str = None,
    ):
        self.summary_image_count = summary_image_count
        self.summary_model = summary_model
        self.summary_prompt = summary_prompt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.summary_image_count is not None:
            result['summaryImageCount'] = self.summary_image_count

        if self.summary_model is not None:
            result['summaryModel'] = self.summary_model

        if self.summary_prompt is not None:
            result['summaryPrompt'] = self.summary_prompt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('summaryImageCount') is not None:
            self.summary_image_count = m.get('summaryImageCount')

        if m.get('summaryModel') is not None:
            self.summary_model = m.get('summaryModel')

        if m.get('summaryPrompt') is not None:
            self.summary_prompt = m.get('summaryPrompt')

        return self

