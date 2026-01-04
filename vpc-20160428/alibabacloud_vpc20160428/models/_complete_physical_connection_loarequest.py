# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CompletePhysicalConnectionLOARequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        finish_work: bool = None,
        instance_id: str = None,
        line_code: str = None,
        line_label: str = None,
        line_spcontact_info: str = None,
        line_service_provider: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among different requests.
        # 
        # >  If you do not set this parameter, the system automatically uses **RequestId** as **ClientToken**. **RequestId** of each API request may be different.
        self.client_token = client_token
        # Specifies whether the construction is completed. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.finish_work = finish_work
        # The ID of the Express Connect circuit.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The circuit code provided by the connectivity provider.
        self.line_code = line_code
        # The label of the cable in the data center.
        self.line_label = line_label
        # The contact information about line O\\&M.
        self.line_spcontact_info = line_spcontact_info
        # The ISP. Valid values:
        # 
        # *   **China Telecom**
        # *   **China Unicom**
        # *   **China Mobile**
        # *   **Other ISPs in China**
        self.line_service_provider = line_service_provider
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the Express Connect circuit.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
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

        if self.finish_work is not None:
            result['FinishWork'] = self.finish_work

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.line_code is not None:
            result['LineCode'] = self.line_code

        if self.line_label is not None:
            result['LineLabel'] = self.line_label

        if self.line_spcontact_info is not None:
            result['LineSPContactInfo'] = self.line_spcontact_info

        if self.line_service_provider is not None:
            result['LineServiceProvider'] = self.line_service_provider

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('FinishWork') is not None:
            self.finish_work = m.get('FinishWork')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LineCode') is not None:
            self.line_code = m.get('LineCode')

        if m.get('LineLabel') is not None:
            self.line_label = m.get('LineLabel')

        if m.get('LineSPContactInfo') is not None:
            self.line_spcontact_info = m.get('LineSPContactInfo')

        if m.get('LineServiceProvider') is not None:
            self.line_service_provider = m.get('LineServiceProvider')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

