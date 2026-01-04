# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeHighDefinitionMonitorLogAttributeResponseBody(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_type: str = None,
        log_project: str = None,
        log_store: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The ID of the instance whose fine-grained monitoring configurations you want to query.
        self.instance_id = instance_id
        # The type of instance for which you want to query fine-grained monitoring. Only **EIP** may be returned.
        self.instance_type = instance_type
        # The name of the project.
        self.log_project = log_project
        # The name of the Logstore.
        self.log_store = log_store
        # The request ID.
        self.request_id = request_id
        # Indicates whether the operation is performed. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.log_project is not None:
            result['LogProject'] = self.log_project

        if self.log_store is not None:
            result['LogStore'] = self.log_store

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('LogProject') is not None:
            self.log_project = m.get('LogProject')

        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

