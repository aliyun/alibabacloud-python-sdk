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
        # Model services.
        self.model_services = model_services
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries per page.
        self.page_record_count = page_record_count
        # Request ID.
        self.request_id = request_id
        # The total number of entries returned.
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
        # A list of AI nodes for model deployment.
        self.ai_nodes = ai_nodes
        # The API key.
        self.api_key = api_key
        # The creation time.
        self.create_time = create_time
        # The description.
        self.description = description
        # The model name.
        self.model_name = model_name
        # Model service parameters (not available).
        self.model_params = model_params
        # Model service ID.
        self.model_service_id = model_service_id
        # Private Endpoint.
        self.private_conn_url = private_conn_url
        # Public endpoint.
        self.public_conn_url = public_conn_url
        # The IP addresses listed in the whitelist. Up to 1,000 IP addresses are contained in a whitelist and separated by commas (,). The IP addresses must use one of the following formats:
        # 
        # *   0.0.0.0/0
        # *   10.23.12.24(IP)
        # *   10.23.12.24/24 (This is a CIDR block. The value`/24`indicates the network prefix length, which must be an integer and in the range of `[1,32]`.)
        self.security_iplist = security_iplist
        # The status of the operation. Valid values:
        # 
        # *   **success**
        # *   **fail**
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

