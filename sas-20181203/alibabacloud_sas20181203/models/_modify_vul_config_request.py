# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyVulConfigRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        config: str = None,
        dry_run: bool = None,
        type: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. Different requests must use different tokens. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # Specifies whether to enable or disable vulnerability detection. Valid values:
        # 
        # - **on**: Enables vulnerability detection.
        # - **off**: Disables vulnerability detection.
        # 
        # > If the type is set to real risk, valid values:
        # > - **real**: Real risk vulnerabilities.
        # > - **all**: All vulnerabilities.
        self.config = config
        # Specifies whether to perform only a dry run of the request. Valid values: true: performs only a dry run without performing the actual operation. false: performs the actual request. Default value: false.
        self.dry_run = dry_run
        # The type of vulnerability to modify. Valid values:
        # 
        # - **cve**: Linux software vulnerability
        # - **sys**: Windows system vulnerability
        # - **cms**: Web-CMS vulnerability
        # - **emg**: emergency vulnerability
        # - **app**: application vulnerability
        # - **yum**: YUM/APT source configuration
        # - **scanMode**: real risk
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.config is not None:
            result['Config'] = self.config

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

