# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateErAttachmentRequest(DaraModel):
    def __init__(
        self,
        auto_receive_all_route: bool = None,
        er_attachment_name: str = None,
        er_id: str = None,
        instance_id: str = None,
        instance_type: str = None,
        region_id: str = None,
        resource_tenant_id: str = None,
    ):
        # Indicates whether to automatically receive all routes from all instances under the Lingjun HUB. Valid values:
        # 
        # *   **true**: received automatically.
        # *   **false**: Not received.
        # 
        # This parameter is required.
        self.auto_receive_all_route = auto_receive_all_route
        # The name of the network instance connection.
        # 
        # This parameter is required.
        self.er_attachment_name = er_attachment_name
        # Lingjun HUB ID.
        # 
        # This parameter is required.
        self.er_id = er_id
        # The ID of the network instance. Valid values: **VPD** and **VCC**.
        # 
        # For more information, see [What is Lingjun?](https://help.aliyun.com/document_detail/444430.html)
        # 
        # You can query **Lingjun CIDR Block** and **Lingjun Connection** by [ListVpds](https://help.aliyun.com/document_detail/2331077.html) and [ListVccs](https://help.aliyun.com/document_detail/2399526.html?) respectively.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The category of the instance. Valid values:
        # 
        # *   **VPD**: indicates the Lingjun CIDR block.
        # *   **VCC**: indicates a Lingjun connection.
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the tenant to which the resource belongs. This parameter is required for cross-account resources.
        self.resource_tenant_id = resource_tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_receive_all_route is not None:
            result['AutoReceiveAllRoute'] = self.auto_receive_all_route

        if self.er_attachment_name is not None:
            result['ErAttachmentName'] = self.er_attachment_name

        if self.er_id is not None:
            result['ErId'] = self.er_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_tenant_id is not None:
            result['ResourceTenantId'] = self.resource_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoReceiveAllRoute') is not None:
            self.auto_receive_all_route = m.get('AutoReceiveAllRoute')

        if m.get('ErAttachmentName') is not None:
            self.er_attachment_name = m.get('ErAttachmentName')

        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceTenantId') is not None:
            self.resource_tenant_id = m.get('ResourceTenantId')

        return self

