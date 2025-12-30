# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListDataServiceApiCallsRequest(DaraModel):
    def __init__(
        self,
        list_query: main_models.ListDataServiceApiCallsRequestListQuery = None,
        op_tenant_id: int = None,
        project_id: int = None,
    ):
        # This parameter is required.
        self.list_query = list_query
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        if self.list_query:
            self.list_query.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.list_query is not None:
            result['ListQuery'] = self.list_query.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListQuery') is not None:
            temp_model = main_models.ListDataServiceApiCallsRequestListQuery()
            self.list_query = temp_model.from_map(m.get('ListQuery'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

class ListDataServiceApiCallsRequestListQuery(DaraModel):
    def __init__(
        self,
        api_id: int = None,
        api_name: str = None,
        app_key: int = None,
        client_ip: str = None,
        end_time: str = None,
        page_no: int = None,
        page_size: int = None,
        start_time: str = None,
        successful: bool = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        # appKey
        self.app_key = app_key
        self.client_ip = client_ip
        # This parameter is required.
        self.end_time = end_time
        self.page_no = page_no
        self.page_size = page_size
        # This parameter is required.
        self.start_time = start_time
        self.successful = successful

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.api_name is not None:
            result['ApiName'] = self.api_name

        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.successful is not None:
            result['Successful'] = self.successful

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')

        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Successful') is not None:
            self.successful = m.get('Successful')

        return self

