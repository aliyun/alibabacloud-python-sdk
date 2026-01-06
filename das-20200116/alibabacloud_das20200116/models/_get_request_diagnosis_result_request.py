# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRequestDiagnosisResultRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        message_id: str = None,
        node_id: str = None,
        source: str = None,
        sql_id: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The unique ID of the diagnostic task.[](~~341609~~)
        # 
        # >  If you set MessageId to the task ID of the automatic SQL optimization feature, no result is returned.
        # 
        # This parameter is required.
        self.message_id = message_id
        # The node ID.
        # 
        # >  You must specify the node ID if your database instance is a PolarDB for MySQL cluster, a PolarDB for PostgreSQL (compatible with Oracle) instance, or an ApsaraDB for MongoDB database.
        self.node_id = node_id
        # The source of the task.
        # 
        # >  This parameter is required if you call this operation in the DAS console. You do not need to specify this parameter when you call this operation.
        self.source = source
        # The SQL template ID.
        # 
        # >  This parameter is required if you call this operation in the DAS console. You do not need to specify this parameter when you call this operation.
        self.sql_id = sql_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.message_id is not None:
            result['MessageId'] = self.message_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.source is not None:
            result['Source'] = self.source

        if self.sql_id is not None:
            result['SqlId'] = self.sql_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')

        return self

