# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddInstallCodeRequest(DaraModel):
    def __init__(
        self,
        expired_date: int = None,
        group_id: int = None,
        only_image: bool = None,
        os: str = None,
        private_link_id: int = None,
        proxy_cluster: str = None,
        vendor_name: str = None,
    ):
        # The validity period of the installation command. The value is a 13-digit timestamp.
        # 
        # >  The installation command is valid only within the validity period. An expired installation command cannot be used to install the Security Center agent.
        self.expired_date = expired_date
        # The ID of the asset group to which you want to add the asset.
        # 
        # > You can call the [DescribeAllGroups](~~DescribeAllGroups~~) operation to query the IDs of asset groups.
        self.group_id = group_id
        # Specifies whether to create an image. Default value: **false**. Valid values:
        # 
        # *   **false**: does not create an image.
        # *   **true**: creates an image.
        self.only_image = only_image
        # The operating system of the asset. Default value: **linux**. Valid values:
        # 
        # *   **linux**
        # *   **windows**
        self.os = os
        # The ID of the PrivateLink endpoint.
        self.private_link_id = private_link_id
        # The name of the proxy cluster.
        self.proxy_cluster = proxy_cluster
        # The name of the service provider for the asset. Default value: **ALIYUN**.
        # 
        # >  You can call the [DescribeVendorList](~~DescribeVendorList~~) operation to query the names of service providers.
        self.vendor_name = vendor_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expired_date is not None:
            result['ExpiredDate'] = self.expired_date

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.only_image is not None:
            result['OnlyImage'] = self.only_image

        if self.os is not None:
            result['Os'] = self.os

        if self.private_link_id is not None:
            result['PrivateLinkId'] = self.private_link_id

        if self.proxy_cluster is not None:
            result['ProxyCluster'] = self.proxy_cluster

        if self.vendor_name is not None:
            result['VendorName'] = self.vendor_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiredDate') is not None:
            self.expired_date = m.get('ExpiredDate')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('OnlyImage') is not None:
            self.only_image = m.get('OnlyImage')

        if m.get('Os') is not None:
            self.os = m.get('Os')

        if m.get('PrivateLinkId') is not None:
            self.private_link_id = m.get('PrivateLinkId')

        if m.get('ProxyCluster') is not None:
            self.proxy_cluster = m.get('ProxyCluster')

        if m.get('VendorName') is not None:
            self.vendor_name = m.get('VendorName')

        return self

