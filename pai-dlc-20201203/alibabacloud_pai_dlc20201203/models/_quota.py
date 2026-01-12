# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_pai_dlc20201203 import models as main_models
from darabonba.model import DaraModel

class Quota(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        quota_config: main_models.QuotaConfig = None,
        quota_id: str = None,
        quota_name: str = None,
        quota_type: str = None,
        total_quota: main_models.QuotaDetail = None,
        total_tide_quota: main_models.QuotaDetail = None,
        used_quota: main_models.QuotaDetail = None,
        used_tide_quota: main_models.QuotaDetail = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.quota_config = quota_config
        self.quota_id = quota_id
        self.quota_name = quota_name
        self.quota_type = quota_type
        self.total_quota = total_quota
        self.total_tide_quota = total_tide_quota
        self.used_quota = used_quota
        self.used_tide_quota = used_tide_quota

    def validate(self):
        if self.quota_config:
            self.quota_config.validate()
        if self.total_quota:
            self.total_quota.validate()
        if self.total_tide_quota:
            self.total_tide_quota.validate()
        if self.used_quota:
            self.used_quota.validate()
        if self.used_tide_quota:
            self.used_tide_quota.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.quota_config is not None:
            result['QuotaConfig'] = self.quota_config.to_map()

        if self.quota_id is not None:
            result['QuotaId'] = self.quota_id

        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name

        if self.quota_type is not None:
            result['QuotaType'] = self.quota_type

        if self.total_quota is not None:
            result['TotalQuota'] = self.total_quota.to_map()

        if self.total_tide_quota is not None:
            result['TotalTideQuota'] = self.total_tide_quota.to_map()

        if self.used_quota is not None:
            result['UsedQuota'] = self.used_quota.to_map()

        if self.used_tide_quota is not None:
            result['UsedTideQuota'] = self.used_tide_quota.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('QuotaConfig') is not None:
            temp_model = main_models.QuotaConfig()
            self.quota_config = temp_model.from_map(m.get('QuotaConfig'))

        if m.get('QuotaId') is not None:
            self.quota_id = m.get('QuotaId')

        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')

        if m.get('QuotaType') is not None:
            self.quota_type = m.get('QuotaType')

        if m.get('TotalQuota') is not None:
            temp_model = main_models.QuotaDetail()
            self.total_quota = temp_model.from_map(m.get('TotalQuota'))

        if m.get('TotalTideQuota') is not None:
            temp_model = main_models.QuotaDetail()
            self.total_tide_quota = temp_model.from_map(m.get('TotalTideQuota'))

        if m.get('UsedQuota') is not None:
            temp_model = main_models.QuotaDetail()
            self.used_quota = temp_model.from_map(m.get('UsedQuota'))

        if m.get('UsedTideQuota') is not None:
            temp_model = main_models.QuotaDetail()
            self.used_tide_quota = temp_model.from_map(m.get('UsedTideQuota'))

        return self

