# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EngineVersionSupportedFeatures(DaraModel):
    def __init__(
        self,
        support_native_savepoint: bool = None,
        use_for_sql_deployments: bool = None,
    ):
        # Specifies whether the engine version can be used to create a native savepoint.
        self.support_native_savepoint = support_native_savepoint
        # Specifies whether the engine version can be used to submit an SQL deployment.
        self.use_for_sql_deployments = use_for_sql_deployments

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.support_native_savepoint is not None:
            result['supportNativeSavepoint'] = self.support_native_savepoint

        if self.use_for_sql_deployments is not None:
            result['useForSqlDeployments'] = self.use_for_sql_deployments

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('supportNativeSavepoint') is not None:
            self.support_native_savepoint = m.get('supportNativeSavepoint')

        if m.get('useForSqlDeployments') is not None:
            self.use_for_sql_deployments = m.get('useForSqlDeployments')

        return self

