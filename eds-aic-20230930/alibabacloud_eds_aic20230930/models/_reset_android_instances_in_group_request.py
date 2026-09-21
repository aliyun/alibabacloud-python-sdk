# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ResetAndroidInstancesInGroupRequest(DaraModel):
    def __init__(
        self,
        android_instance_ids: List[str] = None,
        auto_pay: bool = None,
        ignore_param_validation: bool = None,
        promotion_id: str = None,
        sale_mode: str = None,
        setting_reset_type: int = None,
        target_data_disk_size: int = None,
    ):
        # The list of instance IDs.
        self.android_instance_ids = android_instance_ids
        # Specifies whether to enable automatic payment. Default value: false.
        self.auto_pay = auto_pay
        self.ignore_param_validation = ignore_param_validation
        # The promotion ID.
        self.promotion_id = promotion_id
        # **[Deprecated]** The sales mode. This parameter is deprecated.
        self.sale_mode = sale_mode
        # <props="china">Specifies whether to retain attribute settings during the reset. If this parameter is not specified, attribute configurations are not retained by default. This parameter takes effect only for cloud phone matrix instances. Run the wya dump config command to view the details of retained attributes.
        # <props="intl">This parameter is not supported on the international site.
        self.setting_reset_type = setting_reset_type
        # Specify this parameter when you need to reduce storage while resetting instances in a cloud phone matrix. This feature is currently available through a whitelist. This parameter applies only to instances in a cloud phone matrix.
        self.target_data_disk_size = target_data_disk_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.android_instance_ids is not None:
            result['AndroidInstanceIds'] = self.android_instance_ids

        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.ignore_param_validation is not None:
            result['IgnoreParamValidation'] = self.ignore_param_validation

        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id

        if self.sale_mode is not None:
            result['SaleMode'] = self.sale_mode

        if self.setting_reset_type is not None:
            result['SettingResetType'] = self.setting_reset_type

        if self.target_data_disk_size is not None:
            result['TargetDataDiskSize'] = self.target_data_disk_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceIds') is not None:
            self.android_instance_ids = m.get('AndroidInstanceIds')

        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('IgnoreParamValidation') is not None:
            self.ignore_param_validation = m.get('IgnoreParamValidation')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        if m.get('SaleMode') is not None:
            self.sale_mode = m.get('SaleMode')

        if m.get('SettingResetType') is not None:
            self.setting_reset_type = m.get('SettingResetType')

        if m.get('TargetDataDiskSize') is not None:
            self.target_data_disk_size = m.get('TargetDataDiskSize')

        return self

