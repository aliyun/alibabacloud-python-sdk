# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListFeatureViewOnlineFeaturesResponseBody(DaraModel):
    def __init__(
        self,
        online_features: List[str] = None,
        request_id: str = None,
    ):
        self.online_features = online_features
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.online_features is not None:
            result['OnlineFeatures'] = self.online_features

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OnlineFeatures') is not None:
            self.online_features = m.get('OnlineFeatures')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

