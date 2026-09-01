# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_fcsandbox20260509 import models as main_models
from darabonba.model import DaraModel

class CreateTemplateRuntimeConfig(DaraModel):
    def __init__(
        self,
        cpu: float = None,
        disk_size: int = None,
        internet_access: bool = None,
        log_config: main_models.CreateTemplateLogConfig = None,
        memory_size: int = None,
        sandbox_config: main_models.CreateTemplateSandboxConfig = None,
        vpc_config: main_models.CreateTemplateVPCConfig = None,
    ):
        # The number of CPU cores.
        self.cpu = cpu
        # The disk size. Unit: GB.
        self.disk_size = disk_size
        # Specifies whether to allow access to the Internet.
        self.internet_access = internet_access
        # The log configuration.
        self.log_config = log_config
        # The memory size. Unit: MB.
        self.memory_size = memory_size
        # The sandbox configuration.
        self.sandbox_config = sandbox_config
        # The VPC configuration.
        self.vpc_config = vpc_config

    def validate(self):
        if self.log_config:
            self.log_config.validate()
        if self.sandbox_config:
            self.sandbox_config.validate()
        if self.vpc_config:
            self.vpc_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['cpu'] = self.cpu

        if self.disk_size is not None:
            result['diskSize'] = self.disk_size

        if self.internet_access is not None:
            result['internetAccess'] = self.internet_access

        if self.log_config is not None:
            result['logConfig'] = self.log_config.to_map()

        if self.memory_size is not None:
            result['memorySize'] = self.memory_size

        if self.sandbox_config is not None:
            result['sandboxConfig'] = self.sandbox_config.to_map()

        if self.vpc_config is not None:
            result['vpcConfig'] = self.vpc_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')

        if m.get('diskSize') is not None:
            self.disk_size = m.get('diskSize')

        if m.get('internetAccess') is not None:
            self.internet_access = m.get('internetAccess')

        if m.get('logConfig') is not None:
            temp_model = main_models.CreateTemplateLogConfig()
            self.log_config = temp_model.from_map(m.get('logConfig'))

        if m.get('memorySize') is not None:
            self.memory_size = m.get('memorySize')

        if m.get('sandboxConfig') is not None:
            temp_model = main_models.CreateTemplateSandboxConfig()
            self.sandbox_config = temp_model.from_map(m.get('sandboxConfig'))

        if m.get('vpcConfig') is not None:
            temp_model = main_models.CreateTemplateVPCConfig()
            self.vpc_config = temp_model.from_map(m.get('vpcConfig'))

        return self

