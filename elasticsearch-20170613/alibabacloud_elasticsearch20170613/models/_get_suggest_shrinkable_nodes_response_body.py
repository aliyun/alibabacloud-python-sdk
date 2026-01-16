# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class GetSuggestShrinkableNodesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.GetSuggestShrinkableNodesResponseBodyResult] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The return results.
        self.result = result

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.GetSuggestShrinkableNodesResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class GetSuggestShrinkableNodesResponseBodyResult(DaraModel):
    def __init__(
        self,
        host: str = None,
        port: int = None,
    ):
        # The IP address of the node.
        self.host = host
        # The access port number of the node.
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host is not None:
            result['host'] = self.host

        if self.port is not None:
            result['port'] = self.port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('host') is not None:
            self.host = m.get('host')

        if m.get('port') is not None:
            self.port = m.get('port')

        return self

