# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListFeatureConsistencyCheckJobScoreReportsRequest(DaraModel):
    def __init__(
        self,
        exclude_request_ids: List[str] = None,
        instance_id: str = None,
    ):
        self.exclude_request_ids = exclude_request_ids
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exclude_request_ids is not None:
            result['ExcludeRequestIds'] = self.exclude_request_ids

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExcludeRequestIds') is not None:
            self.exclude_request_ids = m.get('ExcludeRequestIds')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

