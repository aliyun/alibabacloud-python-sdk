# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sandbox20260820 import models as main_models
from darabonba.model import DaraModel

class PublicUpdateTemplateRuntimeConfig(DaraModel):
    def __init__(
        self,
        cpu: float = None,
        disk_size: int = None,
        internet_access: bool = None,
        log_config: main_models.PublicUpdateTemplateLogConfig = None,
        memory_size: int = None,
        sandbox_config: main_models.PublicUpdateTemplateSandboxConfig = None,
        vpc_bindings: List[str] = None,
        vpc_config: main_models.PublicUpdateTemplateVPCConfig = None,
    ):
        # The number of vCPU cores.
        self.cpu = cpu
        # The size of the system cloud disk in MB.
        self.disk_size = disk_size
        # Specifies whether the sandbox is allowed to access the Internet.
        self.internet_access = internet_access
        # The log configuration.
        self.log_config = log_config
        # The memory size in MB.
        self.memory_size = memory_size
        # The sandbox configuration.
        self.sandbox_config = sandbox_config
        # Supported only for generation 2 templates. Omitting this field or setting it to null retains the original list. A non-empty array replaces the entire allowed set. An explicit empty array [] clears the inbound VPC restrictions for the new version. This field is independent of vpcConfig. An empty request body {}, an empty runtimeConfig, or a runtimeConfig containing only vpcBindings: null returns a 400 error and does not clear the bindings. The actual JSON received by the server prevails. An empty array omitted by the SDK cannot clear the list. If the target is a generation 1 template, explicitly passing an empty or non-empty array returns a 400 error. If non-empty bindings already exist, you must first clear them on the generation 2 template and wait for the update to succeed before switching to generation 1.
        self.vpc_bindings = vpc_bindings
        # The VPC network configuration.
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

        if self.vpc_bindings is not None:
            result['vpcBindings'] = self.vpc_bindings

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
            temp_model = main_models.PublicUpdateTemplateLogConfig()
            self.log_config = temp_model.from_map(m.get('logConfig'))

        if m.get('memorySize') is not None:
            self.memory_size = m.get('memorySize')

        if m.get('sandboxConfig') is not None:
            temp_model = main_models.PublicUpdateTemplateSandboxConfig()
            self.sandbox_config = temp_model.from_map(m.get('sandboxConfig'))

        if m.get('vpcBindings') is not None:
            self.vpc_bindings = m.get('vpcBindings')

        if m.get('vpcConfig') is not None:
            temp_model = main_models.PublicUpdateTemplateVPCConfig()
            self.vpc_config = temp_model.from_map(m.get('vpcConfig'))

        return self

