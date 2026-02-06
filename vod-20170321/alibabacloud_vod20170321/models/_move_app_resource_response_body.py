# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class MoveAppResourceResponseBody(DaraModel):
    def __init__(
        self,
        failed_resource_ids: List[str] = None,
        non_exist_resource_ids: List[str] = None,
        request_id: str = None,
    ):
        # The IDs of the resources that failed to be migrated.
        self.failed_resource_ids = failed_resource_ids
        # The IDs of the resources that were not found.
        self.non_exist_resource_ids = non_exist_resource_ids
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed_resource_ids is not None:
            result['FailedResourceIds'] = self.failed_resource_ids

        if self.non_exist_resource_ids is not None:
            result['NonExistResourceIds'] = self.non_exist_resource_ids

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedResourceIds') is not None:
            self.failed_resource_ids = m.get('FailedResourceIds')

        if m.get('NonExistResourceIds') is not None:
            self.non_exist_resource_ids = m.get('NonExistResourceIds')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

