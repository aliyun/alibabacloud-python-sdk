# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class PublishSkillVersionRequest(DaraModel):
    def __init__(
        self,
        body: main_models.PublishSkillVersionRequestBody = None,
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
            temp_model = main_models.PublishSkillVersionRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        return self

class PublishSkillVersionRequestBody(DaraModel):
    def __init__(
        self,
        update_latest_label: bool = None,
    ):
        # Specifies whether to update the latest label.
        self.update_latest_label = update_latest_label

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.update_latest_label is not None:
            result['updateLatestLabel'] = self.update_latest_label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('updateLatestLabel') is not None:
            self.update_latest_label = m.get('updateLatestLabel')

        return self

