# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMongoDBCurrentOpRequest(DaraModel):
    def __init__(
        self,
        filter_doc: str = None,
        instance_id: str = None,
        node_id: str = None,
        role: str = None,
    ):
        # The `db.currentOp()` command that is used to filter sessions. For more information, see [db.currentOp()](https://docs.mongodb.com/manual/reference/method/db.currentOp/) of MongoDB Documentation.
        self.filter_doc = filter_doc
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The node ID.
        # 
        # >  If you do not specify a node ID, the sessions of the primary node are queried by default.
        self.node_id = node_id
        # A reserved parameter. You do not need to specify the parameter.
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter_doc is not None:
            result['FilterDoc'] = self.filter_doc

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.role is not None:
            result['Role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilterDoc') is not None:
            self.filter_doc = m.get('FilterDoc')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        return self

