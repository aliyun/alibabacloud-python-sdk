# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class ModifyDesktopsPolicyGroupResponseBody(DaraModel):
    def __init__(
        self,
        modify_results: List[main_models.ModifyDesktopsPolicyGroupResponseBodyModifyResults] = None,
        request_id: str = None,
    ):
        # The request results.
        self.modify_results = modify_results
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.modify_results:
            for v1 in self.modify_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ModifyResults'] = []
        if self.modify_results is not None:
            for k1 in self.modify_results:
                result['ModifyResults'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.modify_results = []
        if m.get('ModifyResults') is not None:
            for k1 in m.get('ModifyResults'):
                temp_model = main_models.ModifyDesktopsPolicyGroupResponseBodyModifyResults()
                self.modify_results.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ModifyDesktopsPolicyGroupResponseBodyModifyResults(DaraModel):
    def __init__(
        self,
        code: str = None,
        desktop_id: str = None,
        message: str = None,
    ):
        # The returned message. If the request was successful, `success` is returned. If the request failed, an error message is returned.
        self.code = code
        # The cloud computer ID.
        self.desktop_id = desktop_id
        # The error message returned if the request failed. This parameter is not returned if the value of Code is success.``
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

