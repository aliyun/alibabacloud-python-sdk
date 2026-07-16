# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteBackupPolicyRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dbcluster_id: str = None,
        max_results: int = None,
        product: str = None,
        resource_owner_id: int = None,
    ):
        # A client token used to ensure the idempotence of the request. The value must be a string that contains a maximum of 64 ASCII characters and cannot contain non-ASCII characters.
        self.client_token = client_token
        # The cluster ID.
        # 
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/170879.html) operation to query information about all clusters in the destination region, including cluster IDs.
        self.dbcluster_id = dbcluster_id
        # The number of records to return on each page. Valid values: 1 to **100**. Default value: **30**.
        self.max_results = max_results
        # The product name.
        self.product = product
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.product is not None:
            result['Product'] = self.product

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

