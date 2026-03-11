# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class CreateSandboxInput(DaraModel):
    def __init__(
        self,
        nas_config: main_models.NASConfig = None,
        oss_mount_config: main_models.OSSMountConfig = None,
        polar_fs_config: main_models.PolarFsConfig = None,
        sandbox_id: str = None,
        sandbox_idle_timeout_in_seconds: int = None,
        sandbox_idle_timeout_seconds: int = None,
        template_name: str = None,
    ):
        self.nas_config = nas_config
        self.oss_mount_config = oss_mount_config
        self.polar_fs_config = polar_fs_config
        self.sandbox_id = sandbox_id
        self.sandbox_idle_timeout_in_seconds = sandbox_idle_timeout_in_seconds
        # 沙箱空闲超时时间（秒）
        self.sandbox_idle_timeout_seconds = sandbox_idle_timeout_seconds
        # 模板名称（系统内部通过 templateName 查询 template_id）
        # 
        # This parameter is required.
        self.template_name = template_name

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
        if self.nas_config is not None:
            result['nasConfig'] = self.nas_config.to_map()

        if self.oss_mount_config is not None:
            result['ossMountConfig'] = self.oss_mount_config.to_map()

        if self.polar_fs_config is not None:
            result['polarFsConfig'] = self.polar_fs_config.to_map()

        if self.sandbox_id is not None:
            result['sandboxId'] = self.sandbox_id

        if self.sandbox_idle_timeout_in_seconds is not None:
            result['sandboxIdleTimeoutInSeconds'] = self.sandbox_idle_timeout_in_seconds

        if self.sandbox_idle_timeout_seconds is not None:
            result['sandboxIdleTimeoutSeconds'] = self.sandbox_idle_timeout_seconds

        if self.template_name is not None:
            result['templateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nasConfig') is not None:
            temp_model = main_models.NASConfig()
            self.nas_config = temp_model.from_map(m.get('nasConfig'))

        if m.get('ossMountConfig') is not None:
            temp_model = main_models.OSSMountConfig()
            self.oss_mount_config = temp_model.from_map(m.get('ossMountConfig'))

        if m.get('polarFsConfig') is not None:
            temp_model = main_models.PolarFsConfig()
            self.polar_fs_config = temp_model.from_map(m.get('polarFsConfig'))

        if m.get('sandboxId') is not None:
            self.sandbox_id = m.get('sandboxId')

        if m.get('sandboxIdleTimeoutInSeconds') is not None:
            self.sandbox_idle_timeout_in_seconds = m.get('sandboxIdleTimeoutInSeconds')

        if m.get('sandboxIdleTimeoutSeconds') is not None:
            self.sandbox_idle_timeout_seconds = m.get('sandboxIdleTimeoutSeconds')

        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')

        return self

