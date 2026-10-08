# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateK8sSecretRequest(DaraModel):
    def __init__(
        self,
        base_64encoded: bool = None,
        cert_id: str = None,
        cert_region_id: str = None,
        cluster_id: str = None,
        data: str = None,
        name: str = None,
        namespace: str = None,
        type: str = None,
    ):
        # Specifies whether the data has been encoded in Base64.
        self.base_64encoded = base_64encoded
        # The ID of the certificate.
        self.cert_id = cert_id
        # The region ID of the certificate.
        self.cert_region_id = cert_region_id
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The data of the Secret. The value must be a JSON array that contains the following information:
        # 
        # - Key: Secret key
        # 
        # - Value: Secret value
        self.data = data
        # The name of the Secret. The name must start with a letter, and can contain digits, letters, and hyphens (-). It can be up to 63 characters in length.
        self.name = name
        # The namespace of the Kubernetes cluster.
        self.namespace = namespace
        # The type of the Secret. Valid values:
        # 
        # - Opaque: user-defined data type
        # 
        # - kubernetes.io/tls: Transport Layer Security (TLS) certificate type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_64encoded is not None:
            result['Base64Encoded'] = self.base_64encoded

        if self.cert_id is not None:
            result['CertId'] = self.cert_id

        if self.cert_region_id is not None:
            result['CertRegionId'] = self.cert_region_id

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.data is not None:
            result['Data'] = self.data

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Base64Encoded') is not None:
            self.base_64encoded = m.get('Base64Encoded')

        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')

        if m.get('CertRegionId') is not None:
            self.cert_region_id = m.get('CertRegionId')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

