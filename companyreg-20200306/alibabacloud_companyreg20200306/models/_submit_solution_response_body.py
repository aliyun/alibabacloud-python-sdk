# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitSolutionResponseBody(DaraModel):
    def __init__(
        self,
        confirm_url: str = None,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        solution_biz_id: str = None,
        success: bool = None,
    ):
        self.confirm_url = confirm_url
        self.error_code = error_code
        self.error_msg = error_msg
        self.request_id = request_id
        self.solution_biz_id = solution_biz_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.confirm_url is not None:
            result['ConfirmUrl'] = self.confirm_url

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.solution_biz_id is not None:
            result['SolutionBizId'] = self.solution_biz_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfirmUrl') is not None:
            self.confirm_url = m.get('ConfirmUrl')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SolutionBizId') is not None:
            self.solution_biz_id = m.get('SolutionBizId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

