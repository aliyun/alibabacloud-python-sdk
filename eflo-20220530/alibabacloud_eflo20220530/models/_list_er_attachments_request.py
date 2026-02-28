# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListErAttachmentsRequest(DaraModel):
    def __init__(
        self,
        auto_receive_all_route: bool = None,
        enable_page: bool = None,
        er_attachment_id: str = None,
        er_attachment_name: str = None,
        er_id: str = None,
        instance_id: str = None,
        instance_type: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_tenant_id: str = None,
        status: str = None,
    ):
        # Whether to automatically receive all routes from all instances under this Lingjun HUB. Valid values:
        # 
        # *   **true**: received automatically.
        # *   **false**: Not received.
        self.auto_receive_all_route = auto_receive_all_route
        # Specifies whether to enable paged query. Valid values:
        # 
        # *   **true**: enables paged query.
        # *   **false**: Paged query is not enabled.
        self.enable_page = enable_page
        # The ID of the network instance connection
        self.er_attachment_id = er_attachment_id
        # The name of the network instance connection.
        self.er_attachment_name = er_attachment_name
        # The ID of the Lingjun HUB instance.
        # 
        # This parameter is required.
        self.er_id = er_id
        # The ID of the network instance. Valid values: **VPD** and **VCC**.
        # 
        # For more information, see [What is Lingjun?](https://help.aliyun.com/document_detail/444430.html)
        # 
        # You can query **Lingjun CIDR blocks** and **Lingjun connections** by [ListVpds](https://help.aliyun.com/document_detail/2331077.html) and [ListVccs](https://help.aliyun.com/document_detail/2399526.html?) respectively.
        self.instance_id = instance_id
        # The mitigation plan of the instance. Valid values:
        # 
        # *   **VPD**: indicates the Lingjun CIDR block.
        # *   **VCC**: indicates a Lingjun connection.
        self.instance_type = instance_type
        # The page number to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 20.
        self.page_size = page_size
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Resource group instance ID
        self.resource_group_id = resource_group_id
        # The ID of the tenant to which the instance belongs.
        self.resource_tenant_id = resource_tenant_id
        # The status of the CLB instance. Valid values:
        # 
        # *   **Available**: Normal.
        # *   **Not Available**: Not available.
        # *   **Executing**: The task is being executed.
        # *   **Deleting**: The account is being deleted
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_receive_all_route is not None:
            result['AutoReceiveAllRoute'] = self.auto_receive_all_route

        if self.enable_page is not None:
            result['EnablePage'] = self.enable_page

        if self.er_attachment_id is not None:
            result['ErAttachmentId'] = self.er_attachment_id

        if self.er_attachment_name is not None:
            result['ErAttachmentName'] = self.er_attachment_name

        if self.er_id is not None:
            result['ErId'] = self.er_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_tenant_id is not None:
            result['ResourceTenantId'] = self.resource_tenant_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoReceiveAllRoute') is not None:
            self.auto_receive_all_route = m.get('AutoReceiveAllRoute')

        if m.get('EnablePage') is not None:
            self.enable_page = m.get('EnablePage')

        if m.get('ErAttachmentId') is not None:
            self.er_attachment_id = m.get('ErAttachmentId')

        if m.get('ErAttachmentName') is not None:
            self.er_attachment_name = m.get('ErAttachmentName')

        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceTenantId') is not None:
            self.resource_tenant_id = m.get('ResourceTenantId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

