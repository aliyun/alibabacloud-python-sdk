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
        lock_reason: str = None,
        page_number: int = None,
        page_size: int = None,
        standby: str = None,
        status: str = None,
    ):
        # The ID of the EIP instance to query. You can specify up to 50 EIP instance IDs separated by commas (,).
        self.allocation_id = allocation_id
        # The instance ID of the cloud service.
        self.associated_instance_id = associated_instance_id
        # The type of the cloud service instance to associate. Valid values: 
        # 
        # - **EnsInstance**: a VPC-type ENS instance.
        # 
        # - **SlbInstance**: a load balancing instance.
        self.associated_instance_type = associated_instance_type
        # The IP address of the EIP to query. You can specify up to 50 EIP addresses separated by commas (,).
        self.eip_address = eip_address
        # The name of the EIP.
        self.eip_name = eip_name
        # The ENS edge zone ID.
        self.ens_region_id = ens_region_id
        # The array of ENS edge zone IDs. Array length: 1 to 100.
        self.ens_region_ids = ens_region_ids
        # Specifies whether ICMP echo reply is enabled. Valid values:
        # 
        # - **true** (default): enabled.
        # - **false**: disabled.
        self.icmp_reply_enabled = icmp_reply_enabled
        # The lock type.
        # - financial: locked due to overdue payment.
        self.lock_reason = lock_reason
        # The page number of the list. Default value: 1.
        self.page_number = page_number
        # The number of entries per page for a paged query. Maximum value: 100. Default value: 10.
        self.page_size = page_size
        # Specifies whether the EIP is a standby EIP. Valid values:
        # 
        # - **true**: standby.
        # 
        # - **false**: not standby.
        self.standby = standby
        # The status of the EIP. Valid values: Associating: being associated. Unassociating: being disassociated. InUse: allocated. Available: available.
        self.status = status

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

        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.standby is not None:
            result['Standby'] = self.standby

        if self.status is not None:
            result['Status'] = self.status

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

        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Standby') is not None:
            self.standby = m.get('Standby')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

