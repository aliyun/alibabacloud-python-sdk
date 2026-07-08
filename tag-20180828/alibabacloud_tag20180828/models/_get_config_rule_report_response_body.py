# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_tag20180828 import models as main_models
from darabonba.model import DaraModel

class GetConfigRuleReportResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetConfigRuleReportResponseBodyData = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The basic information of the resource non-compliance report that is last generated.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request is successful.
        # *   false: The request fails.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetConfigRuleReportResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetConfigRuleReportResponseBodyData(DaraModel):
    def __init__(
        self,
        created_time: int = None,
        report_id: str = None,
        target_id: str = None,
        target_type: str = None,
    ):
        # The time when the report was generated. This value is a UNIX timestamp.
        self.created_time = created_time
        # The ID of the report.
        self.report_id = report_id
        # The ID of the object.
        # 
        # >  This parameter is returned if you set the `TargetType` and `TargetId` parameters in the current request to the same values as the parameters that are configured when you call the [GenerateConfigRuleReport](https://help.aliyun.com/document_detail/433313.html) operation to generate the report.
        self.target_id = target_id
        # The type of the object. Valid values:
        # 
        # *   USER: the current logon account. This value is available if you use the Tag Policy feature in single-account mode.
        # *   ROOT: the Root folder in the resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        # *   FOLDER: a folder other than the Root folder in the resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        # *   ACCOUNT: a member in the resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        # 
        # >  This parameter is returned if you set the `TargetType` and `TargetId` parameters in the current request to the same values as the parameters that are configured when you call the [GenerateConfigRuleReport](https://help.aliyun.com/document_detail/433313.html) operation to generate the report.
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.report_id is not None:
            result['ReportId'] = self.report_id

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

