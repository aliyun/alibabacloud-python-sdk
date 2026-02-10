# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeWebLockStatusResponseBody(DaraModel):
    def __init__(
        self,
        auth_count: int = None,
        bind_count: int = None,
        block_count: int = None,
        dir_count: int = None,
        expire_time: int = None,
        request_id: str = None,
        white_count: int = None,
    ):
        # The total quota that you purchase for web tamper proofing.
        self.auth_count = auth_count
        # The associated tamper proofing quota.
        self.bind_count = bind_count
        # The number of blocked processes.
        self.block_count = block_count
        # The number of protected directories.
        self.dir_count = dir_count
        # The timestamp generated when the quota for tamper proofing expires. Unit: millisecond.
        self.expire_time = expire_time
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The number of processes in the whitelist.
        self.white_count = white_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_count is not None:
            result['AuthCount'] = self.auth_count

        if self.bind_count is not None:
            result['BindCount'] = self.bind_count

        if self.block_count is not None:
            result['BlockCount'] = self.block_count

        if self.dir_count is not None:
            result['DirCount'] = self.dir_count

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.white_count is not None:
            result['WhiteCount'] = self.white_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCount') is not None:
            self.auth_count = m.get('AuthCount')

        if m.get('BindCount') is not None:
            self.bind_count = m.get('BindCount')

        if m.get('BlockCount') is not None:
            self.block_count = m.get('BlockCount')

        if m.get('DirCount') is not None:
            self.dir_count = m.get('DirCount')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('WhiteCount') is not None:
            self.white_count = m.get('WhiteCount')

        return self

