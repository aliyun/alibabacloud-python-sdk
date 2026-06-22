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
        # Settings for the types of vulnerabilities to detect by using the one-click scan feature. Valid values:
        # - **cve**: Linux software vulnerability.
        # - **sys**: Windows system vulnerability.
        # - **cms**: Web-CMS vulnerability.
        # - **app**: Application vulnerability detected by the web scanner.
        # - **emg**: Emergency vulnerability.
        # - **image**: Container image vulnerability.
        # - **sca**: Application vulnerability detected by software constituency parsing.
        # > If this parameter is left empty, all vulnerability types are detected.
        self.types = types
        # The list of server UUIDs. Separate multiple UUIDs with commas (,).
        # 
        # > You can call the [DescribeCloudCenterInstances](https://help.aliyun.com/document_detail/421726.html) operation to obtain this parameter.
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

