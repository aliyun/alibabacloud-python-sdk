# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class GetVulScanGlobalConfigResponseBody(DaraModel):
    def __init__(
        self,
        max_download_speed: int = None,
        request_id: str = None,
        wuying_vul_fix_config: main_models.GetVulScanGlobalConfigResponseBodyWuyingVulFixConfig = None,
    ):
        # The maximum download speed for vulnerability patches on a single user terminal device. Unit: bytes per second. A value of 0 indicates no speed limit.
        self.max_download_speed = max_download_speed
        # The request ID.
        self.request_id = request_id
        # The vulnerability fix configuration for WUYING Workspace. This configuration takes effect only on user terminal devices of the Cloud Desktop type.
        self.wuying_vul_fix_config = wuying_vul_fix_config

    def validate(self):
        if self.wuying_vul_fix_config:
            self.wuying_vul_fix_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_download_speed is not None:
            result['MaxDownloadSpeed'] = self.max_download_speed

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.wuying_vul_fix_config is not None:
            result['WuyingVulFixConfig'] = self.wuying_vul_fix_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxDownloadSpeed') is not None:
            self.max_download_speed = m.get('MaxDownloadSpeed')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('WuyingVulFixConfig') is not None:
            temp_model = main_models.GetVulScanGlobalConfigResponseBodyWuyingVulFixConfig()
            self.wuying_vul_fix_config = temp_model.from_map(m.get('WuyingVulFixConfig'))

        return self

class GetVulScanGlobalConfigResponseBodyWuyingVulFixConfig(DaraModel):
    def __init__(
        self,
        anti_shutdown_switch: bool = None,
        snapshot_switch: bool = None,
    ):
        # Specifies whether to prohibit shutdown during the fix process to prevent system exceptions caused by shutting down during patch installation. Valid values:
        # - **true**: Shutdown is prohibited.
        # - **false**: Shutdown is not prohibited.
        self.anti_shutdown_switch = anti_shutdown_switch
        # Specifies whether to create a snapshot for the cloud desktop before the fix, which can be used for rollback if the fix fails. Valid values:
        # - **true**: A snapshot is created.
        # - **false**: No snapshot is created.
        self.snapshot_switch = snapshot_switch

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.anti_shutdown_switch is not None:
            result['AntiShutdownSwitch'] = self.anti_shutdown_switch

        if self.snapshot_switch is not None:
            result['SnapshotSwitch'] = self.snapshot_switch

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntiShutdownSwitch') is not None:
            self.anti_shutdown_switch = m.get('AntiShutdownSwitch')

        if m.get('SnapshotSwitch') is not None:
            self.snapshot_switch = m.get('SnapshotSwitch')

        return self

