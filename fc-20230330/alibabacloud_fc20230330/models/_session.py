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
        function_name: str = None,
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
        self.container_id = container_id
        self.created_time = created_time
        self.disable_session_id_reuse = disable_session_id_reuse
        self.function_name = function_name
        self.last_modified_time = last_modified_time
        self.nas_config = nas_config
        self.oss_mount_config = oss_mount_config
        self.polar_fs_config = polar_fs_config
        self.qualifier = qualifier
        self.session_affinity_type = session_affinity_type
        self.session_id = session_id
        self.session_idle_timeout_in_seconds = session_idle_timeout_in_seconds
        self.session_status = session_status
        self.session_ttlin_seconds = session_ttlin_seconds

    def validate(self):
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

        if self.function_name is not None:
            result['functionName'] = self.function_name

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

        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')

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

