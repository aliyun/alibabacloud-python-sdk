# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateVulScanGlobalConfigShrinkRequest(DaraModel):
    def __init__(
        self,
        max_download_speed: int = None,
        wuying_vul_fix_config_shrink: str = None,
    ):
        # The maximum download rate for vulnerability patches on a single user terminal device. Unit: Byte/s. A value of 0 indicates no speed limit.
        self.max_download_speed = max_download_speed
        # The vulnerability fix configuration for WUYING Workspace. This configuration applies only to user terminal devices of the Cloud Desktop type.
        self.wuying_vul_fix_config_shrink = wuying_vul_fix_config_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_download_speed is not None:
            result['MaxDownloadSpeed'] = self.max_download_speed

        if self.wuying_vul_fix_config_shrink is not None:
            result['WuyingVulFixConfig'] = self.wuying_vul_fix_config_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxDownloadSpeed') is not None:
            self.max_download_speed = m.get('MaxDownloadSpeed')

        if m.get('WuyingVulFixConfig') is not None:
            self.wuying_vul_fix_config_shrink = m.get('WuyingVulFixConfig')

        return self

