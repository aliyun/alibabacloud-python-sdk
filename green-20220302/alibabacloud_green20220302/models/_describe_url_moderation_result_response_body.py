# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_green20220302 import models as main_models
from darabonba.model import DaraModel

class DescribeUrlModerationResultResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.DescribeUrlModerationResultResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
    ):
        # The returned HTTP status code. The status code 200 indicates that the request was successful.
        self.code = code
        # The data returned.
        self.data = data
        # The message that is returned in response to the request.
        self.msg = msg
        # The request ID.
        self.request_id = request_id

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

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeUrlModerationResultResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeUrlModerationResultResponseBodyData(DaraModel):
    def __init__(
        self,
        data_id: str = None,
        extra_info: main_models.DescribeUrlModerationResultResponseBodyDataExtraInfo = None,
        req_id: str = None,
        result: List[main_models.DescribeUrlModerationResultResponseBodyDataResult] = None,
    ):
        # The value of dataId that is specified in the API request. If this parameter is not specified in the API request, this field is not available in the response.
        self.data_id = data_id
        # The supplementary information.
        self.extra_info = extra_info
        # The ReqId field returned by an asynchronous URL moderation operation.
        self.req_id = req_id
        # The returned results.
        self.result = result

    def validate(self):
        if self.extra_info:
            self.extra_info.validate()
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_id is not None:
            result['DataId'] = self.data_id

        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info.to_map()

        if self.req_id is not None:
            result['ReqId'] = self.req_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')

        if m.get('ExtraInfo') is not None:
            temp_model = main_models.DescribeUrlModerationResultResponseBodyDataExtraInfo()
            self.extra_info = temp_model.from_map(m.get('ExtraInfo'))

        if m.get('ReqId') is not None:
            self.req_id = m.get('ReqId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.DescribeUrlModerationResultResponseBodyDataResult()
                self.result.append(temp_model.from_map(k1))

        return self

class DescribeUrlModerationResultResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        confidence: float = None,
        label: str = None,
    ):
        # The score of the confidence level. Valid values: 0 to 100. The value is accurate to two decimal places.
        self.confidence = confidence
        # The labels returned after the asynchronous URL moderation.
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.confidence is not None:
            result['Confidence'] = self.confidence

        if self.label is not None:
            result['Label'] = self.label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        return self

class DescribeUrlModerationResultResponseBodyDataExtraInfo(DaraModel):
    def __init__(
        self,
        icp_no: str = None,
        icp_type: str = None,
        site_type: str = None,
    ):
        # The ICP number.
        self.icp_no = icp_no
        # The type of the ICP filing.
        self.icp_type = icp_type
        # The type of site
        self.site_type = site_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.icp_no is not None:
            result['IcpNo'] = self.icp_no

        if self.icp_type is not None:
            result['IcpType'] = self.icp_type

        if self.site_type is not None:
            result['SiteType'] = self.site_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IcpNo') is not None:
            self.icp_no = m.get('IcpNo')

        if m.get('IcpType') is not None:
            self.icp_type = m.get('IcpType')

        if m.get('SiteType') is not None:
            self.site_type = m.get('SiteType')

        return self

