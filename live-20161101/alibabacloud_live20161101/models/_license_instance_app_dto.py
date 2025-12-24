# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class LicenseInstanceAppDTO(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        begin_on: str = None,
        contract_no: str = None,
        creation_time: str = None,
        expired_on: str = None,
        instance_id: str = None,
        item_id: str = None,
        license_configs: List[main_models.LicenseInstanceAppDTOLicenseConfigs] = None,
        modification_time: str = None,
        status: str = None,
        user_id: int = None,
    ):
        self.app_id = app_id
        self.begin_on = begin_on
        self.contract_no = contract_no
        self.creation_time = creation_time
        self.expired_on = expired_on
        self.instance_id = instance_id
        self.item_id = item_id
        self.license_configs = license_configs
        self.modification_time = modification_time
        self.status = status
        self.user_id = user_id

    def validate(self):
        if self.license_configs:
            for v1 in self.license_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.begin_on is not None:
            result['BeginOn'] = self.begin_on

        if self.contract_no is not None:
            result['ContractNo'] = self.contract_no

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.expired_on is not None:
            result['ExpiredOn'] = self.expired_on

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.item_id is not None:
            result['ItemId'] = self.item_id

        result['LicenseConfigs'] = []
        if self.license_configs is not None:
            for k1 in self.license_configs:
                result['LicenseConfigs'].append(k1.to_map() if k1 else None)

        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time

        if self.status is not None:
            result['Status'] = self.status

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('BeginOn') is not None:
            self.begin_on = m.get('BeginOn')

        if m.get('ContractNo') is not None:
            self.contract_no = m.get('ContractNo')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('ExpiredOn') is not None:
            self.expired_on = m.get('ExpiredOn')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')

        self.license_configs = []
        if m.get('LicenseConfigs') is not None:
            for k1 in m.get('LicenseConfigs'):
                temp_model = main_models.LicenseInstanceAppDTOLicenseConfigs()
                self.license_configs.append(temp_model.from_map(k1))

        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class LicenseInstanceAppDTOLicenseConfigs(DaraModel):
    def __init__(
        self,
        business_type: str = None,
        feature_ids: str = None,
        is_trial: bool = None,
        sdk_id: int = None,
        sdk_name: str = None,
        subscription: str = None,
        subscription_imp: str = None,
        subscription_pkg: str = None,
    ):
        self.business_type = business_type
        self.feature_ids = feature_ids
        self.is_trial = is_trial
        self.sdk_id = sdk_id
        self.sdk_name = sdk_name
        self.subscription = subscription
        self.subscription_imp = subscription_imp
        self.subscription_pkg = subscription_pkg

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_type is not None:
            result['BusinessType'] = self.business_type

        if self.feature_ids is not None:
            result['FeatureIds'] = self.feature_ids

        if self.is_trial is not None:
            result['IsTrial'] = self.is_trial

        if self.sdk_id is not None:
            result['SdkId'] = self.sdk_id

        if self.sdk_name is not None:
            result['SdkName'] = self.sdk_name

        if self.subscription is not None:
            result['Subscription'] = self.subscription

        if self.subscription_imp is not None:
            result['SubscriptionImp'] = self.subscription_imp

        if self.subscription_pkg is not None:
            result['SubscriptionPkg'] = self.subscription_pkg

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

        if m.get('FeatureIds') is not None:
            self.feature_ids = m.get('FeatureIds')

        if m.get('IsTrial') is not None:
            self.is_trial = m.get('IsTrial')

        if m.get('SdkId') is not None:
            self.sdk_id = m.get('SdkId')

        if m.get('SdkName') is not None:
            self.sdk_name = m.get('SdkName')

        if m.get('Subscription') is not None:
            self.subscription = m.get('Subscription')

        if m.get('SubscriptionImp') is not None:
            self.subscription_imp = m.get('SubscriptionImp')

        if m.get('SubscriptionPkg') is not None:
            self.subscription_pkg = m.get('SubscriptionPkg')

        return self

