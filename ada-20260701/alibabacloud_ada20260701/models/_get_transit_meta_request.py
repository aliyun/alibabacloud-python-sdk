# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTransitMetaRequest(DaraModel):
    def __init__(
        self,
        expire_ms: int = None,
        file_path: str = None,
        network: str = None,
        transit_id: str = None,
    ):
        # The validity period of the temporary download URL, in milliseconds. The value must be an integer greater than or equal to 1000 and is rounded down to the nearest whole second. If `ExpireMs` is not specified, the default validity period is `900000` milliseconds (15 minutes). A download URL is generated only when `Network` is specified.
        self.expire_ms = expire_ms
        # The opaque object path returned by `CreateTransitUploadPolicy`. Specify at least one of this parameter and `TransitId`.
        self.file_path = file_path
        # The network type for the download URL. Valid values: `public` and `internal`. If this parameter is not specified, no download URL is generated.
        self.network = network
        # The Transit ID. Specify at least one of this parameter and `FilePath`. If both are specified, this parameter takes precedence.
        self.transit_id = transit_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expire_ms is not None:
            result['ExpireMs'] = self.expire_ms

        if self.file_path is not None:
            result['FilePath'] = self.file_path

        if self.network is not None:
            result['Network'] = self.network

        if self.transit_id is not None:
            result['TransitId'] = self.transit_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireMs') is not None:
            self.expire_ms = m.get('ExpireMs')

        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        if m.get('Network') is not None:
            self.network = m.get('Network')

        if m.get('TransitId') is not None:
            self.transit_id = m.get('TransitId')

        return self

