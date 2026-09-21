# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetWorkspaceAgenticFsMountRamAuthorizeUrlRequest(DaraModel):
    def __init__(
        self,
        access_point_id: str = None,
        file_system_id: str = None,
        server: str = None,
    ):
        # The ID of the target NAS AccessPoint. This parameter corresponds to the server and fileSystemId parameters.
        # 
        # This parameter is required.
        self.access_point_id = access_point_id
        # The ID of the NAS file system to which the target AccessPoint belongs. This parameter corresponds to the server and accessPointId parameters.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The domain name of the target AccessPoint, obtained from the DomainName field of the NAS ListAccessPoints operation. Do not include the protocol, port, or path.
        # 
        # This parameter is required.
        self.server = server

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_point_id is not None:
            result['accessPointId'] = self.access_point_id

        if self.file_system_id is not None:
            result['fileSystemId'] = self.file_system_id

        if self.server is not None:
            result['server'] = self.server

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessPointId') is not None:
            self.access_point_id = m.get('accessPointId')

        if m.get('fileSystemId') is not None:
            self.file_system_id = m.get('fileSystemId')

        if m.get('server') is not None:
            self.server = m.get('server')

        return self

