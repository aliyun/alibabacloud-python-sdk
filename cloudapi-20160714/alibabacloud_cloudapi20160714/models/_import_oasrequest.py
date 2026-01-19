# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImportOASRequest(DaraModel):
    def __init__(
        self,
        auth_type: str = None,
        backend_name: str = None,
        data: str = None,
        group_id: str = None,
        ignore_warning: bool = None,
        oasversion: str = None,
        overwrite: bool = None,
        request_mode: str = None,
        security_token: str = None,
        skip_dry_run: bool = None,
    ):
        # The security authentication method of the API. Valid values:
        # 
        # *   **APP: Only authorized applications can call the API.**
        # 
        # *   **ANONYMOUS: The API can be anonymously called. In this mode, you must take note of the following rules:**
        # 
        #     *   All users who have obtained the API service information can call this API. API Gateway does not authenticate callers and cannot set user-specific throttling policies. If you make this API public, set API-specific throttling policies.
        self.auth_type = auth_type
        # The name of the backend service.
        self.backend_name = backend_name
        # The OAS-compliant text file or OSS object URL.
        # 
        # This parameter is required.
        self.data = data
        # The ID of the API group.
        # 
        # This parameter is required.
        self.group_id = group_id
        # Specifies whether to ignore alerts.
        self.ignore_warning = ignore_warning
        # The OAS version.
        self.oasversion = oasversion
        # Specifies whether to overwrite an existing API.
        # 
        # If an existing API has the same HTTP request type and backend request path as the API to be imported, the existing API is overwritten.
        # 
        # This parameter is required.
        self.overwrite = overwrite
        # The request mode. Valid values:
        # 
        # *   MAPPING: Parameters are mapped. Unknown parameters are filtered out.
        # *   PASSTHROUGH: Parameters are passed through.
        self.request_mode = request_mode
        self.security_token = security_token
        # Specifies whether to directly import the API without performing a precheck.
        self.skip_dry_run = skip_dry_run

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type

        if self.backend_name is not None:
            result['BackendName'] = self.backend_name

        if self.data is not None:
            result['Data'] = self.data

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.ignore_warning is not None:
            result['IgnoreWarning'] = self.ignore_warning

        if self.oasversion is not None:
            result['OASVersion'] = self.oasversion

        if self.overwrite is not None:
            result['Overwrite'] = self.overwrite

        if self.request_mode is not None:
            result['RequestMode'] = self.request_mode

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.skip_dry_run is not None:
            result['SkipDryRun'] = self.skip_dry_run

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')

        if m.get('BackendName') is not None:
            self.backend_name = m.get('BackendName')

        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('IgnoreWarning') is not None:
            self.ignore_warning = m.get('IgnoreWarning')

        if m.get('OASVersion') is not None:
            self.oasversion = m.get('OASVersion')

        if m.get('Overwrite') is not None:
            self.overwrite = m.get('Overwrite')

        if m.get('RequestMode') is not None:
            self.request_mode = m.get('RequestMode')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('SkipDryRun') is not None:
            self.skip_dry_run = m.get('SkipDryRun')

        return self

