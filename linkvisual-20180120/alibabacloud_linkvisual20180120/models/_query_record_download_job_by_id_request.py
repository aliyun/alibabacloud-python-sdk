# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryRecordDownloadJobByIdRequest(DaraModel):
    def __init__(
        self,
        iot_instance_id: str = None,
        job_id: str = None,
    ):
        # The instance ID. You can view the ID of the current instance on the **Instance Overview** tab in the IoT Platform console.
        # 
        # This parameter is required.
        self.iot_instance_id = iot_instance_id
        # The ID of the cloud record download task.
        # 
        # This parameter is required.
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        return self

