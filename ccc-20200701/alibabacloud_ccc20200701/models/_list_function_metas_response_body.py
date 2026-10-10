# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ccc20200701 import models as main_models
from darabonba.model import DaraModel

class ListFunctionMetasResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListFunctionMetasResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListFunctionMetasResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListFunctionMetasResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListFunctionMetasResponseBodyDataList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.list = list
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.ListFunctionMetasResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListFunctionMetasResponseBodyDataList(DaraModel):
    def __init__(
        self,
        aliyun_uid: str = None,
        description: str = None,
        failover_region: str = None,
        failover_region_weight: float = None,
        function_meta_id: str = None,
        function_name: str = None,
        http_trigger_url: str = None,
        instance_id: str = None,
        region: int = None,
        role: str = None,
        service: str = None,
    ):
        self.aliyun_uid = aliyun_uid
        self.description = description
        self.failover_region = failover_region
        self.failover_region_weight = failover_region_weight
        self.function_meta_id = function_meta_id
        self.function_name = function_name
        self.http_trigger_url = http_trigger_url
        self.instance_id = instance_id
        self.region = region
        self.role = role
        self.service = service

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_uid is not None:
            result['AliyunUid'] = self.aliyun_uid

        if self.description is not None:
            result['Description'] = self.description

        if self.failover_region is not None:
            result['FailoverRegion'] = self.failover_region

        if self.failover_region_weight is not None:
            result['FailoverRegionWeight'] = self.failover_region_weight

        if self.function_meta_id is not None:
            result['FunctionMetaId'] = self.function_meta_id

        if self.function_name is not None:
            result['FunctionName'] = self.function_name

        if self.http_trigger_url is not None:
            result['HttpTriggerUrl'] = self.http_trigger_url

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region is not None:
            result['Region'] = self.region

        if self.role is not None:
            result['Role'] = self.role

        if self.service is not None:
            result['Service'] = self.service

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunUid') is not None:
            self.aliyun_uid = m.get('AliyunUid')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FailoverRegion') is not None:
            self.failover_region = m.get('FailoverRegion')

        if m.get('FailoverRegionWeight') is not None:
            self.failover_region_weight = m.get('FailoverRegionWeight')

        if m.get('FunctionMetaId') is not None:
            self.function_meta_id = m.get('FunctionMetaId')

        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')

        if m.get('HttpTriggerUrl') is not None:
            self.http_trigger_url = m.get('HttpTriggerUrl')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('Service') is not None:
            self.service = m.get('Service')

        return self

