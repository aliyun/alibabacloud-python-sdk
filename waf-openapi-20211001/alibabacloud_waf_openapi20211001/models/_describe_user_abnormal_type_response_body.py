# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeUserAbnormalTypeResponseBody(DaraModel):
    def __init__(
        self,
        abnormal: List[main_models.DescribeUserAbnormalTypeResponseBodyAbnormal] = None,
        request_id: str = None,
    ):
        # The risk types detected by API security and the number of risks for each type.
        self.abnormal = abnormal
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.abnormal:
            for v1 in self.abnormal:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Abnormal'] = []
        if self.abnormal is not None:
            for k1 in self.abnormal:
                result['Abnormal'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.abnormal = []
        if m.get('Abnormal') is not None:
            for k1 in m.get('Abnormal'):
                temp_model = main_models.DescribeUserAbnormalTypeResponseBodyAbnormal()
                self.abnormal.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeUserAbnormalTypeResponseBodyAbnormal(DaraModel):
    def __init__(
        self,
        abnormal_code: str = None,
        abnormal_count: int = None,
        abnormal_parent_type: str = None,
        abnormal_type: str = None,
    ):
        # The code that identifies the specific risk, such as `Risk_InternalWeakPasswd`.
        self.abnormal_code = abnormal_code
        # The total number of risks detected for this risk type.
        self.abnormal_count = abnormal_count
        # The parent category of the risk, such as `RiskType_Account`.
        self.abnormal_parent_type = abnormal_parent_type
        # The type of the risk detected by API security.
        # 
        # > Call the [DescribeApisecRules](https://help.aliyun.com/document_detail/2859155.html) operation to query the supported risk types.
        self.abnormal_type = abnormal_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abnormal_code is not None:
            result['AbnormalCode'] = self.abnormal_code

        if self.abnormal_count is not None:
            result['AbnormalCount'] = self.abnormal_count

        if self.abnormal_parent_type is not None:
            result['AbnormalParentType'] = self.abnormal_parent_type

        if self.abnormal_type is not None:
            result['AbnormalType'] = self.abnormal_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbnormalCode') is not None:
            self.abnormal_code = m.get('AbnormalCode')

        if m.get('AbnormalCount') is not None:
            self.abnormal_count = m.get('AbnormalCount')

        if m.get('AbnormalParentType') is not None:
            self.abnormal_parent_type = m.get('AbnormalParentType')

        if m.get('AbnormalType') is not None:
            self.abnormal_type = m.get('AbnormalType')

        return self

