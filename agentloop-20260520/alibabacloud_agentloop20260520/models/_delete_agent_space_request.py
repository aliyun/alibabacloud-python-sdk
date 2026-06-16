# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAgentSpaceRequest(DaraModel):
    def __init__(
        self,
        delete_cms_workspace: bool = None,
        delete_mse_namespace: bool = None,
        delete_sls_project: bool = None,
    ):
        self.delete_cms_workspace = delete_cms_workspace
        self.delete_mse_namespace = delete_mse_namespace
        self.delete_sls_project = delete_sls_project

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delete_cms_workspace is not None:
            result['deleteCmsWorkspace'] = self.delete_cms_workspace

        if self.delete_mse_namespace is not None:
            result['deleteMseNamespace'] = self.delete_mse_namespace

        if self.delete_sls_project is not None:
            result['deleteSlsProject'] = self.delete_sls_project

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deleteCmsWorkspace') is not None:
            self.delete_cms_workspace = m.get('deleteCmsWorkspace')

        if m.get('deleteMseNamespace') is not None:
            self.delete_mse_namespace = m.get('deleteMseNamespace')

        if m.get('deleteSlsProject') is not None:
            self.delete_sls_project = m.get('deleteSlsProject')

        return self

