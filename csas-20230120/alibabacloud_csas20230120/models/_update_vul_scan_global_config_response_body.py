# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class UpdateVulScanGlobalConfigResponseBody(DaraModel):
    def __init__(
        self,
        max_download_speed: int = None,
        request_id: str = None,
        wuying_vul_fix_config: main_models.UpdateVulScanGlobalConfigResponseBodyWuyingVulFixConfig = None,
    ):
        # The maximum download rate for vulnerability patches on a single user terminal device. Unit: Byte/s. A value of 0 indicates no speed limit.
        self.max_download_speed = max_download_speed
        # The ID of the request.
        self.request_id = request_id
        # The vulnerability fix configuration for WUYING Workspace. This configuration applies only to user terminal devices of the Cloud Desktop type.
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
            temp_model = main_models.UpdateVulScanGlobalConfigResponseBodyWuyingVulFixConfig()
            self.wuying_vul_fix_config = temp_model.from_map(m.get('WuyingVulFixConfig'))

        return self

class UpdateVulScanGlobalConfigResponseBodyWuyingVulFixConfig(DaraModel):
    def __init__(
        self,
        anti_shutdown_switch: bool = None,
        snapshot_switch: bool = None,
    ):
        # Specifies whether to prohibit shutdown during the fix process to prevent system exceptions caused by shutting down during patch installation. Valid values:
        # - **true**: Prohibit shutdown.
        # - **false**: Do not prohibit shutdown.
        self.anti_shutdown_switch = anti_shutdown_switch
        # Specifies whether to create a snapshot for the cloud desktop before the fix for rollback in case of fix failure. Valid values:
        # - **true**: Create a snapshot.
        # - **false**: Do not create a snapshot.
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

