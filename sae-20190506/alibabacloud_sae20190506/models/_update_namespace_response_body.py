# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class UpdateNamespaceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.UpdateNamespaceResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # The HTTP status code. Valid values:
        # 
        # *   **2xx**: The call was successful.
        # *   **3xx**: The call was redirected.
        # *   **4xx**: The call failed.
        # *   **5xx**: A server error occurred.
        self.code = code
        # The information about a namespace.
        self.data = data
        # The error code returned. Take note of the following rules:
        # 
        # *   The **ErrorCode** parameter is not returned if the request succeeds.
        # *   If the call fails, the **ErrorCode** parameter is returned. For more information, see the "**Error codes**" section of this topic.
        self.error_code = error_code
        # The message returned for the operation.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the information about the namespace was updated. Valid values:
        # 
        # *   **true**: The instance was updated.
        # *   **false**: The instance failed to be updated.
        self.success = success
        # The trace ID that is used to query the details of the request.
        self.trace_id = trace_id

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

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.UpdateNamespaceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

class UpdateNamespaceResponseBodyData(DaraModel):
    def __init__(
        self,
        enable_micro_registration: bool = None,
        name_space_short_id: str = None,
        namespace_description: str = None,
        namespace_id: str = None,
        namespace_name: str = None,
        region_id: str = None,
    ):
        # Indicates whether to enable SAE built-in registry:
        # 
        # *   **true**
        # *   **false**
        self.enable_micro_registration = enable_micro_registration
        # The short ID of the namespace.
        self.name_space_short_id = name_space_short_id
        # The description of the namespace.
        self.namespace_description = namespace_description
        # The ID of the namespace.
        self.namespace_id = namespace_id
        # The name of the namespace.
        self.namespace_name = namespace_name
        # The region where the namespace resides.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_micro_registration is not None:
            result['EnableMicroRegistration'] = self.enable_micro_registration

        if self.name_space_short_id is not None:
            result['NameSpaceShortId'] = self.name_space_short_id

        if self.namespace_description is not None:
            result['NamespaceDescription'] = self.namespace_description

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableMicroRegistration') is not None:
            self.enable_micro_registration = m.get('EnableMicroRegistration')

        if m.get('NameSpaceShortId') is not None:
            self.name_space_short_id = m.get('NameSpaceShortId')

        if m.get('NamespaceDescription') is not None:
            self.namespace_description = m.get('NamespaceDescription')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

