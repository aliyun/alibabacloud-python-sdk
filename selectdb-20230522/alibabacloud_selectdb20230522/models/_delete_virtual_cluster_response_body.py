# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_selectdb20230522 import models as main_models
from darabonba.model import DaraModel

class DeleteVirtualClusterResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DeleteVirtualClusterResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DeleteVirtualClusterResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DeleteVirtualClusterResponseBodyData(DaraModel):
    def __init__(
        self,
        db_cluster_id: str = None,
        db_instance_id: str = None,
    ):
        self.db_cluster_id = db_cluster_id
        self.db_instance_id = db_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_cluster_id is not None:
            result['DbClusterId'] = self.db_cluster_id

        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbClusterId') is not None:
            self.db_cluster_id = m.get('DbClusterId')

        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')

        return self

