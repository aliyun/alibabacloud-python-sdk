# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetServiceSettingsRequest(DaraModel):
    def __init__(
        self,
        delivery_oss_bucket_name: str = None,
        delivery_oss_enabled: bool = None,
        delivery_oss_key_prefix: str = None,
        delivery_sls_enabled: bool = None,
        delivery_sls_project_name: str = None,
        rdc_enterprise_id: str = None,
        region_id: str = None,
    ):
        # The name of OSS bucket to deliver.
        self.delivery_oss_bucket_name = delivery_oss_bucket_name
        # Whether to enable OSS delivery.
        self.delivery_oss_enabled = delivery_oss_enabled
        # The key prefix of OSS to deliver.
        self.delivery_oss_key_prefix = delivery_oss_key_prefix
        # Whether to enable SLS delivery.
        self.delivery_sls_enabled = delivery_sls_enabled
        # The name of SLS project to deliver.
        self.delivery_sls_project_name = delivery_sls_project_name
        # The id of RDC Enterprise.
        self.rdc_enterprise_id = rdc_enterprise_id
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delivery_oss_bucket_name is not None:
            result['DeliveryOssBucketName'] = self.delivery_oss_bucket_name

        if self.delivery_oss_enabled is not None:
            result['DeliveryOssEnabled'] = self.delivery_oss_enabled

        if self.delivery_oss_key_prefix is not None:
            result['DeliveryOssKeyPrefix'] = self.delivery_oss_key_prefix

        if self.delivery_sls_enabled is not None:
            result['DeliverySlsEnabled'] = self.delivery_sls_enabled

        if self.delivery_sls_project_name is not None:
            result['DeliverySlsProjectName'] = self.delivery_sls_project_name

        if self.rdc_enterprise_id is not None:
            result['RdcEnterpriseId'] = self.rdc_enterprise_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryOssBucketName') is not None:
            self.delivery_oss_bucket_name = m.get('DeliveryOssBucketName')

        if m.get('DeliveryOssEnabled') is not None:
            self.delivery_oss_enabled = m.get('DeliveryOssEnabled')

        if m.get('DeliveryOssKeyPrefix') is not None:
            self.delivery_oss_key_prefix = m.get('DeliveryOssKeyPrefix')

        if m.get('DeliverySlsEnabled') is not None:
            self.delivery_sls_enabled = m.get('DeliverySlsEnabled')

        if m.get('DeliverySlsProjectName') is not None:
            self.delivery_sls_project_name = m.get('DeliverySlsProjectName')

        if m.get('RdcEnterpriseId') is not None:
            self.rdc_enterprise_id = m.get('RdcEnterpriseId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

