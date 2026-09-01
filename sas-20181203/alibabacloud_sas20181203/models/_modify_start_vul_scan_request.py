# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyStartVulScanRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        resource_directory_account_id: int = None,
        types: str = None,
        uuids: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. Different requests should use different tokens. The token supports only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        self.resource_directory_account_id = resource_directory_account_id
        # Settings for the types of vulnerabilities to detect by using the one-click scan feature. Valid values:
        # - **cve**: Linux software vulnerability.
        # - **sys**: Windows system vulnerability.
        # - **cms**: Web-CMS vulnerability.
        # - **app**: application vulnerability detected by the web scanner.
        # - **emg**: urgent vulnerability.
        # - **image**: container image vulnerability.
        # - **sca**: application vulnerability detected by software constituency parsing.
        # > If this parameter is left empty, all vulnerability types are detected.
        self.types = types
        # The UUIDs of the servers. Separate multiple UUIDs with commas (,).
        # 
        # > You can call the [DescribeCloudCenterInstances](https://help.aliyun.com/document_detail/421726.html) operation to obtain this parameter.
        self.uuids = uuids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        if self.types is not None:
            result['Types'] = self.types

        if self.uuids is not None:
            result['Uuids'] = self.uuids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('Types') is not None:
            self.types = m.get('Types')

        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')

        return self

