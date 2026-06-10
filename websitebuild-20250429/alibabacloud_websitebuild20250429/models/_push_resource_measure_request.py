# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PushResourceMeasureRequest(DaraModel):
    def __init__(
        self,
        amount: int = None,
        belong_id: str = None,
        belong_id_type: str = None,
        biz_id: str = None,
        measure_data: str = None,
        meta_data: str = None,
        resource_code: str = None,
        use_time: str = None,
        use_type: str = None,
    ):
        # Resource usage amount
        self.amount = amount
        # Belonging ID
        self.belong_id = belong_id
        # Belonging ID Type (siteId, uid)
        self.belong_id_type = belong_id_type
        # Business ID associated with this push, such as session ID, Job ID, or file ID
        self.biz_id = biz_id
        # Metering data, used to flexibly push multiple data points such as model invocation count and token usage (JSON string)
        self.measure_data = measure_data
        # Business extension metadata (in Map format, must be a JSON string)
        self.meta_data = meta_data
        # Resource identity
        self.resource_code = resource_code
        # Usage time, format: yyyy-MM-dd HH:mm:ss
        self.use_time = use_time
        # Usage type
        self.use_type = use_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.belong_id is not None:
            result['BelongId'] = self.belong_id

        if self.belong_id_type is not None:
            result['BelongIdType'] = self.belong_id_type

        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.measure_data is not None:
            result['MeasureData'] = self.measure_data

        if self.meta_data is not None:
            result['MetaData'] = self.meta_data

        if self.resource_code is not None:
            result['ResourceCode'] = self.resource_code

        if self.use_time is not None:
            result['UseTime'] = self.use_time

        if self.use_type is not None:
            result['UseType'] = self.use_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('BelongId') is not None:
            self.belong_id = m.get('BelongId')

        if m.get('BelongIdType') is not None:
            self.belong_id_type = m.get('BelongIdType')

        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('MeasureData') is not None:
            self.measure_data = m.get('MeasureData')

        if m.get('MetaData') is not None:
            self.meta_data = m.get('MetaData')

        if m.get('ResourceCode') is not None:
            self.resource_code = m.get('ResourceCode')

        if m.get('UseTime') is not None:
            self.use_time = m.get('UseTime')

        if m.get('UseType') is not None:
            self.use_type = m.get('UseType')

        return self

