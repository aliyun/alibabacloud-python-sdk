# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAIDBClusterDatasetResponseBody(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        data_service_id: str = None,
        dataset_id: str = None,
        dataset_name: str = None,
        path: str = None,
        request_id: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.data_service_id = data_service_id
        self.dataset_id = dataset_id
        self.dataset_name = dataset_name
        self.path = path
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.data_service_id is not None:
            result['DataServiceId'] = self.data_service_id

        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id

        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.path is not None:
            result['Path'] = self.path

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DataServiceId') is not None:
            self.data_service_id = m.get('DataServiceId')

        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')

        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

