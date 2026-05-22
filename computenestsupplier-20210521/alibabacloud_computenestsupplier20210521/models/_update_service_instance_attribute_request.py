# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_computenestsupplier20210521 import models as main_models
from darabonba.model import DaraModel

class UpdateServiceInstanceAttributeRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        license_data: main_models.UpdateServiceInstanceAttributeRequestLicenseData = None,
        reason: str = None,
        region_id: str = None,
        service_instance_id: str = None,
    ):
        # The time when the service instance expires.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.end_time = end_time
        # The License Data
        self.license_data = license_data
        # Application reason, currently used for trial application extension.
        self.reason = reason
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The service instance ID.
        # 
        # This parameter is required.
        self.service_instance_id = service_instance_id

    def validate(self):
        if self.license_data:
            self.license_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.license_data is not None:
            result['LicenseData'] = self.license_data.to_map()

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('LicenseData') is not None:
            temp_model = main_models.UpdateServiceInstanceAttributeRequestLicenseData()
            self.license_data = temp_model.from_map(m.get('LicenseData'))

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')

        return self

class UpdateServiceInstanceAttributeRequestLicenseData(DaraModel):
    def __init__(
        self,
        custom_data: str = None,
        response_info: main_models.UpdateServiceInstanceAttributeRequestLicenseDataResponseInfo = None,
    ):
        # The Custom Data
        self.custom_data = custom_data
        # Mock response info.
        self.response_info = response_info

    def validate(self):
        if self.response_info:
            self.response_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_data is not None:
            result['CustomData'] = self.custom_data

        if self.response_info is not None:
            result['ResponseInfo'] = self.response_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomData') is not None:
            self.custom_data = m.get('CustomData')

        if m.get('ResponseInfo') is not None:
            temp_model = main_models.UpdateServiceInstanceAttributeRequestLicenseDataResponseInfo()
            self.response_info = temp_model.from_map(m.get('ResponseInfo'))

        return self

class UpdateServiceInstanceAttributeRequestLicenseDataResponseInfo(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        update_response: bool = None,
    ):
        # Mock error code.
        self.error_code = error_code
        # Mock error message.
        self.error_message = error_message
        # if you want mock response, please open this option.
        self.update_response = update_response

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.update_response is not None:
            result['UpdateResponse'] = self.update_response

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('UpdateResponse') is not None:
            self.update_response = m.get('UpdateResponse')

        return self

