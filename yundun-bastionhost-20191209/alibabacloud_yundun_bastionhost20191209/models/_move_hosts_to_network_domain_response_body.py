# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class MoveHostsToNetworkDomainResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[main_models.MoveHostsToNetworkDomainResponseBodyResults] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The result of the call.
        self.results = results

    def validate(self):
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['Results'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.results = []
        if m.get('Results') is not None:
            for k1 in m.get('Results'):
                temp_model = main_models.MoveHostsToNetworkDomainResponseBodyResults()
                self.results.append(temp_model.from_map(k1))

        return self

class MoveHostsToNetworkDomainResponseBodyResults(DaraModel):
    def __init__(
        self,
        code: str = None,
        host_id: str = None,
        message: str = None,
    ):
        # The return code that indicates whether the host is added to the network domain.
        # 
        # > The code LICENSE_OUT_OF_LIMIT indicates that the network domain feature is not supported by the current Bastionhost edition.
        self.code = code
        # The host ID.
        self.host_id = host_id
        # The error message that is returned.
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

        if self.host_id is not None:
            result['HostId'] = self.host_id

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

