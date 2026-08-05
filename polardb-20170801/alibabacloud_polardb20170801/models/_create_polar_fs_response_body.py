# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePolarFsResponseBody(DaraModel):
    def __init__(
        self,
        order_id: str = None,
        polar_fs_instance_id: str = None,
        polar_fs_path: str = None,
        polar_fs_status: str = None,
        request_id: str = None,
    ):
        # The order ID.
        self.order_id = order_id
        # The PolarFS instance ID.
        self.polar_fs_instance_id = polar_fs_instance_id
        # The PolarFS file system path.
        self.polar_fs_path = polar_fs_path
        # The PolarFS instance status.
        self.polar_fs_status = polar_fs_status
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.polar_fs_instance_id is not None:
            result['PolarFsInstanceId'] = self.polar_fs_instance_id

        if self.polar_fs_path is not None:
            result['PolarFsPath'] = self.polar_fs_path

        if self.polar_fs_status is not None:
            result['PolarFsStatus'] = self.polar_fs_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('PolarFsInstanceId') is not None:
            self.polar_fs_instance_id = m.get('PolarFsInstanceId')

        if m.get('PolarFsPath') is not None:
            self.polar_fs_path = m.get('PolarFsPath')

        if m.get('PolarFsStatus') is not None:
            self.polar_fs_status = m.get('PolarFsStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

