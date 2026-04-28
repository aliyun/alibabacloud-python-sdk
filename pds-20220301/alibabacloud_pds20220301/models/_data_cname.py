# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DataCName(DaraModel):
    def __init__(
        self,
        cert_expire_time: int = None,
        cert_name: str = None,
        cname: str = None,
        cname_type: str = None,
        location: str = None,
        store_id: str = None,
    ):
        self.cert_expire_time = cert_expire_time
        self.cert_name = cert_name
        self.cname = cname
        self.cname_type = cname_type
        self.location = location
        self.store_id = store_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_expire_time is not None:
            result['cert_expire_time'] = self.cert_expire_time

        if self.cert_name is not None:
            result['cert_name'] = self.cert_name

        if self.cname is not None:
            result['cname'] = self.cname

        if self.cname_type is not None:
            result['cname_type'] = self.cname_type

        if self.location is not None:
            result['location'] = self.location

        if self.store_id is not None:
            result['store_id'] = self.store_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cert_expire_time') is not None:
            self.cert_expire_time = m.get('cert_expire_time')

        if m.get('cert_name') is not None:
            self.cert_name = m.get('cert_name')

        if m.get('cname') is not None:
            self.cname = m.get('cname')

        if m.get('cname_type') is not None:
            self.cname_type = m.get('cname_type')

        if m.get('location') is not None:
            self.location = m.get('location')

        if m.get('store_id') is not None:
            self.store_id = m.get('store_id')

        return self

