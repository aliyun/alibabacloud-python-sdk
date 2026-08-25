# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDIJobLogRequest(DaraModel):
    def __init__(
        self,
        dijob_id: int = None,
        failover_id: int = None,
        id: int = None,
        instance_id: int = None,
        node_type: str = None,
        page_number: int = None,
    ):
        # **[Deprecated]** This parameter is deprecated. Use the Id parameter instead.
        self.dijob_id = dijob_id
        # The failover ID.
        self.failover_id = failover_id
        # The node ID.
        self.id = id
        # The instance ID.
        self.instance_id = instance_id
        # The node type. This parameter is applicable only to tasks that run on resource group 2.0. Valid values:
        # 
        # * **MASTER**: retrieves the JobManager logs.
        # * **WORKER**: retrieves the TaskManager logs.
        self.node_type = node_type
        # The page number for paging. The value must be a positive integer greater than or equal to 1.
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dijob_id is not None:
            result['DIJobId'] = self.dijob_id

        if self.failover_id is not None:
            result['FailoverId'] = self.failover_id

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DIJobId') is not None:
            self.dijob_id = m.get('DIJobId')

        if m.get('FailoverId') is not None:
            self.failover_id = m.get('FailoverId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        return self

