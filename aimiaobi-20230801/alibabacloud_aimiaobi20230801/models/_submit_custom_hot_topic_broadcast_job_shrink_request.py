# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitCustomHotTopicBroadcastJobShrinkRequest(DaraModel):
    def __init__(
        self,
        hot_topic_broadcast_config_shrink: str = None,
        hot_topic_version: str = None,
        topics_shrink: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.hot_topic_broadcast_config_shrink = hot_topic_broadcast_config_shrink
        self.hot_topic_version = hot_topic_version
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
        if self.hot_topic_broadcast_config_shrink is not None:
            result['HotTopicBroadcastConfig'] = self.hot_topic_broadcast_config_shrink

        if self.hot_topic_version is not None:
            result['HotTopicVersion'] = self.hot_topic_version

        if self.topics_shrink is not None:
            result['Topics'] = self.topics_shrink

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotTopicBroadcastConfig') is not None:
            self.hot_topic_broadcast_config_shrink = m.get('HotTopicBroadcastConfig')

        if m.get('HotTopicVersion') is not None:
            self.hot_topic_version = m.get('HotTopicVersion')

        if m.get('Topics') is not None:
            self.topics_shrink = m.get('Topics')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

