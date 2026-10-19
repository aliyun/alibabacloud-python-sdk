# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MasterNodeShutDownFailOverRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        dbfault_mode: str = None,
        dbnodes: str = None,
        fail_mode: str = None,
        instance_id: str = None,
        proxy_fault_mode: str = None,
        proxy_instance_ids: str = None,
    ):
        # The resource type. Set the value to `instance`.
        self.category = category
        # - **Specify**: Specifies the data nodes.
        # - **Random**: The system randomly simulates a failure for one-fourth of the data nodes (rounded up to the nearest integer, with a minimum of 1). This parameter takes effect only when no data nodes are specified.
        self.dbfault_mode = dbfault_mode
        # The specified data nodes.
        self.dbnodes = dbnodes
        # - **Hard**: Simulates an unrecoverable hardware failure. A switchover (HA) is directly triggered.
        # - **Soft** (default): Simulates a recoverable hardware failure. The system preferentially attempts to recover the failed node. If the recovery fails, a switchover (HA) is triggered.
        self.fail_mode = fail_mode
        # The instance ID. You can call the [DescribeInstances](https://help.aliyun.com/document_detail/473778.html) operation to query the instance ID.
        self.instance_id = instance_id
        # - **Specify**: Specifies the proxy nodes.
        # - **Random**: The system randomly simulates a failure for one-fourth of the proxy nodes (rounded up to the nearest integer, with a minimum of 1). This parameter takes effect only when no proxy nodes are specified.
        self.proxy_fault_mode = proxy_fault_mode
        # The specified proxy nodes.
        self.proxy_instance_ids = proxy_instance_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.dbfault_mode is not None:
            result['DBFaultMode'] = self.dbfault_mode

        if self.dbnodes is not None:
            result['DBNodes'] = self.dbnodes

        if self.fail_mode is not None:
            result['FailMode'] = self.fail_mode

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.proxy_fault_mode is not None:
            result['ProxyFaultMode'] = self.proxy_fault_mode

        if self.proxy_instance_ids is not None:
            result['ProxyInstanceIds'] = self.proxy_instance_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('DBFaultMode') is not None:
            self.dbfault_mode = m.get('DBFaultMode')

        if m.get('DBNodes') is not None:
            self.dbnodes = m.get('DBNodes')

        if m.get('FailMode') is not None:
            self.fail_mode = m.get('FailMode')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ProxyFaultMode') is not None:
            self.proxy_fault_mode = m.get('ProxyFaultMode')

        if m.get('ProxyInstanceIds') is not None:
            self.proxy_instance_ids = m.get('ProxyInstanceIds')

        return self

