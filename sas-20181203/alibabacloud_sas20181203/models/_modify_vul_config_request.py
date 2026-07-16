# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyVulConfigRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        type: str = None,
    ):
        # Specifies whether to enable or disable vulnerability detection. Valid values:
        # 
        # - **on**: Enable vulnerability detection.
        # - **off**: Disable vulnerability detection.
        # 
        # > If the type is set to real risk, valid values:
        # > - **real**: Real risk vulnerabilities.
        # > - **all**: All vulnerabilities.
        self.config = config
        # The type of vulnerability to modify. Valid values:
        # 
        # - **cve**: Linux vulnerability
        # - **sys**: Windows vulnerability
        # - **cms**: WebCMS vulnerability
        # - **emg**: emergency vulnerability
        # - **app**: application vulnerability
        # - **yum**: YUM/APT source configuration
        # - **scanMode**: real risk.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

