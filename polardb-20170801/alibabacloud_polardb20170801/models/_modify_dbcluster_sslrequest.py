# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBClusterSSLRequest(DaraModel):
    def __init__(
        self,
        cert_valid_days: str = None,
        connection_string: str = None,
        dbcluster_id: str = None,
        dbendpoint_id: str = None,
        net_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pfs_instance_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sslauto_rotate: str = None,
        sslenabled: str = None,
    ):
        self.cert_valid_days = cert_valid_days
        self.connection_string = connection_string
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The endpoint ID.
        # 
        # >* If the cluster is a PolarDB for MySQL cluster, this parameter is required.
        # >* If the cluster is a PolarDB for PostgreSQL cluster or a PolarDB for PostgreSQL (Compatible with Oracle) cluster, you do not need to specify this parameter. Secure Sockets Layer (SSL) encryption is enabled for all endpoints by default.
        # >* You can call the [DescribeDBClusterSSL](https://help.aliyun.com/document_detail/2319159.html) operation to query endpoint details.
        self.dbendpoint_id = dbendpoint_id
        # The network type of the endpoint. The value must be consistent with the network type of the endpoint specified by the **DBEndpointId** parameter. Valid values:
        # * **Public**: public network
        # * **Private**: private network
        # * **Inner**: private network (classic network)
        # 
        # >* If the cluster is a PolarDB for MySQL cluster, this parameter is required.
        # >* If the cluster is a PolarDB for PostgreSQL cluster or a PolarDB for PostgreSQL (Compatible with Oracle) cluster, you do not need to specify this parameter. Secure Sockets Layer (SSL) encryption is enabled for all endpoints by default.
        self.net_type = net_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.pfs_instance_id = pfs_instance_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to enable automatic SSL certificate rotation. Valid values:
        # 
        # - **Enable**: Enables automatic rotation.
        # 
        # - **Disable**: Disables automatic rotation.
        self.sslauto_rotate = sslauto_rotate
        # The SSL status. Valid values:
        # * **Disable**: Shutdown of Secure Sockets Layer (SSL) encryption.
        # * **Enable**: Enables Secure Sockets Layer (SSL) encryption.
        # * **Update**: Updates the CA certificate.
        # 
        # > After you enable Secure Sockets Layer (SSL) encryption or update the CA certificate, you must download and configure the certificate. For details, see [Settings for SSL encryption](https://help.aliyun.com/document_detail/153182.html).
        self.sslenabled = sslenabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_valid_days is not None:
            result['CertValidDays'] = self.cert_valid_days

        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

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

        if self.pfs_instance_id is not None:
            result['PfsInstanceId'] = self.pfs_instance_id

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
        if m.get('CertValidDays') is not None:
            self.cert_valid_days = m.get('CertValidDays')

        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

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

        if m.get('PfsInstanceId') is not None:
            self.pfs_instance_id = m.get('PfsInstanceId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SSLAutoRotate') is not None:
            self.sslauto_rotate = m.get('SSLAutoRotate')

        if m.get('SSLEnabled') is not None:
            self.sslenabled = m.get('SSLEnabled')

        return self

