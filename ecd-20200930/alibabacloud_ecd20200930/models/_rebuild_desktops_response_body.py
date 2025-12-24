# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class RebuildDesktopsResponseBody(DaraModel):
    def __init__(
        self,
        rebuild_results: List[main_models.RebuildDesktopsResponseBodyRebuildResults] = None,
        request_id: str = None,
    ):
        # The recreation results.
        self.rebuild_results = rebuild_results
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.rebuild_results:
            for v1 in self.rebuild_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RebuildResults'] = []
        if self.rebuild_results is not None:
            for k1 in self.rebuild_results:
                result['RebuildResults'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rebuild_results = []
        if m.get('RebuildResults') is not None:
            for k1 in m.get('RebuildResults'):
                temp_model = main_models.RebuildDesktopsResponseBodyRebuildResults()
                self.rebuild_results.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class RebuildDesktopsResponseBodyRebuildResults(DaraModel):
    def __init__(
        self,
        code: str = None,
        desktop_id: str = None,
        message: str = None,
    ):
        # The recreation result code. If the request was successful, `success` is returned. If the request failed, an error message is returned.
        self.code = code
        # The IDs of the cloud computers.
        self.desktop_id = desktop_id
        # The error message. This parameter is invalid if the value of `Code` is `success`.
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

