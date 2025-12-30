# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class GetAiRtcLicenseInfoListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        license_info_list: List[main_models.AiRtcLicenseInfoDTO] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The error code returned.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # An array of AiRtcLicenseInfoDTO objects, each representing a license batch.
        self.license_info_list = license_info_list
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful.
        self.success = success
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.license_info_list:
            for v1 in self.license_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        result['LicenseInfoList'] = []
        if self.license_info_list is not None:
            for k1 in self.license_info_list:
                result['LicenseInfoList'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        self.license_info_list = []
        if m.get('LicenseInfoList') is not None:
            for k1 in m.get('LicenseInfoList'):
                temp_model = main_models.AiRtcLicenseInfoDTO()
                self.license_info_list.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

