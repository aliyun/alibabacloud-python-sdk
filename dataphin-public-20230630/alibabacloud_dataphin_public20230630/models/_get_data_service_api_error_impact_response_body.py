# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetDataServiceApiErrorImpactResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetDataServiceApiErrorImpactResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

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
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetDataServiceApiErrorImpactResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetDataServiceApiErrorImpactResponseBodyData(DaraModel):
    def __init__(
        self,
        error_api_list: List[main_models.GetDataServiceApiErrorImpactResponseBodyDataErrorApiList] = None,
        error_app_list: List[main_models.GetDataServiceApiErrorImpactResponseBodyDataErrorAppList] = None,
    ):
        self.error_api_list = error_api_list
        self.error_app_list = error_app_list

    def validate(self):
        if self.error_api_list:
            for v1 in self.error_api_list:
                 if v1:
                    v1.validate()
        if self.error_app_list:
            for v1 in self.error_app_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ErrorApiList'] = []
        if self.error_api_list is not None:
            for k1 in self.error_api_list:
                result['ErrorApiList'].append(k1.to_map() if k1 else None)

        result['ErrorAppList'] = []
        if self.error_app_list is not None:
            for k1 in self.error_app_list:
                result['ErrorAppList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.error_api_list = []
        if m.get('ErrorApiList') is not None:
            for k1 in m.get('ErrorApiList'):
                temp_model = main_models.GetDataServiceApiErrorImpactResponseBodyDataErrorApiList()
                self.error_api_list.append(temp_model.from_map(k1))

        self.error_app_list = []
        if m.get('ErrorAppList') is not None:
            for k1 in m.get('ErrorAppList'):
                temp_model = main_models.GetDataServiceApiErrorImpactResponseBodyDataErrorAppList()
                self.error_app_list.append(temp_model.from_map(k1))

        return self

class GetDataServiceApiErrorImpactResponseBodyDataErrorAppList(DaraModel):
    def __init__(
        self,
        app_id: int = None,
        app_key: int = None,
        app_name: str = None,
        error_count: int = None,
    ):
        # appId
        self.app_id = app_id
        # appKey
        self.app_key = app_key
        self.app_name = app_name
        self.error_count = error_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.error_count is not None:
            result['ErrorCount'] = self.error_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ErrorCount') is not None:
            self.error_count = m.get('ErrorCount')

        return self

class GetDataServiceApiErrorImpactResponseBodyDataErrorApiList(DaraModel):
    def __init__(
        self,
        api_name: str = None,
        app_id: int = None,
        error_count: int = None,
    ):
        self.api_name = api_name
        self.app_id = app_id
        self.error_count = error_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_name is not None:
            result['ApiName'] = self.api_name

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.error_count is not None:
            result['ErrorCount'] = self.error_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ErrorCount') is not None:
            self.error_count = m.get('ErrorCount')

        return self

