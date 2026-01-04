# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class ListPublicIpAddressPoolCidrBlocksResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        public_ip_pool_cidr_block_list: List[main_models.ListPublicIpAddressPoolCidrBlocksResponseBodyPublicIpPoolCidrBlockList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The token that is used for the next query. Valid values:
        # 
        # *   If **NextToken** was not returned, it indicates that no additional results exist.
        # *   If **NextToken** is returned, the value is the token that is used for the next query.
        self.next_token = next_token
        # The total number of entries returned.
        self.public_ip_pool_cidr_block_list = public_ip_pool_cidr_block_list
        # The ID of the request.
        self.request_id = request_id
        # The maximum number of entries returned. Valid values: **10** to **100**. Default value: **10**.
        self.total_count = total_count

    def validate(self):
        if self.public_ip_pool_cidr_block_list:
            for v1 in self.public_ip_pool_cidr_block_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['PublicIpPoolCidrBlockList'] = []
        if self.public_ip_pool_cidr_block_list is not None:
            for k1 in self.public_ip_pool_cidr_block_list:
                result['PublicIpPoolCidrBlockList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.public_ip_pool_cidr_block_list = []
        if m.get('PublicIpPoolCidrBlockList') is not None:
            for k1 in m.get('PublicIpPoolCidrBlockList'):
                temp_model = main_models.ListPublicIpAddressPoolCidrBlocksResponseBodyPublicIpPoolCidrBlockList()
                self.public_ip_pool_cidr_block_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListPublicIpAddressPoolCidrBlocksResponseBodyPublicIpPoolCidrBlockList(DaraModel):
    def __init__(
        self,
        cidr_block: str = None,
        creation_time: str = None,
        public_ip_address_pool_id: str = None,
        status: str = None,
        total_ip_num: int = None,
        used_ip_num: int = None,
    ):
        # The ID of the IP address pool.
        self.cidr_block = cidr_block
        # The CIDR blocks.
        self.creation_time = creation_time
        # The information about the CIDR blocks.
        self.public_ip_address_pool_id = public_ip_address_pool_id
        # The time when the CIDR block was created. The time is displayed in `YYYY-MM-DDThh:mm:ssZ` format.
        self.status = status
        # The total number of available IP addresses in the CIDR block.
        self.total_ip_num = total_ip_num
        # The status of the CIDR block in the IP address pool. Valid values:
        # 
        # *   **Created**: available
        # *   **Deleting**: being deleted
        # *   **Modifying**: being modified
        self.used_ip_num = used_ip_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.public_ip_address_pool_id is not None:
            result['PublicIpAddressPoolId'] = self.public_ip_address_pool_id

        if self.status is not None:
            result['Status'] = self.status

        if self.total_ip_num is not None:
            result['TotalIpNum'] = self.total_ip_num

        if self.used_ip_num is not None:
            result['UsedIpNum'] = self.used_ip_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('PublicIpAddressPoolId') is not None:
            self.public_ip_address_pool_id = m.get('PublicIpAddressPoolId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalIpNum') is not None:
            self.total_ip_num = m.get('TotalIpNum')

        if m.get('UsedIpNum') is not None:
            self.used_ip_num = m.get('UsedIpNum')

        return self

