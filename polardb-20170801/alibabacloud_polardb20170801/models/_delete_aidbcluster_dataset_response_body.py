# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAIDBClusterDatasetResponseBody(DaraModel):
    def __init__(
        self,
        data_service_id: str = None,
        dataset_id: str = None,
        request_id: str = None,
    ):
        self.data_service_id = data_service_id
        self.dataset_id = dataset_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_service_id is not None:
            result['DataServiceId'] = self.data_service_id

        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataServiceId') is not None:
            self.data_service_id = m.get('DataServiceId')

        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

