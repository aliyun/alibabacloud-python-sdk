# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InvokeEsRequestRequest(DaraModel):
    def __init__(
        self,
        body: str = None,
        credential_id: str = None,
        method: str = None,
        path: str = None,
        system: bool = None,
    ):
        # The request body passed through to ES. Set this parameter based on the requirements of the target ES API. This parameter is not required for calls such as GET that do not have a request body.
        self.body = body
        # The ID of the credential to use. If this parameter is not specified, the default credential of the instance is used.
        self.credential_id = credential_id
        # The HTTP method used to access ES. Default value: GET.
        self.method = method
        # The ES path to access. This parameter is required. The leading / can be omitted.
        # 
        # This parameter is required.
        self.path = path
        # Specifies whether to use the Alibaba Cloud ES system credential. Default value: false.
        self.system = system

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body

        if self.credential_id is not None:
            result['credentialId'] = self.credential_id

        if self.method is not None:
            result['method'] = self.method

        if self.path is not None:
            result['path'] = self.path

        if self.system is not None:
            result['system'] = self.system

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')

        if m.get('credentialId') is not None:
            self.credential_id = m.get('credentialId')

        if m.get('method') is not None:
            self.method = m.get('method')

        if m.get('path') is not None:
            self.path = m.get('path')

        if m.get('system') is not None:
            self.system = m.get('system')

        return self

