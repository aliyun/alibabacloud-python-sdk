# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ecd20201002 import models as main_models
from darabonba.model import DaraModel

class GetCloudDriveServiceMountTokenResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        token: main_models.GetCloudDriveServiceMountTokenResponseBodyToken = None,
    ):
        self.request_id = request_id
        # The tokens.
        self.token = token

    def validate(self):
        if self.token:
            self.token.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.token is not None:
            result['Token'] = self.token.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Token') is not None:
            temp_model = main_models.GetCloudDriveServiceMountTokenResponseBodyToken()
            self.token = temp_model.from_map(m.get('Token'))

        return self

class GetCloudDriveServiceMountTokenResponseBodyToken(DaraModel):
    def __init__(
        self,
        domain_id: str = None,
        expired_after: str = None,
        status: str = None,
        token: str = None,
        total_size: int = None,
        used_size: int = None,
    ):
        self.domain_id = domain_id
        self.expired_after = expired_after
        self.status = status
        # The token.
        self.token = token
        # The total capacity of the enterprise drive. Unit: GiB
        self.total_size = total_size
        self.used_size = used_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id

        if self.expired_after is not None:
            result['ExpiredAfter'] = self.expired_after

        if self.status is not None:
            result['Status'] = self.status

        if self.token is not None:
            result['Token'] = self.token

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        if self.used_size is not None:
            result['UsedSize'] = self.used_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')

        if m.get('ExpiredAfter') is not None:
            self.expired_after = m.get('ExpiredAfter')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        if m.get('UsedSize') is not None:
            self.used_size = m.get('UsedSize')

        return self

