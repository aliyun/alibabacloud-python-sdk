# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ResetAndroidInstancesInGroupRequest(DaraModel):
    def __init__(
        self,
        android_instance_ids: List[str] = None,
        ignore_param_validation: bool = None,
        sale_mode: str = None,
        setting_reset_type: int = None,
    ):
        # A list of instance IDs.
        self.android_instance_ids = android_instance_ids
        self.ignore_param_validation = ignore_param_validation
        # The sale mode. This parameter is deprecated.
        self.sale_mode = sale_mode
        # <props="china">Specifies whether to retain the property settings when you reset the instances. By default, the property settings are not retained. This parameter applies only to cloud phone matrix instances. Run the wya dump config command to view the details of the retained properties.<props="intl">This parameter is not supported on the international site (alibabacloud.com).
        self.setting_reset_type = setting_reset_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.android_instance_ids is not None:
            result['AndroidInstanceIds'] = self.android_instance_ids

        if self.ignore_param_validation is not None:
            result['IgnoreParamValidation'] = self.ignore_param_validation

        if self.sale_mode is not None:
            result['SaleMode'] = self.sale_mode

        if self.setting_reset_type is not None:
            result['SettingResetType'] = self.setting_reset_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceIds') is not None:
            self.android_instance_ids = m.get('AndroidInstanceIds')

        if m.get('IgnoreParamValidation') is not None:
            self.ignore_param_validation = m.get('IgnoreParamValidation')

        if m.get('SaleMode') is not None:
            self.sale_mode = m.get('SaleMode')

        if m.get('SettingResetType') is not None:
            self.setting_reset_type = m.get('SettingResetType')

        return self

