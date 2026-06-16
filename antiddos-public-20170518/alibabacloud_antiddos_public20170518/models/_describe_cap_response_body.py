# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_antiddos_public20170518 import models as main_models
from darabonba.model import DaraModel

class DescribeCapResponseBody(DaraModel):
    def __init__(
        self,
        cap_url: main_models.DescribeCapResponseBodyCapUrl = None,
        request_id: str = None,
    ):
        # The download link to the traffic data that is captured when a DDoS attack event occurs.
        self.cap_url = cap_url
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.cap_url:
            self.cap_url.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cap_url is not None:
            result['CapUrl'] = self.cap_url.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CapUrl') is not None:
            temp_model = main_models.DescribeCapResponseBodyCapUrl()
            self.cap_url = temp_model.from_map(m.get('CapUrl'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCapResponseBodyCapUrl(DaraModel):
    def __init__(
        self,
        url: str = None,
    ):
        # The download link to the traffic data.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

