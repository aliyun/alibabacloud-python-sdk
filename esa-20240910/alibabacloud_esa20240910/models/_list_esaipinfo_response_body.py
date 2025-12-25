# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListESAIPInfoResponseBody(DaraModel):
    def __init__(
        self,
        content: List[main_models.ListESAIPInfoResponseBodyContent] = None,
        request_id: str = None,
    ):
        # The objects that are returned.
        self.content = content
        # The request ID.
        # 
        # Example D03F9502-6653-127C-8A5F-0647197\\*\\*\\*\\*\\*
        self.request_id = request_id

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['Content'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('Content') is not None:
            for k1 in m.get('Content'):
                temp_model = main_models.ListESAIPInfoResponseBodyContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListESAIPInfoResponseBodyContent(DaraModel):
    def __init__(
        self,
        cdn_ip: str = None,
        ip: str = None,
    ):
        # Whether the IP address in the parameter belongs to ESA POPs.
        # 
        # *   **true**
        # *   **false**
        self.cdn_ip = cdn_ip
        # The IP addresses.
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cdn_ip is not None:
            result['CdnIp'] = self.cdn_ip

        if self.ip is not None:
            result['Ip'] = self.ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdnIp') is not None:
            self.cdn_ip = m.get('CdnIp')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        return self

