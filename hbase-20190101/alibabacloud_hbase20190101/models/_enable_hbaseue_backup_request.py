# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnableHBaseueBackupRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        cold_storage_size: int = None,
        hbaseue_cluster_id: str = None,
        node_count: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The cold storage size for the backup service. The minimum value is 800 GB.
        self.cold_storage_size = cold_storage_size
        # The ID of the HBaseue cluster.
        # 
        # This parameter is required.
        self.hbaseue_cluster_id = hbaseue_cluster_id
        # The number of backup nodes.
        # 
        # This parameter is required.
        self.node_count = node_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.cold_storage_size is not None:
            result['ColdStorageSize'] = self.cold_storage_size

        if self.hbaseue_cluster_id is not None:
            result['HbaseueClusterId'] = self.hbaseue_cluster_id

        if self.node_count is not None:
            result['NodeCount'] = self.node_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ColdStorageSize') is not None:
            self.cold_storage_size = m.get('ColdStorageSize')

        if m.get('HbaseueClusterId') is not None:
            self.hbaseue_cluster_id = m.get('HbaseueClusterId')

        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')

        return self

