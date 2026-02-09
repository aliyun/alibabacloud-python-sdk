# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_brain_industrial20200920 import models as main_models
from darabonba.model import DaraModel

class ListUserResourcesResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: List[main_models.ListUserResourcesResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListUserResourcesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListUserResourcesResponseBodyData(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        commodity_code: str = None,
        end_date: str = None,
        instance_id: str = None,
        region: str = None,
        start_date: str = None,
        status: str = None,
        status_msg: str = None,
    ):
        self.charge_type = charge_type
        self.commodity_code = commodity_code
        self.end_date = end_date
        self.instance_id = instance_id
        self.region = region
        self.start_date = start_date
        self.status = status
        self.status_msg = status_msg

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type

        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code

        if self.end_date is not None:
            result['endDate'] = self.end_date

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.region is not None:
            result['region'] = self.region

        if self.start_date is not None:
            result['startDate'] = self.start_date

        if self.status is not None:
            result['status'] = self.status

        if self.status_msg is not None:
            result['statusMsg'] = self.status_msg

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')

        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')

        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('statusMsg') is not None:
            self.status_msg = m.get('statusMsg')

        return self

