# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetInstanceLicenseResponseBody(DaraModel):
    def __init__(
        self,
        license: main_models.GetInstanceLicenseResponseBodyLicense = None,
        request_id: str = None,
    ):
        # Returned result.
        self.license = license
        # Request ID
        self.request_id = request_id

    def validate(self):
        if self.license:
            self.license.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.license is not None:
            result['License'] = self.license.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('License') is not None:
            temp_model = main_models.GetInstanceLicenseResponseBodyLicense()
            self.license = temp_model.from_map(m.get('License'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetInstanceLicenseResponseBodyLicense(DaraModel):
    def __init__(
        self,
        edition: str = None,
        end_time: int = None,
        license_charge_type: str = None,
        license_config_json: str = None,
        license_create_time: int = None,
        license_id: str = None,
        license_status: str = None,
        purchase_channel: str = None,
        purchase_instance_id: str = None,
        start_time: int = None,
        user_quota: int = None,
    ):
        # Edition of the License
        self.edition = edition
        # End date of the validity period of the License, timestamp
        self.end_time = end_time
        # Payment type of the License
        self.license_charge_type = license_charge_type
        # Detailed configuration JSON string of the License
        self.license_config_json = license_config_json
        # Creation time of the License, timestamp
        self.license_create_time = license_create_time
        # Unique identifier of the License
        self.license_id = license_id
        # Status of the License
        self.license_status = license_status
        # Purchase channel of the License
        self.purchase_channel = purchase_channel
        # Unique external product identifier corresponding to the License
        self.purchase_instance_id = purchase_instance_id
        # Start date of the validity period of the License, timestamp
        self.start_time = start_time
        # User quota of the License
        self.user_quota = user_quota

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.edition is not None:
            result['Edition'] = self.edition

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.license_charge_type is not None:
            result['LicenseChargeType'] = self.license_charge_type

        if self.license_config_json is not None:
            result['LicenseConfigJson'] = self.license_config_json

        if self.license_create_time is not None:
            result['LicenseCreateTime'] = self.license_create_time

        if self.license_id is not None:
            result['LicenseId'] = self.license_id

        if self.license_status is not None:
            result['LicenseStatus'] = self.license_status

        if self.purchase_channel is not None:
            result['PurchaseChannel'] = self.purchase_channel

        if self.purchase_instance_id is not None:
            result['PurchaseInstanceId'] = self.purchase_instance_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.user_quota is not None:
            result['UserQuota'] = self.user_quota

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('LicenseChargeType') is not None:
            self.license_charge_type = m.get('LicenseChargeType')

        if m.get('LicenseConfigJson') is not None:
            self.license_config_json = m.get('LicenseConfigJson')

        if m.get('LicenseCreateTime') is not None:
            self.license_create_time = m.get('LicenseCreateTime')

        if m.get('LicenseId') is not None:
            self.license_id = m.get('LicenseId')

        if m.get('LicenseStatus') is not None:
            self.license_status = m.get('LicenseStatus')

        if m.get('PurchaseChannel') is not None:
            self.purchase_channel = m.get('PurchaseChannel')

        if m.get('PurchaseInstanceId') is not None:
            self.purchase_instance_id = m.get('PurchaseInstanceId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('UserQuota') is not None:
            self.user_quota = m.get('UserQuota')

        return self

