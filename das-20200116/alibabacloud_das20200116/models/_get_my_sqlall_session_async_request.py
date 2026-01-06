# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMySQLAllSessionAsyncRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        node_id: str = None,
        result_id: str = None,
    ):
        # The instance ID.
        # 
        # >  Only ApsaraDB RDS for MySQL, PolarDB for MySQL, and PolarDB-X 2.0 instances are supported.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The node ID.
        # 
        # >  You must specify this parameter for PolarDB for MySQL clusters. If you do not specify a node ID, the session data of the primary node is returned by default.
        self.node_id = node_id
        # The asynchronous request ID.
        # 
        # >  GetMySQLAllSessionAsync is an asynchronous operation. After a request is sent, the system does not return complete results but returns a **request ID**. You need to use the **request ID** to initiate requests until the value of the **isFinish** field in the returned results is **true**, the complete results are returned. This indicates that to obtain complete data, you must call this operation at least twice.
        self.result_id = result_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.result_id is not None:
            result['ResultId'] = self.result_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('ResultId') is not None:
            self.result_id = m.get('ResultId')

        return self

