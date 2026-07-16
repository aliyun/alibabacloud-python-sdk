# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class Session(DaraModel):
    def __init__(
        self,
        container_id: str = None,
        created_time: str = None,
        disable_session_id_reuse: bool = None,
        enable_auto_pause: bool = None,
        enable_auto_resume: bool = None,
        function_name: str = None,
        juice_fs_config: main_models.JuiceFsConfig = None,
        last_modified_time: str = None,
        nas_config: main_models.NASConfig = None,
        oss_mount_config: main_models.OSSMountConfig = None,
        polar_fs_config: main_models.PolarFsConfig = None,
        qualifier: str = None,
        session_affinity_type: str = None,
        session_id: str = None,
        session_idle_timeout_in_seconds: int = None,
        session_status: str = None,
        session_ttlin_seconds: int = None,
    ):
        # The instance ID of the function instance associated with the session.
        self.container_id = container_id
        # The time when the session was created.
        self.created_time = created_time
        # Specifies whether to disable session ID reuse. Default value: False, which indicates that after the session expires, you can use the same session ID to initiate requests. The system treats the request as a new session and binds it to a new instance. If you set this parameter to True, the session ID cannot be reused after the session expires.
        self.disable_session_id_reuse = disable_session_id_reuse
        self.enable_auto_pause = enable_auto_pause
        self.enable_auto_resume = enable_auto_resume
        # The name of the function to which the session belongs.
        self.function_name = function_name
        self.juice_fs_config = juice_fs_config
        # The time when the session was last updated.
        self.last_modified_time = last_modified_time
        # The NAS configuration. After configuration, the instance associated with the session can access the specified NAS resource.
        self.nas_config = nas_config
        self.oss_mount_config = oss_mount_config
        self.polar_fs_config = polar_fs_config
        # The qualifier passed in when the customer created the session. If not specified, the default value is LATEST.
        self.qualifier = qualifier
        # The session affinity type.
        self.session_affinity_type = session_affinity_type
        # The unique identifier of the function session.
        self.session_id = session_id
        # The idle timeout period of the session.
        self.session_idle_timeout_in_seconds = session_idle_timeout_in_seconds
        # The session status. Valid values:
        # - Active: The session is valid.
        # - Expired: The session has expired.
        self.session_status = session_status
        # The maximum lifetime of the session.
        self.session_ttlin_seconds = session_ttlin_seconds

    def validate(self):
        if self.juice_fs_config:
            self.juice_fs_config.validate()
        if self.nas_config:
            self.nas_config.validate()
        if self.oss_mount_config:
            self.oss_mount_config.validate()
        if self.polar_fs_config:
            self.polar_fs_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.container_id is not None:
            result['containerId'] = self.container_id

        if self.created_time is not None:
            result['createdTime'] = self.created_time

        if self.disable_session_id_reuse is not None:
            result['disableSessionIdReuse'] = self.disable_session_id_reuse

        if self.enable_auto_pause is not None:
            result['enableAutoPause'] = self.enable_auto_pause

        if self.enable_auto_resume is not None:
            result['enableAutoResume'] = self.enable_auto_resume

        if self.function_name is not None:
            result['functionName'] = self.function_name

        if self.juice_fs_config is not None:
            result['juiceFsConfig'] = self.juice_fs_config.to_map()

        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time

        if self.nas_config is not None:
            result['nasConfig'] = self.nas_config.to_map()

        if self.oss_mount_config is not None:
            result['ossMountConfig'] = self.oss_mount_config.to_map()

        if self.polar_fs_config is not None:
            result['polarFsConfig'] = self.polar_fs_config.to_map()

        if self.qualifier is not None:
            result['qualifier'] = self.qualifier

        if self.session_affinity_type is not None:
            result['sessionAffinityType'] = self.session_affinity_type

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.session_idle_timeout_in_seconds is not None:
            result['sessionIdleTimeoutInSeconds'] = self.session_idle_timeout_in_seconds

        if self.session_status is not None:
            result['sessionStatus'] = self.session_status

        if self.session_ttlin_seconds is not None:
            result['sessionTTLInSeconds'] = self.session_ttlin_seconds

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('containerId') is not None:
            self.container_id = m.get('containerId')

        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')

        if m.get('disableSessionIdReuse') is not None:
            self.disable_session_id_reuse = m.get('disableSessionIdReuse')

        if m.get('enableAutoPause') is not None:
            self.enable_auto_pause = m.get('enableAutoPause')

        if m.get('enableAutoResume') is not None:
            self.enable_auto_resume = m.get('enableAutoResume')

        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')

        if m.get('juiceFsConfig') is not None:
            temp_model = main_models.JuiceFsConfig()
            self.juice_fs_config = temp_model.from_map(m.get('juiceFsConfig'))

        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')

        if m.get('nasConfig') is not None:
            temp_model = main_models.NASConfig()
            self.nas_config = temp_model.from_map(m.get('nasConfig'))

        if m.get('ossMountConfig') is not None:
            temp_model = main_models.OSSMountConfig()
            self.oss_mount_config = temp_model.from_map(m.get('ossMountConfig'))

        if m.get('polarFsConfig') is not None:
            temp_model = main_models.PolarFsConfig()
            self.polar_fs_config = temp_model.from_map(m.get('polarFsConfig'))

        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')

        if m.get('sessionAffinityType') is not None:
            self.session_affinity_type = m.get('sessionAffinityType')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('sessionIdleTimeoutInSeconds') is not None:
            self.session_idle_timeout_in_seconds = m.get('sessionIdleTimeoutInSeconds')

        if m.get('sessionStatus') is not None:
            self.session_status = m.get('sessionStatus')

        if m.get('sessionTTLInSeconds') is not None:
            self.session_ttlin_seconds = m.get('sessionTTLInSeconds')

        return self

