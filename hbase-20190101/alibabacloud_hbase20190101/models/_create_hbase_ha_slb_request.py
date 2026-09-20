# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateHbaseHaSlbRequest(DaraModel):
    def __init__(
        self,
        bds_id: str = None,
        client_token: str = None,
        ha_id: str = None,
        ha_types: str = None,
        hbase_type: str = None,
    ):
        # The ID of the BDS cluster.
        # 
        # This parameter is required.
        self.bds_id = bds_id
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The value cannot exceed 64 printable ASCII characters in length.
        self.client_token = client_token
        # The high-availability ID in the BDS active-active management.
        # 
        # This parameter is required.
        self.ha_id = ha_id
        # The high-availability type. Valid values:
        # 
        # - thrift
        # - phoenix.
        # 
        # This parameter is required.
        self.ha_types = ha_types
        # Specifies whether the high-availability type is on the primary or secondary instance. Valid values:
        # 
        # - Active: The high-availability type is on the primary instance.
        # - Standby: The high-availability type is on the secondary instance.
        # 
        # This parameter is required.
        self.hbase_type = hbase_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bds_id is not None:
            result['BdsId'] = self.bds_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.ha_id is not None:
            result['HaId'] = self.ha_id

        if self.ha_types is not None:
            result['HaTypes'] = self.ha_types

        if self.hbase_type is not None:
            result['HbaseType'] = self.hbase_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BdsId') is not None:
            self.bds_id = m.get('BdsId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('HaId') is not None:
            self.ha_id = m.get('HaId')

        if m.get('HaTypes') is not None:
            self.ha_types = m.get('HaTypes')

        if m.get('HbaseType') is not None:
            self.hbase_type = m.get('HbaseType')

        return self

