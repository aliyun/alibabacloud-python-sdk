# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class ListModelServicesResponseBody(DaraModel):
    def __init__(
        self,
        model_services: List[main_models.ListModelServicesResponseBodyModelServices] = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        self.model_services = model_services
        self.page_number = page_number
        self.page_record_count = page_record_count
        self.request_id = request_id
        self.total_record_count = total_record_count

    def validate(self):
        if self.model_services:
            for v1 in self.model_services:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ModelServices'] = []
        if self.model_services is not None:
            for k1 in self.model_services:
                result['ModelServices'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.model_services = []
        if m.get('ModelServices') is not None:
            for k1 in m.get('ModelServices'):
                temp_model = main_models.ListModelServicesResponseBodyModelServices()
                self.model_services.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class ListModelServicesResponseBodyModelServices(DaraModel):
    def __init__(
        self,
        ai_nodes: List[str] = None,
        api_key: str = None,
        create_time: str = None,
        description: str = None,
        model_name: str = None,
        model_params: Dict[str, str] = None,
        model_service_id: str = None,
        private_conn_url: str = None,
        public_conn_url: str = None,
        security_iplist: str = None,
        status: str = None,
    ):
        self.ai_nodes = ai_nodes
        self.api_key = api_key
        self.create_time = create_time
        self.description = description
        self.model_name = model_name
        self.model_params = model_params
        self.model_service_id = model_service_id
        self.private_conn_url = private_conn_url
        self.public_conn_url = public_conn_url
        self.security_iplist = security_iplist
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_nodes is not None:
            result['AiNodes'] = self.ai_nodes

        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.model_params is not None:
            result['ModelParams'] = self.model_params

        if self.model_service_id is not None:
            result['ModelServiceId'] = self.model_service_id

        if self.private_conn_url is not None:
            result['PrivateConnUrl'] = self.private_conn_url

        if self.public_conn_url is not None:
            result['PublicConnUrl'] = self.public_conn_url

        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AiNodes') is not None:
            self.ai_nodes = m.get('AiNodes')

        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('ModelParams') is not None:
            self.model_params = m.get('ModelParams')

        if m.get('ModelServiceId') is not None:
            self.model_service_id = m.get('ModelServiceId')

        if m.get('PrivateConnUrl') is not None:
            self.private_conn_url = m.get('PrivateConnUrl')

        if m.get('PublicConnUrl') is not None:
            self.public_conn_url = m.get('PublicConnUrl')

        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

