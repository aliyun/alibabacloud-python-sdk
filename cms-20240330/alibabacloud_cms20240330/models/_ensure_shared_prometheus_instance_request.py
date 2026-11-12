# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnsureSharedPrometheusInstanceRequest(DaraModel):
    def __init__(
        self,
        aliyun_lang: str = None,
        share_scope: str = None,
        workspace: str = None,
    ):
        # The language of the returned information. zh indicates Chinese, and en indicates English. Default value: zh.
        self.aliyun_lang = aliyun_lang
        # The share scope. Currently, only Workspace is supported, which indicates the shared Prometheus instance for the workspace in the requested region. Workspaces in the same region share the same instance, and no additional instances are created. Policy and Environment are not currently supported.
        # 
        # This parameter is required.
        self.share_scope = share_scope
        # The name of the workspace. If the workspace does not exist, a 404 error is returned.
        # 
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_lang is not None:
            result['aliyunLang'] = self.aliyun_lang

        if self.share_scope is not None:
            result['shareScope'] = self.share_scope

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliyunLang') is not None:
            self.aliyun_lang = m.get('aliyunLang')

        if m.get('shareScope') is not None:
            self.share_scope = m.get('shareScope')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

