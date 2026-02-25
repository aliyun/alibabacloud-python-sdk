# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class HTTPGetAction(DaraModel):
    def __init__(
        self,
        host: str = None,
        http_headers: List[main_models.HTTPHeader] = None,
        path: str = None,
        port: int = None,
        scheme: str = None,
    ):
        # The hostname to which you want to connect. The default value is the IP address of the pod. You may need to specify Host in HttpHeaders.
        self.host = host
        # The custom headers that you need to specify in the request. Duplicate headers are allowed in an HTTP request.
        self.http_headers = http_headers
        # The path of a URL.
        self.path = path
        # The port range. Valid values: 1 to 65535.
        self.port = port
        # The scheme that you want to use to connect to the host. Default value: http.
        self.scheme = scheme

    def validate(self):
        if self.http_headers:
            for v1 in self.http_headers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host is not None:
            result['Host'] = self.host

        result['HttpHeaders'] = []
        if self.http_headers is not None:
            for k1 in self.http_headers:
                result['HttpHeaders'].append(k1.to_map() if k1 else None)

        if self.path is not None:
            result['Path'] = self.path

        if self.port is not None:
            result['Port'] = self.port

        if self.scheme is not None:
            result['Scheme'] = self.scheme

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')

        self.http_headers = []
        if m.get('HttpHeaders') is not None:
            for k1 in m.get('HttpHeaders'):
                temp_model = main_models.HTTPHeader()
                self.http_headers.append(temp_model.from_map(k1))

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')

        return self

