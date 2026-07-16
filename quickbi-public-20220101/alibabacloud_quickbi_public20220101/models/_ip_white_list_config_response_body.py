# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class IpWhiteListConfigResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.IpWhiteListConfigResponseBodyResult = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The IP address whitelist.
        self.result = result
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.IpWhiteListConfigResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class IpWhiteListConfigResponseBodyResult(DaraModel):
    def __init__(
        self,
        ip_white_list: List[str] = None,
    ):
        # The IP address whitelist array.
        self.ip_white_list = ip_white_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_white_list is not None:
            result['IpWhiteList'] = self.ip_white_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpWhiteList') is not None:
            self.ip_white_list = m.get('IpWhiteList')

        return self

