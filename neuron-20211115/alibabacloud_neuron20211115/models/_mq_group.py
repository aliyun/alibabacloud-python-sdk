# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MqGroup(DaraModel):
    def __init__(
        self,
        env: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        group_id: str = None,
        id: int = None,
        message_type: int = None,
        protocol_type: str = None,
        remark: str = None,
        request_id: str = None,
        service_id: str = None,
    ):
        self.env = env
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.group_id = group_id
        self.id = id
        self.message_type = message_type
        self.protocol_type = protocol_type
        self.remark = remark
        self.request_id = request_id
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.env is not None:
            result['env'] = self.env

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.id is not None:
            result['id'] = self.id

        if self.message_type is not None:
            result['messageType'] = self.message_type

        if self.protocol_type is not None:
            result['protocolType'] = self.protocol_type

        if self.remark is not None:
            result['remark'] = self.remark

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('env') is not None:
            self.env = m.get('env')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('messageType') is not None:
            self.message_type = m.get('messageType')

        if m.get('protocolType') is not None:
            self.protocol_type = m.get('protocolType')

        if m.get('remark') is not None:
            self.remark = m.get('remark')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        return self

