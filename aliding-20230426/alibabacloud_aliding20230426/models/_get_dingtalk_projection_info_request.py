# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GetDingtalkProjectionInfoRequest(DaraModel):
    def __init__(
        self,
        tenant_context: main_models.GetDingtalkProjectionInfoRequestTenantContext = None,
        client: str = None,
        end_ts: int = None,
        org_id: str = None,
        pub_work_no: str = None,
        room_id: str = None,
        start_ts: int = None,
        sub_uid: str = None,
    ):
        self.tenant_context = tenant_context
        self.client = client
        self.end_ts = end_ts
        self.org_id = org_id
        self.pub_work_no = pub_work_no
        self.room_id = room_id
        self.start_ts = start_ts
        self.sub_uid = sub_uid

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        if self.client is not None:
            result['client'] = self.client

        if self.end_ts is not None:
            result['endTs'] = self.end_ts

        if self.org_id is not None:
            result['orgId'] = self.org_id

        if self.pub_work_no is not None:
            result['pubWorkNo'] = self.pub_work_no

        if self.room_id is not None:
            result['roomId'] = self.room_id

        if self.start_ts is not None:
            result['startTs'] = self.start_ts

        if self.sub_uid is not None:
            result['subUid'] = self.sub_uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TenantContext') is not None:
            temp_model = main_models.GetDingtalkProjectionInfoRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        if m.get('client') is not None:
            self.client = m.get('client')

        if m.get('endTs') is not None:
            self.end_ts = m.get('endTs')

        if m.get('orgId') is not None:
            self.org_id = m.get('orgId')

        if m.get('pubWorkNo') is not None:
            self.pub_work_no = m.get('pubWorkNo')

        if m.get('roomId') is not None:
            self.room_id = m.get('roomId')

        if m.get('startTs') is not None:
            self.start_ts = m.get('startTs')

        if m.get('subUid') is not None:
            self.sub_uid = m.get('subUid')

        return self

class GetDingtalkProjectionInfoRequestTenantContext(DaraModel):
    def __init__(
        self,
        tenant_id: str = None,
    ):
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

