# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunHotTopicSummaryShrinkRequest(DaraModel):
    def __init__(
        self,
        hot_topic_version: str = None,
        step_for_custom_summary_style_config_shrink: str = None,
        topic_ids_shrink: str = None,
    ):
        # This parameter is required.
        self.hot_topic_version = hot_topic_version
        # This parameter is required.
        self.step_for_custom_summary_style_config_shrink = step_for_custom_summary_style_config_shrink
        # This parameter is required.
        self.topic_ids_shrink = topic_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hot_topic_version is not None:
            result['hotTopicVersion'] = self.hot_topic_version

        if self.step_for_custom_summary_style_config_shrink is not None:
            result['stepForCustomSummaryStyleConfig'] = self.step_for_custom_summary_style_config_shrink

        if self.topic_ids_shrink is not None:
            result['topicIds'] = self.topic_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hotTopicVersion') is not None:
            self.hot_topic_version = m.get('hotTopicVersion')

        if m.get('stepForCustomSummaryStyleConfig') is not None:
            self.step_for_custom_summary_style_config_shrink = m.get('stepForCustomSummaryStyleConfig')

        if m.get('topicIds') is not None:
            self.topic_ids_shrink = m.get('topicIds')

        return self

