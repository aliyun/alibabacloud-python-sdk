# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetClusterScannerYamlResponseBody(DaraModel):
    def __init__(
        self,
        ca_cert_base_64: str = None,
        cluster_env_info: str = None,
        cluster_id: str = None,
        image: str = None,
        request_id: str = None,
        tls_cert_base_64: str = None,
        tls_key_base_64: str = None,
        webhook_open: int = None,
    ):
        # Base64 encoded CA certificate.
        self.ca_cert_base_64 = ca_cert_base_64
        # Cluster environment information.
        self.cluster_env_info = cluster_env_info
        # The ID of the cluster that you want to scan.
        self.cluster_id = cluster_id
        # The name of the image.
        self.image = image
        # The request ID.
        self.request_id = request_id
        # Base64 encoded webhook certificate.
        self.tls_cert_base_64 = tls_cert_base_64
        # Base64 encoded webhook private key.
        self.tls_key_base_64 = tls_key_base_64
        # Indicates whether the incremental scan switch is enabled. Values:
        # - **0**: Not enabled
        # - **1**: Enabled
        self.webhook_open = webhook_open

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ca_cert_base_64 is not None:
            result['CaCertBase64'] = self.ca_cert_base_64

        if self.cluster_env_info is not None:
            result['ClusterEnvInfo'] = self.cluster_env_info

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.image is not None:
            result['Image'] = self.image

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.tls_cert_base_64 is not None:
            result['TlsCertBase64'] = self.tls_cert_base_64

        if self.tls_key_base_64 is not None:
            result['TlsKeyBase64'] = self.tls_key_base_64

        if self.webhook_open is not None:
            result['WebhookOpen'] = self.webhook_open

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaCertBase64') is not None:
            self.ca_cert_base_64 = m.get('CaCertBase64')

        if m.get('ClusterEnvInfo') is not None:
            self.cluster_env_info = m.get('ClusterEnvInfo')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TlsCertBase64') is not None:
            self.tls_cert_base_64 = m.get('TlsCertBase64')

        if m.get('TlsKeyBase64') is not None:
            self.tls_key_base_64 = m.get('TlsKeyBase64')

        if m.get('WebhookOpen') is not None:
            self.webhook_open = m.get('WebhookOpen')

        return self

