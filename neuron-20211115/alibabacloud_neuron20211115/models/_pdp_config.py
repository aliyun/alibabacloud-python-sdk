# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PdpConfig(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        ask_id: str = None,
        context: str = None,
        enterprise_id: int = None,
        env: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        name: str = None,
        pbc_id: int = None,
        request_id: str = None,
        service_group_id: int = None,
        service_id: int = None,
        type: str = None,
    ):
        self.account_id = account_id
        self.account_name = account_name
        self.ask_id = ask_id
        # This parameter is required.
        self.context = context
        self.enterprise_id = enterprise_id
        self.env = env
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.name = name
        self.pbc_id = pbc_id
        self.request_id = request_id
        # This parameter is required.
        self.service_group_id = service_group_id
        self.service_id = service_id
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['accountId'] = self.account_id

        if self.account_name is not None:
            result['accountName'] = self.account_name

        if self.ask_id is not None:
            result['askId'] = self.ask_id

        if self.context is not None:
            result['context'] = self.context

        if self.enterprise_id is not None:
            result['enterpriseId'] = self.enterprise_id

        if self.env is not None:
            result['env'] = self.env

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.pbc_id is not None:
            result['pbcId'] = self.pbc_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.service_group_id is not None:
            result['serviceGroupId'] = self.service_group_id

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('accountName') is not None:
            self.account_name = m.get('accountName')

        if m.get('askId') is not None:
            self.ask_id = m.get('askId')

        if m.get('context') is not None:
            self.context = m.get('context')

        if m.get('enterpriseId') is not None:
            self.enterprise_id = m.get('enterpriseId')

        if m.get('env') is not None:
            self.env = m.get('env')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('pbcId') is not None:
            self.pbc_id = m.get('pbcId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('serviceGroupId') is not None:
            self.service_group_id = m.get('serviceGroupId')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

