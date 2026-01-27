# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDedicatedBlockStorageClusterAttributeRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dbsc_id: str = None,
        dbsc_name: str = None,
        description: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests.
        # 
        # The ClientToken value can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure idempotence ](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The ID of the dedicated block storage cluster.
        # 
        # This parameter is required.
        self.dbsc_id = dbsc_id
        # The new name of the dedicated block storage cluster.
        # 
        # This parameter is required.
        self.dbsc_name = dbsc_name
        # The new description of dedicated block storage cluster.
        self.description = description
        # The region ID of the dedicated block storage cluster. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dbsc_id is not None:
            result['DbscId'] = self.dbsc_id

        if self.dbsc_name is not None:
            result['DbscName'] = self.dbsc_name

        if self.description is not None:
            result['Description'] = self.description

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DbscId') is not None:
            self.dbsc_id = m.get('DbscId')

        if m.get('DbscName') is not None:
            self.dbsc_name = m.get('DbscName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

