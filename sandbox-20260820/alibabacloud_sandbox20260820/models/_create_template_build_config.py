# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sandbox20260820 import models as main_models
from darabonba.model import DaraModel

class CreateTemplateBuildConfig(DaraModel):
    def __init__(
        self,
        copy: main_models.CreateTemplateCopyAction = None,
        envd_inject: main_models.CreateTemplateEnvdInjectAction = None,
        install_storage_clients: bool = None,
    ):
        # The action configuration for pulling the source image and pushing it to the destination repository.
        self.copy = copy
        # The action configuration for packaging the envd daemon process into the image. This is an optional intermediate step in the copy process and is supported only by first-generation sandboxes.
        self.envd_inject = envd_inject
        # The installation of clients required for storage mounting.
        self.install_storage_clients = install_storage_clients

    def validate(self):
        if self.copy:
            self.copy.validate()
        if self.envd_inject:
            self.envd_inject.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.copy is not None:
            result['copy'] = self.copy.to_map()

        if self.envd_inject is not None:
            result['envdInject'] = self.envd_inject.to_map()

        if self.install_storage_clients is not None:
            result['installStorageClients'] = self.install_storage_clients

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('copy') is not None:
            temp_model = main_models.CreateTemplateCopyAction()
            self.copy = temp_model.from_map(m.get('copy'))

        if m.get('envdInject') is not None:
            temp_model = main_models.CreateTemplateEnvdInjectAction()
            self.envd_inject = temp_model.from_map(m.get('envdInject'))

        if m.get('installStorageClients') is not None:
            self.install_storage_clients = m.get('installStorageClients')

        return self

