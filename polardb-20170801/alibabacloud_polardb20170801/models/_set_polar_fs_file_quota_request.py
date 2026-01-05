# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class SetPolarFsFileQuotaRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        file_path_quotas: List[main_models.SetPolarFsFileQuotaRequestFilePathQuotas] = None,
        polar_fs_instance_id: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        # This parameter is required.
        self.file_path_quotas = file_path_quotas
        # This parameter is required.
        self.polar_fs_instance_id = polar_fs_instance_id

    def validate(self):
        if self.file_path_quotas:
            for v1 in self.file_path_quotas:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        result['FilePathQuotas'] = []
        if self.file_path_quotas is not None:
            for k1 in self.file_path_quotas:
                result['FilePathQuotas'].append(k1.to_map() if k1 else None)

        if self.polar_fs_instance_id is not None:
            result['PolarFsInstanceId'] = self.polar_fs_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        self.file_path_quotas = []
        if m.get('FilePathQuotas') is not None:
            for k1 in m.get('FilePathQuotas'):
                temp_model = main_models.SetPolarFsFileQuotaRequestFilePathQuotas()
                self.file_path_quotas.append(temp_model.from_map(k1))

        if m.get('PolarFsInstanceId') is not None:
            self.polar_fs_instance_id = m.get('PolarFsInstanceId')

        return self

class SetPolarFsFileQuotaRequestFilePathQuotas(DaraModel):
    def __init__(
        self,
        file_path_id: str = None,
        max_depth: int = None,
        quota_ids: str = None,
        strategy: str = None,
    ):
        self.file_path_id = file_path_id
        self.max_depth = max_depth
        self.quota_ids = quota_ids
        self.strategy = strategy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_path_id is not None:
            result['FilePathId'] = self.file_path_id

        if self.max_depth is not None:
            result['MaxDepth'] = self.max_depth

        if self.quota_ids is not None:
            result['QuotaIds'] = self.quota_ids

        if self.strategy is not None:
            result['Strategy'] = self.strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilePathId') is not None:
            self.file_path_id = m.get('FilePathId')

        if m.get('MaxDepth') is not None:
            self.max_depth = m.get('MaxDepth')

        if m.get('QuotaIds') is not None:
            self.quota_ids = m.get('QuotaIds')

        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')

        return self

