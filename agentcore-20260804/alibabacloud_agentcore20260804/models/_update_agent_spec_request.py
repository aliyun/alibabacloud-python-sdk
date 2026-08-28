# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class UpdateAgentSpecRequest(DaraModel):
    def __init__(
        self,
        body: main_models.UpdateAgentSpecRequestBody = None,
    ):
        # The request body.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.UpdateAgentSpecRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        return self

class UpdateAgentSpecRequestBody(DaraModel):
    def __init__(
        self,
        biz_tags: str = None,
        labels: str = None,
        scope: str = None,
    ):
        # The business tags as a JSON-formatted string.
        self.biz_tags = biz_tags
        # The label mapping as a JSON-formatted string.
        self.labels = labels
        # The visibility scope. Valid values:
        # - PUBLIC
        # - PRIVATE
        self.scope = scope

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_tags is not None:
            result['bizTags'] = self.biz_tags

        if self.labels is not None:
            result['labels'] = self.labels

        if self.scope is not None:
            result['scope'] = self.scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizTags') is not None:
            self.biz_tags = m.get('bizTags')

        if m.get('labels') is not None:
            self.labels = m.get('labels')

        if m.get('scope') is not None:
            self.scope = m.get('scope')

        return self

