# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListFeatureConsistencyCheckJobScoreReportsShrinkRequest(DaraModel):
    def __init__(
        self,
        exclude_request_ids_shrink: str = None,
        instance_id: str = None,
    ):
        self.exclude_request_ids_shrink = exclude_request_ids_shrink
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exclude_request_ids_shrink is not None:
            result['ExcludeRequestIds'] = self.exclude_request_ids_shrink

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExcludeRequestIds') is not None:
            self.exclude_request_ids_shrink = m.get('ExcludeRequestIds')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

