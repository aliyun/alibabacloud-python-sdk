# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mpaas20201028 import models as main_models
from darabonba.model import DaraModel

class UploadMcubeMiniPackageResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
        upload_mini_package_result: main_models.UploadMcubeMiniPackageResponseBodyUploadMiniPackageResult = None,
    ):
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message
        self.upload_mini_package_result = upload_mini_package_result

    def validate(self):
        if self.upload_mini_package_result:
            self.upload_mini_package_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.result_message is not None:
            result['ResultMessage'] = self.result_message

        if self.upload_mini_package_result is not None:
            result['UploadMiniPackageResult'] = self.upload_mini_package_result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')

        if m.get('UploadMiniPackageResult') is not None:
            temp_model = main_models.UploadMcubeMiniPackageResponseBodyUploadMiniPackageResult()
            self.upload_mini_package_result = temp_model.from_map(m.get('UploadMiniPackageResult'))

        return self

class UploadMcubeMiniPackageResponseBodyUploadMiniPackageResult(DaraModel):
    def __init__(
        self,
        result_msg: str = None,
        return_package_result: main_models.UploadMcubeMiniPackageResponseBodyUploadMiniPackageResultReturnPackageResult = None,
        success: bool = None,
    ):
        self.result_msg = result_msg
        self.return_package_result = return_package_result
        self.success = success

    def validate(self):
        if self.return_package_result:
            self.return_package_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg

        if self.return_package_result is not None:
            result['ReturnPackageResult'] = self.return_package_result.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')

        if m.get('ReturnPackageResult') is not None:
            temp_model = main_models.UploadMcubeMiniPackageResponseBodyUploadMiniPackageResultReturnPackageResult()
            self.return_package_result = temp_model.from_map(m.get('ReturnPackageResult'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class UploadMcubeMiniPackageResponseBodyUploadMiniPackageResultReturnPackageResult(DaraModel):
    def __init__(
        self,
        debug_url: str = None,
        package_id: str = None,
        user_id: str = None,
    ):
        self.debug_url = debug_url
        self.package_id = package_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.debug_url is not None:
            result['DebugUrl'] = self.debug_url

        if self.package_id is not None:
            result['PackageId'] = self.package_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DebugUrl') is not None:
            self.debug_url = m.get('DebugUrl')

        if m.get('PackageId') is not None:
            self.package_id = m.get('PackageId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

