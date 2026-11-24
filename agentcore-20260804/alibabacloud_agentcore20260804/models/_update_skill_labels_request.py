# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class UpdateSkillLabelsRequest(DaraModel):
    def __init__(
        self,
        body: main_models.UpdateSkillLabelsRequestBody = None,
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
            temp_model = main_models.UpdateSkillLabelsRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        return self

class UpdateSkillLabelsRequestBody(DaraModel):
    def __init__(
        self,
        label_descriptions: str = None,
        labels: str = None,
    ):
        # The label descriptions.
        self.label_descriptions = label_descriptions
        # The version label mapping JSON string.
        # 
        # This parameter is required.
        self.labels = labels

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label_descriptions is not None:
            result['labelDescriptions'] = self.label_descriptions

        if self.labels is not None:
            result['labels'] = self.labels

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('labelDescriptions') is not None:
            self.label_descriptions = m.get('labelDescriptions')

        if m.get('labels') is not None:
            self.labels = m.get('labels')

        return self

