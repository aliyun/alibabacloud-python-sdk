# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class LogGroup(DaraModel):
    def __init__(
        self,
        log_items: List[main_models.LogItem] = None,
        log_tags: List[main_models.LogTag] = None,
        source: str = None,
        topic: str = None,
    ):
        # This parameter is required.
        self.log_items = log_items
        self.log_tags = log_tags
        self.source = source
        self.topic = topic

    def validate(self):
        if self.log_items:
            for v1 in self.log_items:
                 if v1:
                    v1.validate()
        if self.log_tags:
            for v1 in self.log_tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LogItems'] = []
        if self.log_items is not None:
            for k1 in self.log_items:
                result['LogItems'].append(k1.to_map() if k1 else None)

        result['LogTags'] = []
        if self.log_tags is not None:
            for k1 in self.log_tags:
                result['LogTags'].append(k1.to_map() if k1 else None)

        if self.source is not None:
            result['Source'] = self.source

        if self.topic is not None:
            result['Topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.log_items = []
        if m.get('LogItems') is not None:
            for k1 in m.get('LogItems'):
                temp_model = main_models.LogItem()
                self.log_items.append(temp_model.from_map(k1))

        self.log_tags = []
        if m.get('LogTags') is not None:
            for k1 in m.get('LogTags'):
                temp_model = main_models.LogTag()
                self.log_tags.append(temp_model.from_map(k1))

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        return self

