# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetSparkAppLogRootPathRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        oss_log_path: str = None,
        use_default_oss: bool = None,
    ):
        # The ID of the AnalyticDB for MySQL cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The path of Object Storage Service (OSS) logs.
        self.oss_log_path = oss_log_path
        # Specifies whether to use the default OSS log path.
        self.use_default_oss = use_default_oss

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.oss_log_path is not None:
            result['OssLogPath'] = self.oss_log_path

        if self.use_default_oss is not None:
            result['UseDefaultOss'] = self.use_default_oss

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('OssLogPath') is not None:
            self.oss_log_path = m.get('OssLogPath')

        if m.get('UseDefaultOss') is not None:
            self.use_default_oss = m.get('UseDefaultOss')

        return self

