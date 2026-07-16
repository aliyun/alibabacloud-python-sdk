# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class QueryDigitalSignByNameResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Details of the access denial. This parameter is returned only if Resource Access Management (RAM) authentication fails.
        self.access_denied_detail = access_denied_detail
        # The status code of the request. A value of `OK` indicates that the request was successful. Other values indicate error codes.
        self.code = code
        # - `gmtModified`: The time when the signature was last modified.
        # 
        # - `creator`: The ID of the user who created the signature.
        # 
        # - `signName`: The name of the digital SMS signature.
        # 
        # - `qualificationId`: The ID of the qualification. You can create qualifications in the console or by calling an API operation.
        # 
        # - `signIndustry`: The industry type. Valid values: `0` (General) and `1` (E-commerce).
        # 
        # - `signVersion`: The version of the signature. This value is updated for each new version. The current version is 1.
        # 
        # - `telecomRegisterStatus`: The filing status with China Telecom. Valid values: `0` (Filing Failed), `3` (Filing Successful), `-1` (Filing in Progress), and `-2` (Not Filed).
        # 
        # - `signCode`: The code of the digital SMS signature.
        # 
        # - `gmtCreate`: The time when the signature was created.
        # 
        # - `signId`: The ID of the signature. This is a unique identifier.
        # 
        # - `mobileRegisterStatus`: The filing status with China Mobile.
        # 
        # - `SignSource`: The source of the signature. Valid values:
        # 
        # - `mobileAvailableStatus`: The availability status with China Mobile. Valid values: `0` (Unavailable) and `1` (Available). We recommend that you select an available signature when you create a template or send a digital SMS message.
        # 
        # - `unicomRegisterStatus`: The filing status with China Unicom. Valid values: `0` (Filing Failed), `3` (Filing Successful), `-1` (Filing in Progress), and `-2` (Not Filed).
        # 
        # - `unicomAvailableStatus`: The availability status with China Unicom. Valid values: `0` (Unavailable) and `1` (Available). We recommend that you select an available signature when you create a template or send a digital SMS message.
        # 
        # - `telecomAvailableStatus`: The availability status with China Telecom. Valid values: `0` (Unavailable) and `1` (Available). We recommend that you select an available signature when you create a template or send a digital SMS message.
        self.data = data
        # The description of the status code.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

