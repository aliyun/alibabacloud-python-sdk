# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class CreateDataSourceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        create_result: main_models.CreateDataSourceResponseBodyCreateResult = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.create_result = create_result
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.create_result:
            self.create_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.create_result is not None:
            result['CreateResult'] = self.create_result.to_map()

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

        if m.get('CreateResult') is not None:
            temp_model = main_models.CreateDataSourceResponseBodyCreateResult()
            self.create_result = temp_model.from_map(m.get('CreateResult'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreateDataSourceResponseBodyCreateResult(DaraModel):
    def __init__(
        self,
        dev_data_source_id: int = None,
        prod_data_source_id: int = None,
    ):
        self.dev_data_source_id = dev_data_source_id
        self.prod_data_source_id = prod_data_source_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dev_data_source_id is not None:
            result['DevDataSourceId'] = self.dev_data_source_id

        if self.prod_data_source_id is not None:
            result['ProdDataSourceId'] = self.prod_data_source_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DevDataSourceId') is not None:
            self.dev_data_source_id = m.get('DevDataSourceId')

        if m.get('ProdDataSourceId') is not None:
            self.prod_data_source_id = m.get('ProdDataSourceId')

        return self

