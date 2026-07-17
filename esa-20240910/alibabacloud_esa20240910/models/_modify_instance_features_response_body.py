# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyInstanceFeaturesResponseBody(DaraModel):
    def __init__(
        self,
        failed_features: str = None,
        request_id: str = None,
    ):
        # The site feature configurations that failed to be modified.
        self.failed_features = failed_features
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed_features is not None:
            result['FailedFeatures'] = self.failed_features

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedFeatures') is not None:
            self.failed_features = m.get('FailedFeatures')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

