# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetLogviewDownloadUrlRequest(DaraModel):
    def __init__(
        self,
        use_vpc_endpoint: bool = None,
    ):
        # Specifies whether to use the OSS VPC endpoint to generate the download link. Valid values:
        # - false: Uses the default OSS endpoint.
        # - true: Uses the OSS VPC endpoint configured on the server. The download client must have network access to this endpoint.
        # Default value: false. If this parameter is set to true and no OSS VPC endpoint is configured on the server, link generation fails and does not automatically fall back.
        self.use_vpc_endpoint = use_vpc_endpoint

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.use_vpc_endpoint is not None:
            result['useVpcEndpoint'] = self.use_vpc_endpoint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('useVpcEndpoint') is not None:
            self.use_vpc_endpoint = m.get('useVpcEndpoint')

        return self

