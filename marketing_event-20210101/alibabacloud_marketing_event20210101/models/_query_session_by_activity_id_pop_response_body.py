# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_marketing_event20210101 import models as main_models
from darabonba.model import DaraModel

class QuerySessionByActivityIdPopResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: List[main_models.QuerySessionByActivityIdPopResponseBodyData] = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
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

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.QuerySessionByActivityIdPopResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QuerySessionByActivityIdPopResponseBodyData(DaraModel):
    def __init__(
        self,
        description: str = None,
        description_en: str = None,
        end_date_time: str = None,
        id: int = None,
        location: str = None,
        name: str = None,
        name_en: str = None,
        start_date_time: str = None,
    ):
        self.description = description
        self.description_en = description_en
        self.end_date_time = end_date_time
        self.id = id
        self.location = location
        self.name = name
        self.name_en = name_en
        self.start_date_time = start_date_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.description_en is not None:
            result['DescriptionEn'] = self.description_en

        if self.end_date_time is not None:
            result['EndDateTime'] = self.end_date_time

        if self.id is not None:
            result['Id'] = self.id

        if self.location is not None:
            result['Location'] = self.location

        if self.name is not None:
            result['Name'] = self.name

        if self.name_en is not None:
            result['NameEn'] = self.name_en

        if self.start_date_time is not None:
            result['StartDateTime'] = self.start_date_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DescriptionEn') is not None:
            self.description_en = m.get('DescriptionEn')

        if m.get('EndDateTime') is not None:
            self.end_date_time = m.get('EndDateTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NameEn') is not None:
            self.name_en = m.get('NameEn')

        if m.get('StartDateTime') is not None:
            self.start_date_time = m.get('StartDateTime')

        return self

