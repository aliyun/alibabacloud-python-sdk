# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_selectdb20230522 import models as main_models
from darabonba.model import DaraModel

class ModifyDBClusterConfigResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: main_models.ModifyDBClusterConfigResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.data = data
        # The dynamic code. This parameter is not returned.
        self.dynamic_code = dynamic_code
        # The dynamic message. This parameter is not returned.
        self.dynamic_message = dynamic_message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Data') is not None:
            temp_model = main_models.ModifyDBClusterConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ModifyDBClusterConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        db_cluster_id: str = None,
        db_instance_id: str = None,
        db_instance_name: str = None,
        task_id: int = None,
    ):
        self.db_cluster_id = db_cluster_id
        self.db_instance_id = db_instance_id
        self.db_instance_name = db_instance_name
        self.task_id = task_id

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

        if self.db_instance_name is not None:
            result['DbInstanceName'] = self.db_instance_name

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbClusterId') is not None:
            self.db_cluster_id = m.get('DbClusterId')

        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')

        if m.get('DbInstanceName') is not None:
            self.db_instance_name = m.get('DbInstanceName')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

