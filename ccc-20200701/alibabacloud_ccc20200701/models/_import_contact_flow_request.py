# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImportContactFlowRequest(DaraModel):
    def __init__(
        self,
        flow_package_data: str = None,
        instance_id: str = None,
        request_id: str = None,
    ):
        # This parameter is required.
        self.flow_package_data = flow_package_data
        # This parameter is required.
        self.instance_id = instance_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flow_package_data is not None:
            result['FlowPackageData'] = self.flow_package_data

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowPackageData') is not None:
            self.flow_package_data = m.get('FlowPackageData')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

