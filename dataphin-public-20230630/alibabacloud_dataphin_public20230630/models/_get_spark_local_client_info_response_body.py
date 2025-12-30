# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetSparkLocalClientInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.GetSparkLocalClientInfoResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetSparkLocalClientInfoResponseBodyData()
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

class GetSparkLocalClientInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        client_file_resource_id: str = None,
        client_file_resource_name: str = None,
        client_name: str = None,
        editable: bool = None,
    ):
        self.client_file_resource_id = client_file_resource_id
        self.client_file_resource_name = client_file_resource_name
        self.client_name = client_name
        self.editable = editable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_file_resource_id is not None:
            result['ClientFileResourceId'] = self.client_file_resource_id

        if self.client_file_resource_name is not None:
            result['ClientFileResourceName'] = self.client_file_resource_name

        if self.client_name is not None:
            result['ClientName'] = self.client_name

        if self.editable is not None:
            result['Editable'] = self.editable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientFileResourceId') is not None:
            self.client_file_resource_id = m.get('ClientFileResourceId')

        if m.get('ClientFileResourceName') is not None:
            self.client_file_resource_name = m.get('ClientFileResourceName')

        if m.get('ClientName') is not None:
            self.client_name = m.get('ClientName')

        if m.get('Editable') is not None:
            self.editable = m.get('Editable')

        return self

