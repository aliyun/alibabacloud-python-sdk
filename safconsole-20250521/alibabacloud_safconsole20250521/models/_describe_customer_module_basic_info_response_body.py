# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_safconsole20250521 import models as main_models
from darabonba.model import DaraModel

class DescribeCustomerModuleBasicInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        result_object: main_models.DescribeCustomerModuleBasicInfoResponseBodyResultObject = None,
        success: bool = None,
    ):
        # Status code. A return value of 200 indicates success.
        self.code = code
        # HTTP status code.
        self.http_status_code = http_status_code
        # Return message.
        self.message = message
        # Request ID
        self.request_id = request_id
        # Returned result.
        self.result_object = result_object
        # Indicates whether the application configuration information was successfully retrieved. Possible values: true: Success; false: Failure.
        self.success = success

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultObject') is not None:
            temp_model = main_models.DescribeCustomerModuleBasicInfoResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('ResultObject'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self



class DescribeCustomerModuleBasicInfoResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        customer_module_name: str = None,
        description: str = None,
        inner_module_name: str = None,
        module_type: str = None,
        store_path: str = None,
    ):
        # Customer model name.
        self.customer_module_name = customer_module_name
        # Remarks.
        self.description = description
        # Model identifier.
        self.inner_module_name = inner_module_name
        # Module type.
        self.module_type = module_type
        # Test address.
        self.store_path = store_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.customer_module_name is not None:
            result['CustomerModuleName'] = self.customer_module_name

        if self.description is not None:
            result['Description'] = self.description

        if self.inner_module_name is not None:
            result['InnerModuleName'] = self.inner_module_name

        if self.module_type is not None:
            result['ModuleType'] = self.module_type

        if self.store_path is not None:
            result['StorePath'] = self.store_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerModuleName') is not None:
            self.customer_module_name = m.get('CustomerModuleName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InnerModuleName') is not None:
            self.inner_module_name = m.get('InnerModuleName')

        if m.get('ModuleType') is not None:
            self.module_type = m.get('ModuleType')

        if m.get('StorePath') is not None:
            self.store_path = m.get('StorePath')

        return self

