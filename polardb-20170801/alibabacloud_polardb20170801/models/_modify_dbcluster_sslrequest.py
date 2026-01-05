# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBClusterSSLRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        dbendpoint_id: str = None,
        net_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sslauto_rotate: str = None,
        sslenabled: str = None,
    ):
        # The ID of the cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The ID of the endpoint.
        # 
        # > 
        # 
        # *   This parameter is required for PolarDB for MySQL clusters.
        # 
        # *   This parameter is not required for PolarDB for PostgreSQL or PolarDB for PostgreSQL (Compatible with Oracle) clusters. By default, SSL encryption is enabled for all endpoints of the clusters.
        # 
        # *   You can call the [DescribeDBClusterSSL](https://help.aliyun.com/document_detail/2319159.html) operation to view the details of the endpoint.
        self.dbendpoint_id = dbendpoint_id
        # The network type supported by the endpoint that is specified by **DBEndpointId**. Valid values:
        # 
        # *   **Public**
        # *   **Private**
        # *   **Inner**
        # 
        # > 
        # 
        # *   This parameter is required for a PolarDB for MySQL cluster.
        # 
        # *   This parameter is not required for a PolarDB for Oracle or PolarDB for PostgreSQL cluster. By default, SSL encryption is enabled for all endpoints.
        self.net_type = net_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether automatic rotation of SSL certificates is enabled.
        # 
        # *   **Enable**: The feature is enabled.
        # *   **Disable**: The feature is disabled.
        self.sslauto_rotate = sslauto_rotate
        # The SSL encryption status. Valid values:
        # 
        # *   **Disable**: SSL encryption is disabled.
        # *   **Enable**: SSL encryption is enabled.
        # *   **Update**: The SSL certificate is updated.
        # 
        # > After you enable SSL encryption or update the SSL certificate, you must download and configure the certificate. For more information, see [Configure SSL encryption](https://help.aliyun.com/document_detail/153182.html).
        self.sslenabled = sslenabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbendpoint_id is not None:
            result['DBEndpointId'] = self.dbendpoint_id

        if self.net_type is not None:
            result['NetType'] = self.net_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.sslauto_rotate is not None:
            result['SSLAutoRotate'] = self.sslauto_rotate

        if self.sslenabled is not None:
            result['SSLEnabled'] = self.sslenabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBEndpointId') is not None:
            self.dbendpoint_id = m.get('DBEndpointId')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SSLAutoRotate') is not None:
            self.sslauto_rotate = m.get('SSLAutoRotate')

        if m.get('SSLEnabled') is not None:
            self.sslenabled = m.get('SSLEnabled')

        return self

