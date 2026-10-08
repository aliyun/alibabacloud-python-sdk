# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryServerLockResponseBody(DaraModel):
    def __init__(
        self,
        domain_instance_id: str = None,
        domain_name: str = None,
        expire_date: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        lock_instance_id: str = None,
        lock_product_id: str = None,
        request_id: str = None,
        server_lock_status: int = None,
        start_date: str = None,
        user_id: str = None,
    ):
        # Domain instance ID.
        self.domain_instance_id = domain_instance_id
        # The queried domain name.
        self.domain_name = domain_name
        # Expiration Time.
        self.expire_date = expire_date
        # Creation Time.
        self.gmt_create = gmt_create
        # Updated At.
        self.gmt_modified = gmt_modified
        # Registry lock instance ID.
        self.lock_instance_id = lock_instance_id
        # Lock product ID.
        self.lock_product_id = lock_product_id
        # Request ID.
        self.request_id = request_id
        # Registry lock status. Valid values:
        # 
        # - 1: Disabled
        # - 2: Enabled
        # - 3: Shutdown
        self.server_lock_status = server_lock_status
        # The time when the lock takes effect.
        self.start_date = start_date
        # User UID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_instance_id is not None:
            result['DomainInstanceId'] = self.domain_instance_id

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.lock_instance_id is not None:
            result['LockInstanceId'] = self.lock_instance_id

        if self.lock_product_id is not None:
            result['LockProductId'] = self.lock_product_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.server_lock_status is not None:
            result['ServerLockStatus'] = self.server_lock_status

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainInstanceId') is not None:
            self.domain_instance_id = m.get('DomainInstanceId')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('LockInstanceId') is not None:
            self.lock_instance_id = m.get('LockInstanceId')

        if m.get('LockProductId') is not None:
            self.lock_product_id = m.get('LockProductId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ServerLockStatus') is not None:
            self.server_lock_status = m.get('ServerLockStatus')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

