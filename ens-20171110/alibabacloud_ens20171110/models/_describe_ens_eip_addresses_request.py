# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeEnsEipAddressesRequest(DaraModel):
    def __init__(
        self,
        allocation_id: str = None,
        associated_instance_id: str = None,
        associated_instance_type: str = None,
        eip_address: str = None,
        eip_name: str = None,
        ens_region_id: str = None,
        ens_region_ids: List[str] = None,
        icmp_reply_enabled: bool = None,
        page_number: int = None,
        page_size: int = None,
        standby: str = None,
    ):
        # The ID of the EIP that you want to query. You can specify up to 50 EIP IDs. Separate multiple IDs with commas (,).
        self.allocation_id = allocation_id
        # The ID of the instance with which you want to associate the EIP.
        self.associated_instance_id = associated_instance_id
        # The type of the instance that is associated with the EIP. Valid values:
        # 
        # *   **EnsInstance**: ENS instance in a VPC
        # *   **SlbInstance**: SLB instance
        self.associated_instance_type = associated_instance_type
        # The EIP that you want to query. You can specify up to 50 EIPs. Separate multiple EIPs with commas (,).
        self.eip_address = eip_address
        # The name of the EIP.
        self.eip_name = eip_name
        # The ID of the Edge Node Service (ENS) node.
        self.ens_region_id = ens_region_id
        # The IDs of edge nodes. You can specify 1 to 100 IDs.
        self.ens_region_ids = ens_region_ids
        self.icmp_reply_enabled = icmp_reply_enabled
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Maximum value: 100. Default value: 10.
        self.page_size = page_size
        # Specifies whether the EIP is a secondary EIP. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.standby = standby

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id

        if self.associated_instance_id is not None:
            result['AssociatedInstanceId'] = self.associated_instance_id

        if self.associated_instance_type is not None:
            result['AssociatedInstanceType'] = self.associated_instance_type

        if self.eip_address is not None:
            result['EipAddress'] = self.eip_address

        if self.eip_name is not None:
            result['EipName'] = self.eip_name

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.ens_region_ids is not None:
            result['EnsRegionIds'] = self.ens_region_ids

        if self.icmp_reply_enabled is not None:
            result['IcmpReplyEnabled'] = self.icmp_reply_enabled

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.standby is not None:
            result['Standby'] = self.standby

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')

        if m.get('AssociatedInstanceId') is not None:
            self.associated_instance_id = m.get('AssociatedInstanceId')

        if m.get('AssociatedInstanceType') is not None:
            self.associated_instance_type = m.get('AssociatedInstanceType')

        if m.get('EipAddress') is not None:
            self.eip_address = m.get('EipAddress')

        if m.get('EipName') is not None:
            self.eip_name = m.get('EipName')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('EnsRegionIds') is not None:
            self.ens_region_ids = m.get('EnsRegionIds')

        if m.get('IcmpReplyEnabled') is not None:
            self.icmp_reply_enabled = m.get('IcmpReplyEnabled')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Standby') is not None:
            self.standby = m.get('Standby')

        return self

