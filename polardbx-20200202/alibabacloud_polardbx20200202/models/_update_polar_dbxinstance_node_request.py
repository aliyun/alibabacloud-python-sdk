# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdatePolarDBXInstanceNodeRequest(DaraModel):
    def __init__(
        self,
        add_dnspec: str = None,
        cnnode_count: int = None,
        client_token: str = None,
        dbinstance_name: str = None,
        dnnode_count: int = None,
        db_instance_node_count: int = None,
        delete_dnids: str = None,
        region_id: str = None,
        storage_pool_name: str = None,
    ):
        self.add_dnspec = add_dnspec
        self.cnnode_count = cnnode_count
        self.client_token = client_token
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        self.dnnode_count = dnnode_count
        self.db_instance_node_count = db_instance_node_count
        self.delete_dnids = delete_dnids
        # This parameter is required.
        self.region_id = region_id
        self.storage_pool_name = storage_pool_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_dnspec is not None:
            result['AddDNSpec'] = self.add_dnspec

        if self.cnnode_count is not None:
            result['CNNodeCount'] = self.cnnode_count

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.dnnode_count is not None:
            result['DNNodeCount'] = self.dnnode_count

        if self.db_instance_node_count is not None:
            result['DbInstanceNodeCount'] = self.db_instance_node_count

        if self.delete_dnids is not None:
            result['DeleteDNIds'] = self.delete_dnids

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.storage_pool_name is not None:
            result['StoragePoolName'] = self.storage_pool_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddDNSpec') is not None:
            self.add_dnspec = m.get('AddDNSpec')

        if m.get('CNNodeCount') is not None:
            self.cnnode_count = m.get('CNNodeCount')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('DNNodeCount') is not None:
            self.dnnode_count = m.get('DNNodeCount')

        if m.get('DbInstanceNodeCount') is not None:
            self.db_instance_node_count = m.get('DbInstanceNodeCount')

        if m.get('DeleteDNIds') is not None:
            self.delete_dnids = m.get('DeleteDNIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StoragePoolName') is not None:
            self.storage_pool_name = m.get('StoragePoolName')

        return self

