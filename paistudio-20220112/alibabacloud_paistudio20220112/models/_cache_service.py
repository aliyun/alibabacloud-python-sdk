# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class CacheService(DaraModel):
    def __init__(
        self,
        cache_infos: List[main_models.CacheInfo] = None,
        cache_service_id: str = None,
        created_by: str = None,
        gmt_created: str = None,
        quota_id: str = None,
        status: str = None,
        supported_client_quota_ids: List[str] = None,
        tenant_id: str = None,
        user_id: str = None,
        user_vpc: main_models.UserVpc = None,
    ):
        self.cache_infos = cache_infos
        self.cache_service_id = cache_service_id
        self.created_by = created_by
        self.gmt_created = gmt_created
        self.quota_id = quota_id
        self.status = status
        self.supported_client_quota_ids = supported_client_quota_ids
        self.tenant_id = tenant_id
        self.user_id = user_id
        self.user_vpc = user_vpc

    def validate(self):
        if self.cache_infos:
            for v1 in self.cache_infos:
                 if v1:
                    v1.validate()
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CacheInfos'] = []
        if self.cache_infos is not None:
            for k1 in self.cache_infos:
                result['CacheInfos'].append(k1.to_map() if k1 else None)

        if self.cache_service_id is not None:
            result['CacheServiceId'] = self.cache_service_id

        if self.created_by is not None:
            result['CreatedBy'] = self.created_by

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.quota_id is not None:
            result['QuotaId'] = self.quota_id

        if self.status is not None:
            result['Status'] = self.status

        if self.supported_client_quota_ids is not None:
            result['SupportedClientQuotaIds'] = self.supported_client_quota_ids

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cache_infos = []
        if m.get('CacheInfos') is not None:
            for k1 in m.get('CacheInfos'):
                temp_model = main_models.CacheInfo()
                self.cache_infos.append(temp_model.from_map(k1))

        if m.get('CacheServiceId') is not None:
            self.cache_service_id = m.get('CacheServiceId')

        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('QuotaId') is not None:
            self.quota_id = m.get('QuotaId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SupportedClientQuotaIds') is not None:
            self.supported_client_quota_ids = m.get('SupportedClientQuotaIds')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserVpc') is not None:
            temp_model = main_models.UserVpc()
            self.user_vpc = temp_model.from_map(m.get('UserVpc'))

        return self

