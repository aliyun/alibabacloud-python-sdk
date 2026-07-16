# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import BinaryIO

from darabonba.model import DaraModel

class PutKvWithHighCapacityAdvanceRequest(DaraModel):
    def __init__(
        self,
        key: str = None,
        namespace: str = None,
        url_object: BinaryIO = None,
    ):
        # The key name to set. The key name can be up to 512 characters in length and cannot contain spaces or backslashes (/).
        # 
        # This parameter is required.
        self.key = key
        # The name specified when you called the [CreateKvNamespace](https://help.aliyun.com/document_detail/2850317.html) operation.
        # 
        # This parameter is required.
        self.namespace = namespace
        # A publicly accessible HTTP or HTTPS URL that points to a JSON file containing the key-value pair to set. The server actively downloads the content from this URL.
        # 
        # - If you use an SDK, the SDK automatically uploads the file and generates the URL.
        # 
        # - In non-SDK scenarios, upload the JSON payload to any publicly accessible HTTP service and specify the URL.
        # 
        # The file content pointed to by the URL must be in the following JSON format: {"Namespace":"<namespace>","Key":"<key>","Value":"<value>"}.
        # 
        # This parameter is required.
        self.url_object = url_object

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.url_object is not None:
            result['Url'] = self.url_object

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Url') is not None:
            self.url_object = m.get('Url')

        return self

