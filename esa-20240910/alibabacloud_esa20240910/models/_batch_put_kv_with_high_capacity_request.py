# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchPutKvWithHighCapacityRequest(DaraModel):
    def __init__(
        self,
        namespace: str = None,
        url: str = None,
    ):
        # The namespace name specified when you called [CreateKvNamespace](https://help.aliyun.com/document_detail/2850317.html).
        # 
        # This parameter is required.
        self.namespace = namespace
        # A publicly accessible HTTP(S) URL that points to a JSON file containing the key-value pairs to be batch set. The server actively downloads the content from this URL.
        # 
        # - If you use an SDK, the SDK automatically uploads the file and generates the URL.
        # 
        # - In non-SDK scenarios, upload the JSON payload to any publicly accessible HTTP service and specify the URL.
        # 
        # The file content pointed to by the URL must be in the following JSON format: {"Namespace":"<namespace name>","KvList":[{"Key":"<key>","Value":"<value>"},...]}.If the URL content does not match this format, the API silently returns an empty SuccessKeys array.
        # 
        # This parameter is required.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

