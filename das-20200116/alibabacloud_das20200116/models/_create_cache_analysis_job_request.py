# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCacheAnalysisJobRequest(DaraModel):
    def __init__(
        self,
        backup_set_id: str = None,
        instance_id: str = None,
        node_id: str = None,
        separators: str = None,
    ):
        # The ID of the backup file. You can call the [DescribeBackups](https://help.aliyun.com/document_detail/473823.html) operation to query the ID.
        # 
        # *   If you need to specify multiple backup file IDs, separate them with commas (,). For example, you can set this parameter to `12345,67890`.
        # *   If you do not specify this parameter, the system automatically backs up the task and performs cache analysis on the backup file.
        self.backup_set_id = backup_set_id
        # The ID of the ApsaraDB for Redis instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the data node on the instance. You can specify this parameter to query the monitoring information about the specified node.
        # 
        # >  If you specify the BackupSetId parameter, the system ignores the NodeId parameter. You can call the [DescribeLogicInstanceTopology](https://help.aliyun.com/document_detail/473786.html) operation to query the node ID.
        self.node_id = node_id
        # The delimiters used to identify the prefixes of keys. You do not need to specify this parameter if one or more of the following default delimiters are used: `: ; , _ - + @ = | #`
        self.separators = separators

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.separators is not None:
            result['Separators'] = self.separators

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('Separators') is not None:
            self.separators = m.get('Separators')

        return self

