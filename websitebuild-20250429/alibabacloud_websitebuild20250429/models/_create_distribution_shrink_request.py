# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDistributionShrinkRequest(DaraModel):
    def __init__(
        self,
        article_id: str = None,
        channels_shrink: str = None,
    ):
        # The article ID.
        # 
        # This parameter is required.
        self.article_id = article_id
        # The list of selected channels.
        # 
        # This parameter is required.
        self.channels_shrink = channels_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.article_id is not None:
            result['ArticleId'] = self.article_id

        if self.channels_shrink is not None:
            result['Channels'] = self.channels_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArticleId') is not None:
            self.article_id = m.get('ArticleId')

        if m.get('Channels') is not None:
            self.channels_shrink = m.get('Channels')

        return self

