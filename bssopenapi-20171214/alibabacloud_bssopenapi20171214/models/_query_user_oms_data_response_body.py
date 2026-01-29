# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class QueryUserOmsDataResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryUserOmsDataResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code returned.
        self.code = code
        # The data returned.
        self.data = data
        # The message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
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
            temp_model = main_models.QueryUserOmsDataResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryUserOmsDataResponseBodyData(DaraModel):
    def __init__(
        self,
        host_id: str = None,
        marker: str = None,
        oms_data: List[Dict[str, Any]] = None,
    ):
        # The ID of the host.
        self.host_id = host_id
        # Indicates that the returned usage data starts from the next page. If no value is returned for this parameter or this parameter is not returned, no data can be queried.
        self.marker = marker
        self.oms_data = oms_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host_id is not None:
            result['HostId'] = self.host_id

        if self.marker is not None:
            result['Marker'] = self.marker

        if self.oms_data is not None:
            result['OmsData'] = self.oms_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')

        if m.get('Marker') is not None:
            self.marker = m.get('Marker')

        if m.get('OmsData') is not None:
            self.oms_data = m.get('OmsData')

        return self

