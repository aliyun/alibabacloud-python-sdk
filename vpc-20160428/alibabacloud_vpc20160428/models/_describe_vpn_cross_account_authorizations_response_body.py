# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeVpnCrossAccountAuthorizationsResponseBody(DaraModel):
    def __init__(
        self,
        cross_account_authorizations: List[main_models.DescribeVpnCrossAccountAuthorizationsResponseBodyCrossAccountAuthorizations] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The cross-account authorization information about the IPsec-VPN connection.
        self.cross_account_authorizations = cross_account_authorizations
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.cross_account_authorizations:
            for v1 in self.cross_account_authorizations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CrossAccountAuthorizations'] = []
        if self.cross_account_authorizations is not None:
            for k1 in self.cross_account_authorizations:
                result['CrossAccountAuthorizations'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cross_account_authorizations = []
        if m.get('CrossAccountAuthorizations') is not None:
            for k1 in m.get('CrossAccountAuthorizations'):
                temp_model = main_models.DescribeVpnCrossAccountAuthorizationsResponseBodyCrossAccountAuthorizations()
                self.cross_account_authorizations.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeVpnCrossAccountAuthorizationsResponseBodyCrossAccountAuthorizations(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        bind_instance: str = None,
        bind_product: str = None,
        bind_uid: int = None,
        creation_time: int = None,
        vpn_connection_id: str = None,
    ):
        # The ID of the Alibaba Cloud account to which the IPsec-VPN connection belongs.
        self.ali_uid = ali_uid
        # The ID of the CEN instance.
        self.bind_instance = bind_instance
        # The type of resource that can be associated with the IPsec-VPN connection.
        # 
        # Only **CEN** can be returned, which indicates that the IPsec-VPN connection is authorized to be associated with the transit router of a Cloud Enterprise Network (CEN) instance that belongs to another Alibaba Cloud account.
        self.bind_product = bind_product
        # The ID of the Alibaba Cloud account whose resources the IPsec-VPN connection is authorized to be associated with.
        self.bind_uid = bind_uid
        # The time when the authorization for the IPsec-VPN connection was created.
        # 
        # This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.creation_time = creation_time
        # The ID of the IPsec-VPN connection.
        self.vpn_connection_id = vpn_connection_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.bind_instance is not None:
            result['BindInstance'] = self.bind_instance

        if self.bind_product is not None:
            result['BindProduct'] = self.bind_product

        if self.bind_uid is not None:
            result['BindUid'] = self.bind_uid

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.vpn_connection_id is not None:
            result['VpnConnectionId'] = self.vpn_connection_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('BindInstance') is not None:
            self.bind_instance = m.get('BindInstance')

        if m.get('BindProduct') is not None:
            self.bind_product = m.get('BindProduct')

        if m.get('BindUid') is not None:
            self.bind_uid = m.get('BindUid')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('VpnConnectionId') is not None:
            self.vpn_connection_id = m.get('VpnConnectionId')

        return self

