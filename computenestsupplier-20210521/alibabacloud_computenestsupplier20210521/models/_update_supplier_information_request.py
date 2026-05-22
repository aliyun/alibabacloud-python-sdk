# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenestsupplier20210521 import models as main_models
from darabonba.model import DaraModel

class UpdateSupplierInformationRequest(DaraModel):
    def __init__(
        self,
        delivery_settings: main_models.UpdateSupplierInformationRequestDeliverySettings = None,
        operation_ip: str = None,
        operation_mfa_present: bool = None,
        region_id: str = None,
        supplier_desc: str = None,
        supplier_logo: str = None,
        supplier_url: str = None,
        support_contacts: List[main_models.UpdateSupplierInformationRequestSupportContacts] = None,
    ):
        # The delivery settings.
        self.delivery_settings = delivery_settings
        # The Ip of operation.
        self.operation_ip = operation_ip
        # The MFA of operation.
        self.operation_mfa_present = operation_mfa_present
        # Region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The description of service provider.
        self.supplier_desc = supplier_desc
        # The Logo of service provider.
        self.supplier_logo = supplier_logo
        # The URL of the service provider.
        self.supplier_url = supplier_url
        # Contact information of the service provider
        self.support_contacts = support_contacts

    def validate(self):
        if self.delivery_settings:
            self.delivery_settings.validate()
        if self.support_contacts:
            for v1 in self.support_contacts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delivery_settings is not None:
            result['DeliverySettings'] = self.delivery_settings.to_map()

        if self.operation_ip is not None:
            result['OperationIp'] = self.operation_ip

        if self.operation_mfa_present is not None:
            result['OperationMfaPresent'] = self.operation_mfa_present

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.supplier_desc is not None:
            result['SupplierDesc'] = self.supplier_desc

        if self.supplier_logo is not None:
            result['SupplierLogo'] = self.supplier_logo

        if self.supplier_url is not None:
            result['SupplierUrl'] = self.supplier_url

        result['SupportContacts'] = []
        if self.support_contacts is not None:
            for k1 in self.support_contacts:
                result['SupportContacts'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliverySettings') is not None:
            temp_model = main_models.UpdateSupplierInformationRequestDeliverySettings()
            self.delivery_settings = temp_model.from_map(m.get('DeliverySettings'))

        if m.get('OperationIp') is not None:
            self.operation_ip = m.get('OperationIp')

        if m.get('OperationMfaPresent') is not None:
            self.operation_mfa_present = m.get('OperationMfaPresent')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SupplierDesc') is not None:
            self.supplier_desc = m.get('SupplierDesc')

        if m.get('SupplierLogo') is not None:
            self.supplier_logo = m.get('SupplierLogo')

        if m.get('SupplierUrl') is not None:
            self.supplier_url = m.get('SupplierUrl')

        self.support_contacts = []
        if m.get('SupportContacts') is not None:
            for k1 in m.get('SupportContacts'):
                temp_model = main_models.UpdateSupplierInformationRequestSupportContacts()
                self.support_contacts.append(temp_model.from_map(k1))

        return self

class UpdateSupplierInformationRequestSupportContacts(DaraModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
    ):
        # The type of  contact information
        self.type = type
        # The value of contact information
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class UpdateSupplierInformationRequestDeliverySettings(DaraModel):
    def __init__(
        self,
        oss_bucket_name: str = None,
        oss_enabled: bool = None,
        oss_expiration_days: int = None,
        oss_path: str = None,
    ):
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
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')

        if m.get('OssEnabled') is not None:
            self.oss_enabled = m.get('OssEnabled')

        if m.get('OssExpirationDays') is not None:
            self.oss_expiration_days = m.get('OssExpirationDays')

        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')

        return self

