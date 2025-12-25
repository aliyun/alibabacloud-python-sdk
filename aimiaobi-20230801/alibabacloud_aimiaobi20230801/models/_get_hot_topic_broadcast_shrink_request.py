# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetHotTopicBroadcastShrinkRequest(DaraModel):
    def __init__(
        self,
        calc_total_token: bool = None,
        category: str = None,
        current: int = None,
        hot_topic_version: str = None,
        location_query: str = None,
        locations_shrink: str = None,
        query: str = None,
        size: int = None,
        step_for_custom_summary_style_config_shrink: str = None,
        step_for_news_broadcast_content_config_shrink: str = None,
        topics_shrink: str = None,
        workspace_id: str = None,
    ):
        self.calc_total_token = calc_total_token
        self.category = category
        self.current = current
        self.hot_topic_version = hot_topic_version
        self.location_query = location_query
        self.locations_shrink = locations_shrink
        self.query = query
        self.size = size
        self.step_for_custom_summary_style_config_shrink = step_for_custom_summary_style_config_shrink
        self.step_for_news_broadcast_content_config_shrink = step_for_news_broadcast_content_config_shrink
        self.topics_shrink = topics_shrink
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

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

        if self.locations_shrink is not None:
            result['Locations'] = self.locations_shrink

        if self.query is not None:
            result['Query'] = self.query

        if self.size is not None:
            result['Size'] = self.size

        if self.step_for_custom_summary_style_config_shrink is not None:
            result['StepForCustomSummaryStyleConfig'] = self.step_for_custom_summary_style_config_shrink

        if self.step_for_news_broadcast_content_config_shrink is not None:
            result['StepForNewsBroadcastContentConfig'] = self.step_for_news_broadcast_content_config_shrink

        if self.topics_shrink is not None:
            result['Topics'] = self.topics_shrink

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
            self.locations_shrink = m.get('Locations')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('StepForCustomSummaryStyleConfig') is not None:
            self.step_for_custom_summary_style_config_shrink = m.get('StepForCustomSummaryStyleConfig')

        if m.get('StepForNewsBroadcastContentConfig') is not None:
            self.step_for_news_broadcast_content_config_shrink = m.get('StepForNewsBroadcastContentConfig')

        if m.get('Topics') is not None:
            self.topics_shrink = m.get('Topics')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

