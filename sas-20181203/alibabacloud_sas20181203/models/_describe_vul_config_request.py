# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVulConfigRequest(DaraModel):
    def __init__(
        self,
        source_ip: str = None,
        type: str = None,
    ):
        # The source IP address of the request.
        self.source_ip = source_ip
        # The type of configuration. By default, all types of configurations are queried. Valid values:
        # 
        # *   **cve**: Linux software vulnerability.
        # *   **sys**: Windows system vulnerability.
        # *   **cms**: Web-CMS vulnerability.
        # *   **app**: application vulnerability that is detected by using web scanner.
        # *   **emg**: urgent vulnerability.
        # *   **scanMode**: displays easily exploitable vulnerability.
        # *   **imageVulClean**: vulnerability retention duration.
        # *   **yum**: preferentially uses YUM or APT sources of Alibaba Cloud to fix vulnerabilities.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

