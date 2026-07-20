# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class UpdateSessionInput(DaraModel):
    def __init__(
        self,
        allow_internet_access: bool = None,
        disable_session_id_reuse: bool = None,
        enable_auto_pause: bool = None,
        enable_auto_resume: bool = None,
        juice_fs_config: main_models.JuiceFsConfig = None,
        nas_config: main_models.NASConfig = None,
        network: main_models.UpdateSessionNetworkConfig = None,
        oss_mount_config: main_models.OSSMountConfig = None,
        polar_fs_config: main_models.PolarFsConfig = None,
        session_idle_timeout_in_seconds: int = None,
        session_ttlin_seconds: int = None,
    ):
        self.allow_internet_access = allow_internet_access
        # Specifies whether to disable session ID reuse after the session expires. Default value: False, which indicates that after a session expires, you can use the same session ID to initiate requests. The system treats the request as a new session and binds it to a new instance. If you set this parameter to True, the session ID cannot be reused after the session expires.
        self.disable_session_id_reuse = disable_session_id_reuse
        self.enable_auto_pause = enable_auto_pause
        self.enable_auto_resume = enable_auto_resume
        self.juice_fs_config = juice_fs_config
        self.nas_config = nas_config
        self.network = network
        self.oss_mount_config = oss_mount_config
        self.polar_fs_config = polar_fs_config
        # The session idle timeout.
        self.session_idle_timeout_in_seconds = session_idle_timeout_in_seconds
        # The session lifetime.
        self.session_ttlin_seconds = session_ttlin_seconds

    def validate(self):
        if self.juice_fs_config:
            self.juice_fs_config.validate()
        if self.nas_config:
            self.nas_config.validate()
        if self.network:
            self.network.validate()
        if self.oss_mount_config:
            self.oss_mount_config.validate()
        if self.polar_fs_config:
            self.polar_fs_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_internet_access is not None:
            result['allowInternetAccess'] = self.allow_internet_access

        if self.disable_session_id_reuse is not None:
            result['disableSessionIdReuse'] = self.disable_session_id_reuse

        if self.enable_auto_pause is not None:
            result['enableAutoPause'] = self.enable_auto_pause

        if self.enable_auto_resume is not None:
            result['enableAutoResume'] = self.enable_auto_resume

        if self.juice_fs_config is not None:
            result['juiceFsConfig'] = self.juice_fs_config.to_map()

        if self.nas_config is not None:
            result['nasConfig'] = self.nas_config.to_map()

        if self.network is not None:
            result['network'] = self.network.to_map()

        if self.oss_mount_config is not None:
            result['ossMountConfig'] = self.oss_mount_config.to_map()

        if self.polar_fs_config is not None:
            result['polarFsConfig'] = self.polar_fs_config.to_map()

        if self.session_idle_timeout_in_seconds is not None:
            result['sessionIdleTimeoutInSeconds'] = self.session_idle_timeout_in_seconds

        if self.session_ttlin_seconds is not None:
            result['sessionTTLInSeconds'] = self.session_ttlin_seconds

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowInternetAccess') is not None:
            self.allow_internet_access = m.get('allowInternetAccess')

        if m.get('disableSessionIdReuse') is not None:
            self.disable_session_id_reuse = m.get('disableSessionIdReuse')

        if m.get('enableAutoPause') is not None:
            self.enable_auto_pause = m.get('enableAutoPause')

        if m.get('enableAutoResume') is not None:
            self.enable_auto_resume = m.get('enableAutoResume')

        if m.get('juiceFsConfig') is not None:
            temp_model = main_models.JuiceFsConfig()
            self.juice_fs_config = temp_model.from_map(m.get('juiceFsConfig'))

        if m.get('nasConfig') is not None:
            temp_model = main_models.NASConfig()
            self.nas_config = temp_model.from_map(m.get('nasConfig'))

        if m.get('network') is not None:
            temp_model = main_models.UpdateSessionNetworkConfig()
            self.network = temp_model.from_map(m.get('network'))

        if m.get('ossMountConfig') is not None:
            temp_model = main_models.OSSMountConfig()
            self.oss_mount_config = temp_model.from_map(m.get('ossMountConfig'))

        if m.get('polarFsConfig') is not None:
            temp_model = main_models.PolarFsConfig()
            self.polar_fs_config = temp_model.from_map(m.get('polarFsConfig'))

        if m.get('sessionIdleTimeoutInSeconds') is not None:
            self.session_idle_timeout_in_seconds = m.get('sessionIdleTimeoutInSeconds')

        if m.get('sessionTTLInSeconds') is not None:
            self.session_ttlin_seconds = m.get('sessionTTLInSeconds')

        return self

