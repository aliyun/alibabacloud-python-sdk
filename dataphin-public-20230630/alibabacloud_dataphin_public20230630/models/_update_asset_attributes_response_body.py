# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class UpdateAssetAttributesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.UpdateAssetAttributesResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The backend response code.
        self.code = code
        # The result of updating asset property values.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The backend exception details.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.UpdateAssetAttributesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class UpdateAssetAttributesResponseBodyData(DaraModel):
    def __init__(
        self,
        fail_count: int = None,
        result_list: List[main_models.UpdateAssetAttributesResponseBodyDataResultList] = None,
        success_count: int = None,
        total_count: int = None,
    ):
        # The number of assets that failed to be updated.
        self.fail_count = fail_count
        # The update results for each asset.
        self.result_list = result_list
        # The number of assets that were updated successfully.
        self.success_count = success_count
        # The total number of assets.
        self.total_count = total_count

    def validate(self):
        if self.result_list:
            for v1 in self.result_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fail_count is not None:
            result['FailCount'] = self.fail_count

        result['ResultList'] = []
        if self.result_list is not None:
            for k1 in self.result_list:
                result['ResultList'].append(k1.to_map() if k1 else None)

        if self.success_count is not None:
            result['SuccessCount'] = self.success_count

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')

        self.result_list = []
        if m.get('ResultList') is not None:
            for k1 in m.get('ResultList'):
                temp_model = main_models.UpdateAssetAttributesResponseBodyDataResultList()
                self.result_list.append(temp_model.from_map(k1))

        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class UpdateAssetAttributesResponseBodyDataResultList(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        guid: str = None,
        success: bool = None,
    ):
        # The error code returned when the update fails. This value is empty when the update succeeds.
        self.error_code = error_code
        # The error message returned when the update fails. This value is empty when the update succeeds.
        self.error_message = error_message
        # The globally unique identifier (GUID) of the asset.
        self.guid = guid
        # Indicates whether the asset was updated successfully.
        self.success = success

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

        if self.guid is not None:
            result['Guid'] = self.guid

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Guid') is not None:
            self.guid = m.get('Guid')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

