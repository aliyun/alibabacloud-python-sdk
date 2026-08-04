# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_account_crm20160606 import models as main_models
from darabonba.model import DaraModel

class QueryBindsByOuterIdResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.QueryBindsByOuterIdResponseBodyData] = None,
        http_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.http_code is not None:
            result['HttpCode'] = self.http_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.QueryBindsByOuterIdResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryBindsByOuterIdResponseBodyData(DaraModel):
    def __init__(
        self,
        bind_data: Dict[str, Any] = None,
        minor_outer_id: str = None,
        outer_id: str = None,
        pk: str = None,
        status: str = None,
        tenant_id: str = None,
    ):
        self.bind_data = bind_data
        self.minor_outer_id = minor_outer_id
        self.outer_id = outer_id
        self.pk = pk
        self.status = status
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_data is not None:
            result['BindData'] = self.bind_data

        if self.minor_outer_id is not None:
            result['MinorOuterId'] = self.minor_outer_id

        if self.outer_id is not None:
            result['OuterId'] = self.outer_id

        if self.pk is not None:
            result['Pk'] = self.pk

        if self.status is not None:
            result['Status'] = self.status

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindData') is not None:
            self.bind_data = m.get('BindData')

        if m.get('MinorOuterId') is not None:
            self.minor_outer_id = m.get('MinorOuterId')

        if m.get('OuterId') is not None:
            self.outer_id = m.get('OuterId')

        if m.get('Pk') is not None:
            self.pk = m.get('Pk')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

