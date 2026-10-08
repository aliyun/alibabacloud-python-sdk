# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class GetJvmConfigurationResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        jvm_configuration: main_models.GetJvmConfigurationResponseBodyJvmConfiguration = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code that is returned.
        self.code = code
        # The JVM configuration of the application or instance group.
        self.jvm_configuration = jvm_configuration
        # The additional information that is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.jvm_configuration:
            self.jvm_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.jvm_configuration is not None:
            result['JvmConfiguration'] = self.jvm_configuration.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('JvmConfiguration') is not None:
            temp_model = main_models.GetJvmConfigurationResponseBodyJvmConfiguration()
            self.jvm_configuration = temp_model.from_map(m.get('JvmConfiguration'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetJvmConfigurationResponseBodyJvmConfiguration(DaraModel):
    def __init__(
        self,
        max_heap_size: int = None,
        max_perm_size: int = None,
        min_heap_size: int = None,
        options: str = None,
    ):
        # The maximum size of the heap memory. Unit: MB.
        self.max_heap_size = max_heap_size
        # The size of the permanent generation heap memory. Unit: MB.
        self.max_perm_size = max_perm_size
        # The initial size of the heap memory. Unit: MB.
        self.min_heap_size = min_heap_size
        # The custom parameter.
        self.options = options

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_heap_size is not None:
            result['MaxHeapSize'] = self.max_heap_size

        if self.max_perm_size is not None:
            result['MaxPermSize'] = self.max_perm_size

        if self.min_heap_size is not None:
            result['MinHeapSize'] = self.min_heap_size

        if self.options is not None:
            result['Options'] = self.options

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxHeapSize') is not None:
            self.max_heap_size = m.get('MaxHeapSize')

        if m.get('MaxPermSize') is not None:
            self.max_perm_size = m.get('MaxPermSize')

        if m.get('MinHeapSize') is not None:
            self.min_heap_size = m.get('MinHeapSize')

        if m.get('Options') is not None:
            self.options = m.get('Options')

        return self

