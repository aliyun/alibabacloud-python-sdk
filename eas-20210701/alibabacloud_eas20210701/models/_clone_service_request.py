# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class CloneServiceRequest(DaraModel):
    def __init__(
        self,
        labels: Dict[str, str] = None,
        body: str = None,
    ):
        # The label of the service to be cloned.
        self.labels = labels
        # The request body. For more information, see [CreateService](https://help.aliyun.com/document_detail/412086.html).
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.labels is not None:
            result['Labels'] = self.labels

        if self.body is not None:
            result['body'] = self.body

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('body') is not None:
            self.body = m.get('body')

        return self

