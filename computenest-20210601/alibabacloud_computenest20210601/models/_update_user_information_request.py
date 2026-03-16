# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_computenest20210601 import models as main_models
from darabonba.model import DaraModel

class UpdateUserInformationRequest(DaraModel):
    def __init__(
        self,
        delivery_settings: main_models.UpdateUserInformationRequestDeliverySettings = None,
        region_id: str = None,
    ):
        # The modified delivery settings.
        self.delivery_settings = delivery_settings
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        if self.delivery_settings:
            self.delivery_settings.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delivery_settings is not None:
            result['DeliverySettings'] = self.delivery_settings.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliverySettings') is not None:
            temp_model = main_models.UpdateUserInformationRequestDeliverySettings()
            self.delivery_settings = temp_model.from_map(m.get('DeliverySettings'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class UpdateUserInformationRequestDeliverySettings(DaraModel):
    def __init__(
        self,
        actiontrail_delivery_to_oss_enabled: bool = None,
        oss_bucket_name: str = None,
        oss_enabled: bool = None,
        oss_expiration_days: int = None,
        oss_path: str = None,
    ):
        # Specifies whether to enable screencast delivery to OSS. Valid values:
        # 
        # *   true
        # *   false
        self.actiontrail_delivery_to_oss_enabled = actiontrail_delivery_to_oss_enabled
        # The name of the OSS bucket.
        self.oss_bucket_name = oss_bucket_name
        # Specifies whether to enable screencast delivery to Object Storage Service (OSS). Valid values:
        # 
        # *   true
        # *   false
        self.oss_enabled = oss_enabled
        # The number of days for which the screencasts are saved.
        self.oss_expiration_days = oss_expiration_days
        # The OSS path.
        self.oss_path = oss_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actiontrail_delivery_to_oss_enabled is not None:
            result['ActiontrailDeliveryToOssEnabled'] = self.actiontrail_delivery_to_oss_enabled

        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name

        if self.oss_enabled is not None:
            result['OssEnabled'] = self.oss_enabled

        if self.oss_expiration_days is not None:
            result['OssExpirationDays'] = self.oss_expiration_days

        if self.oss_path is not None:
            result['OssPath'] = self.oss_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiontrailDeliveryToOssEnabled') is not None:
            self.actiontrail_delivery_to_oss_enabled = m.get('ActiontrailDeliveryToOssEnabled')

        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')

        if m.get('OssEnabled') is not None:
            self.oss_enabled = m.get('OssEnabled')

        if m.get('OssExpirationDays') is not None:
            self.oss_expiration_days = m.get('OssExpirationDays')

        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')

        return self

