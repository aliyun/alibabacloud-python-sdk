# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class GetHotTopicBroadcastRequest(DaraModel):
    def __init__(
        self,
        calc_total_token: bool = None,
        category: str = None,
        current: int = None,
        hot_topic_version: str = None,
        location_query: str = None,
        locations: List[str] = None,
        query: str = None,
        size: int = None,
        step_for_custom_summary_style_config: main_models.GetHotTopicBroadcastRequestStepForCustomSummaryStyleConfig = None,
        step_for_news_broadcast_content_config: main_models.GetHotTopicBroadcastRequestStepForNewsBroadcastContentConfig = None,
        topics: List[str] = None,
        workspace_id: str = None,
    ):
        self.calc_total_token = calc_total_token
        self.category = category
        self.current = current
        self.hot_topic_version = hot_topic_version
        self.location_query = location_query
        self.locations = locations
        self.query = query
        self.size = size
        self.step_for_custom_summary_style_config = step_for_custom_summary_style_config
        self.step_for_news_broadcast_content_config = step_for_news_broadcast_content_config
        self.topics = topics
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.step_for_custom_summary_style_config:
            self.step_for_custom_summary_style_config.validate()
        if self.step_for_news_broadcast_content_config:
            self.step_for_news_broadcast_content_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.calc_total_token is not None:
            result['CalcTotalToken'] = self.calc_total_token

        if self.category is not None:
            result['Category'] = self.category

        if self.current is not None:
            result['Current'] = self.current

        if self.hot_topic_version is not None:
            result['HotTopicVersion'] = self.hot_topic_version

        if self.location_query is not None:
            result['LocationQuery'] = self.location_query

        if self.locations is not None:
            result['Locations'] = self.locations

        if self.query is not None:
            result['Query'] = self.query

        if self.size is not None:
            result['Size'] = self.size

        if self.step_for_custom_summary_style_config is not None:
            result['StepForCustomSummaryStyleConfig'] = self.step_for_custom_summary_style_config.to_map()

        if self.step_for_news_broadcast_content_config is not None:
            result['StepForNewsBroadcastContentConfig'] = self.step_for_news_broadcast_content_config.to_map()

        if self.topics is not None:
            result['Topics'] = self.topics

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalcTotalToken') is not None:
            self.calc_total_token = m.get('CalcTotalToken')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Current') is not None:
            self.current = m.get('Current')

        if m.get('HotTopicVersion') is not None:
            self.hot_topic_version = m.get('HotTopicVersion')

        if m.get('LocationQuery') is not None:
            self.location_query = m.get('LocationQuery')

        if m.get('Locations') is not None:
            self.locations = m.get('Locations')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('StepForCustomSummaryStyleConfig') is not None:
            temp_model = main_models.GetHotTopicBroadcastRequestStepForCustomSummaryStyleConfig()
            self.step_for_custom_summary_style_config = temp_model.from_map(m.get('StepForCustomSummaryStyleConfig'))

        if m.get('StepForNewsBroadcastContentConfig') is not None:
            temp_model = main_models.GetHotTopicBroadcastRequestStepForNewsBroadcastContentConfig()
            self.step_for_news_broadcast_content_config = temp_model.from_map(m.get('StepForNewsBroadcastContentConfig'))

        if m.get('Topics') is not None:
            self.topics = m.get('Topics')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class GetHotTopicBroadcastRequestStepForNewsBroadcastContentConfig(DaraModel):
    def __init__(
        self,
        categories: List[str] = None,
        custom_hot_value_weights: List[main_models.GetHotTopicBroadcastRequestStepForNewsBroadcastContentConfigCustomHotValueWeights] = None,
        topic_count: int = None,
    ):
        self.categories = categories
        self.custom_hot_value_weights = custom_hot_value_weights
        self.topic_count = topic_count

    def validate(self):
        if self.custom_hot_value_weights:
            for v1 in self.custom_hot_value_weights:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.categories is not None:
            result['Categories'] = self.categories

        result['CustomHotValueWeights'] = []
        if self.custom_hot_value_weights is not None:
            for k1 in self.custom_hot_value_weights:
                result['CustomHotValueWeights'].append(k1.to_map() if k1 else None)

        if self.topic_count is not None:
            result['TopicCount'] = self.topic_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')

        self.custom_hot_value_weights = []
        if m.get('CustomHotValueWeights') is not None:
            for k1 in m.get('CustomHotValueWeights'):
                temp_model = main_models.GetHotTopicBroadcastRequestStepForNewsBroadcastContentConfigCustomHotValueWeights()
                self.custom_hot_value_weights.append(temp_model.from_map(k1))

        if m.get('TopicCount') is not None:
            self.topic_count = m.get('TopicCount')

        return self

class GetHotTopicBroadcastRequestStepForNewsBroadcastContentConfigCustomHotValueWeights(DaraModel):
    def __init__(
        self,
        dimension: str = None,
        weight: int = None,
    ):
        self.dimension = dimension
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dimension is not None:
            result['Dimension'] = self.dimension

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

class GetHotTopicBroadcastRequestStepForCustomSummaryStyleConfig(DaraModel):
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
            result['SummaryImageCount'] = self.summary_image_count

        if self.summary_model is not None:
            result['SummaryModel'] = self.summary_model

        if self.summary_prompt is not None:
            result['SummaryPrompt'] = self.summary_prompt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SummaryImageCount') is not None:
            self.summary_image_count = m.get('SummaryImageCount')

        if m.get('SummaryModel') is not None:
            self.summary_model = m.get('SummaryModel')

        if m.get('SummaryPrompt') is not None:
            self.summary_prompt = m.get('SummaryPrompt')

        return self

