# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetLatestSubmitDetailRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        submit_detail_query: main_models.GetLatestSubmitDetailRequestSubmitDetailQuery = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.submit_detail_query = submit_detail_query

    def validate(self):
        if self.submit_detail_query:
            self.submit_detail_query.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.submit_detail_query is not None:
            result['SubmitDetailQuery'] = self.submit_detail_query.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('SubmitDetailQuery') is not None:
            temp_model = main_models.GetLatestSubmitDetailRequestSubmitDetailQuery()
            self.submit_detail_query = temp_model.from_map(m.get('SubmitDetailQuery'))

        return self

class GetLatestSubmitDetailRequestSubmitDetailQuery(DaraModel):
    def __init__(
        self,
        object_id: str = None,
        object_type: str = None,
    ):
        # This parameter is required.
        self.object_id = object_id
        # This parameter is required.
        self.object_type = object_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.object_id is not None:
            result['ObjectId'] = self.object_id

        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')

        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        return self

