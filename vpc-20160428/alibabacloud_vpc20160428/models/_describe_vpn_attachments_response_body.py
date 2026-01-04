# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeVpnAttachmentsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        vpn_attachments: List[main_models.DescribeVpnAttachmentsResponseBodyVpnAttachments] = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The number of returned entries.
        self.total_count = total_count
        # The list of IPsec-VPN connections associated with the transit router.
        self.vpn_attachments = vpn_attachments

    def validate(self):
        if self.vpn_attachments:
            for v1 in self.vpn_attachments:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['VpnAttachments'] = []
        if self.vpn_attachments is not None:
            for k1 in self.vpn_attachments:
                result['VpnAttachments'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.vpn_attachments = []
        if m.get('VpnAttachments') is not None:
            for k1 in m.get('VpnAttachments'):
                temp_model = main_models.DescribeVpnAttachmentsResponseBodyVpnAttachments()
                self.vpn_attachments.append(temp_model.from_map(k1))

        return self

class DescribeVpnAttachmentsResponseBodyVpnAttachments(DaraModel):
    def __init__(
        self,
        attach_type: str = None,
        cross_account_authorized: bool = None,
        description: str = None,
        instance_id: str = None,
        name: str = None,
        tag: str = None,
        tags: List[main_models.DescribeVpnAttachmentsResponseBodyVpnAttachmentsTags] = None,
        transit_router_id: str = None,
        transit_router_name: str = None,
    ):
        # The type of resource that is associated with the IPsec-VPN connection. The value is set to **CEN**, which indicates that the IPsec-VPN connection is associated with a transit router.
        self.attach_type = attach_type
        # Indicates whether the IPsec-VPN connection is associated with a transit router that belongs to another Alibaba Cloud account. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.cross_account_authorized = cross_account_authorized
        # The description of the IPsec-VPN connection.
        self.description = description
        # The ID of the IPsec-VPN connection.
        self.instance_id = instance_id
        # The name of the IPsec-VPN connection.
        self.name = name
        # The system tags of the IPsec-VPN connection.
        # 
        # You can check whether an IPsec-VPN connection supports BGP based on the system tags.
        # 
        # **BGPSupport**: indicates whether the IPsec-VPN connection supports BGP.
        # 
        # *   **true**
        # *   **false**
        self.tag = tag
        # The list of tags to be added to the IPsec-VPN connection.
        self.tags = tags
        # The ID of the transit router with which the IPsec-VPN connection is associated.
        self.transit_router_id = transit_router_id
        # The name of the transit router.
        self.transit_router_name = transit_router_name

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attach_type is not None:
            result['AttachType'] = self.attach_type

        if self.cross_account_authorized is not None:
            result['CrossAccountAuthorized'] = self.cross_account_authorized

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.tag is not None:
            result['Tag'] = self.tag

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id

        if self.transit_router_name is not None:
            result['TransitRouterName'] = self.transit_router_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachType') is not None:
            self.attach_type = m.get('AttachType')

        if m.get('CrossAccountAuthorized') is not None:
            self.cross_account_authorized = m.get('CrossAccountAuthorized')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeVpnAttachmentsResponseBodyVpnAttachmentsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        if m.get('TransitRouterName') is not None:
            self.transit_router_name = m.get('TransitRouterName')

        return self

class DescribeVpnAttachmentsResponseBodyVpnAttachmentsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the IPsec-VPN connection.
        self.key = key
        # The tag value of the IPsec-VPN connection.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

