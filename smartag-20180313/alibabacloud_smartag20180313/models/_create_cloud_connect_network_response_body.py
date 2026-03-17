# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCloudConnectNetworkResponseBody(DaraModel):
    def __init__(
        self,
        ccn_id: str = None,
        cidr_block: str = None,
        description: str = None,
        name: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        snat_cidr_block: str = None,
        status: str = None,
    ):
        # The ID of the CCN instance.
        self.ccn_id = ccn_id
        # The private CIDR block.
        self.cidr_block = cidr_block
        # The description about the CCN instance.
        self.description = description
        # The name of the CCN instance.
        self.name = name
        # The ID of the request.
        self.request_id = request_id
        # The ID of the resource group to which the CCN instance belongs.
        self.resource_group_id = resource_group_id
        # The private CIDR block used for SNAT.
        self.snat_cidr_block = snat_cidr_block
        # The status of the CCN instance. Valid values:
        # 
        # *   **Active**: indicates the CNN instance running as expected.
        # *   **Pending**: indicates the CCN instance is to be created.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ccn_id is not None:
            result['CcnId'] = self.ccn_id

        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.snat_cidr_block is not None:
            result['SnatCidrBlock'] = self.snat_cidr_block

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CcnId') is not None:
            self.ccn_id = m.get('CcnId')

        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SnatCidrBlock') is not None:
            self.snat_cidr_block = m.get('SnatCidrBlock')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

