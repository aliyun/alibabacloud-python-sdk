# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateGrafanaWorkspaceRequest(DaraModel):
    def __init__(
        self,
        aliyun_lang: str = None,
        description: str = None,
        grafana_workspace_id: str = None,
        grafana_workspace_name: str = None,
        region_id: str = None,
    ):
        # The language. Valid values: zh and en. Default value: zh.
        self.aliyun_lang = aliyun_lang
        # The description of the workspace.
        self.description = description
        # The ID of the workspace.
        # 
        # This parameter is required.
        self.grafana_workspace_id = grafana_workspace_id
        # The workspace name.
        self.grafana_workspace_name = grafana_workspace_name
        # The region ID. Default value: `cn-hangzhou`.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_lang is not None:
            result['AliyunLang'] = self.aliyun_lang

        if self.description is not None:
            result['Description'] = self.description

        if self.grafana_workspace_id is not None:
            result['GrafanaWorkspaceId'] = self.grafana_workspace_id

        if self.grafana_workspace_name is not None:
            result['GrafanaWorkspaceName'] = self.grafana_workspace_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunLang') is not None:
            self.aliyun_lang = m.get('AliyunLang')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GrafanaWorkspaceId') is not None:
            self.grafana_workspace_id = m.get('GrafanaWorkspaceId')

        if m.get('GrafanaWorkspaceName') is not None:
            self.grafana_workspace_name = m.get('GrafanaWorkspaceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

