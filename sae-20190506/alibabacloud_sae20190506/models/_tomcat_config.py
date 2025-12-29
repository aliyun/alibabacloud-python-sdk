# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TomcatConfig(DaraModel):
    def __init__(
        self,
        context_path: str = None,
        max_threads: int = None,
        port: int = None,
        uri_encoding: str = None,
        use_body_encoding_for_uri: bool = None,
        version: str = None,
    ):
        self.context_path = context_path
        self.max_threads = max_threads
        self.port = port
        self.uri_encoding = uri_encoding
        self.use_body_encoding_for_uri = use_body_encoding_for_uri
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.context_path is not None:
            result['ContextPath'] = self.context_path

        if self.max_threads is not None:
            result['MaxThreads'] = self.max_threads

        if self.port is not None:
            result['Port'] = self.port

        if self.uri_encoding is not None:
            result['UriEncoding'] = self.uri_encoding

        if self.use_body_encoding_for_uri is not None:
            result['UseBodyEncodingForUri'] = self.use_body_encoding_for_uri

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContextPath') is not None:
            self.context_path = m.get('ContextPath')

        if m.get('MaxThreads') is not None:
            self.max_threads = m.get('MaxThreads')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('UriEncoding') is not None:
            self.uri_encoding = m.get('UriEncoding')

        if m.get('UseBodyEncodingForUri') is not None:
            self.use_body_encoding_for_uri = m.get('UseBodyEncodingForUri')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

