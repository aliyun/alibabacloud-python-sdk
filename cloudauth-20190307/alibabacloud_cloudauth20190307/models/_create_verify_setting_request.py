# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateVerifySettingRequest(DaraModel):
    def __init__(
        self,
        biz_name: str = None,
        biz_type: str = None,
        guide_step: bool = None,
        privacy_step: bool = None,
        result_step: bool = None,
        solution: str = None,
    ):
        # Verification scenario name, supporting Chinese, English, numbers, and hyphens (-), with a maximum of 20 characters.
        # 
        # This parameter is required.
        self.biz_name = biz_name
        # Verification scenario identifier, supporting English letters, numbers, and hyphens (-), with a maximum of 20 characters.
        # 
        # This parameter is required.
        self.biz_type = biz_type
        # Whether to use the system\\"s default guide page.
        self.guide_step = guide_step
        # Whether to use the system\\"s default authorization page.
        self.privacy_step = privacy_step
        # Whether to use the system\\"s default result page.
        self.result_step = result_step
        # The name of the authentication solution to use, such as **RPBasic**, **RPBioOnly**, etc. For all supported authentication solutions, see [Authentication Solutions](https://help.aliyun.com/document_detail/127521.html).
        # 
        # This parameter is required.
        self.solution = solution

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_name is not None:
            result['BizName'] = self.biz_name

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.guide_step is not None:
            result['GuideStep'] = self.guide_step

        if self.privacy_step is not None:
            result['PrivacyStep'] = self.privacy_step

        if self.result_step is not None:
            result['ResultStep'] = self.result_step

        if self.solution is not None:
            result['Solution'] = self.solution

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('GuideStep') is not None:
            self.guide_step = m.get('GuideStep')

        if m.get('PrivacyStep') is not None:
            self.privacy_step = m.get('PrivacyStep')

        if m.get('ResultStep') is not None:
            self.result_step = m.get('ResultStep')

        if m.get('Solution') is not None:
            self.solution = m.get('Solution')

        return self

