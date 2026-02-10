# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyStartVulScanRequest(DaraModel):
    def __init__(
        self,
        types: str = None,
        uuids: str = None,
    ):
        # The types of vulnerabilities that can be detected. Valid values:
        # 
        # *   **cve**: Linux software vulnerabilities
        # *   **sys**: Windows system vulnerabilities
        # *   **cms**: Web-CMS vulnerabilities
        # *   **app**: application vulnerabilities
        # *   **emg**: urgent vulnerabilities
        # *   **image**: container image vulnerabilities
        # *   **sca**: vulnerabilities that are detected based on software component analysis
        # 
        # > If you leave this parameter empty, all types of vulnerabilities can be detected.
        self.types = types
        # The UUIDs of servers.
        self.uuids = uuids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.types is not None:
            result['Types'] = self.types

        if self.uuids is not None:
            result['Uuids'] = self.uuids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Types') is not None:
            self.types = m.get('Types')

        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')

        return self

