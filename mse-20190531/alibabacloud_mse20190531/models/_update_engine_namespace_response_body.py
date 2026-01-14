# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class UpdateEngineNamespaceResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.UpdateEngineNamespaceResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details of the data.
        self.data = data
        # The error code returned if the request failed.
        self.error_code = error_code
        # The message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   `true`: The request was successful.
        # *   `false`: The request failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.UpdateEngineNamespaceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class UpdateEngineNamespaceResponseBodyData(DaraModel):
    def __init__(
        self,
        config_count: int = None,
        namespace: str = None,
        namespace_desc: str = None,
        namespace_show_name: str = None,
        quota: int = None,
        type: int = None,
    ):
        # The quota value.
        self.config_count = config_count
        # The namespace.
        self.namespace = namespace
        # The description of the namespace.
        self.namespace_desc = namespace_desc
        # The display name of the namespace.
        self.namespace_show_name = namespace_show_name
        # The quota of configurations.
        self.quota = quota
        # The type of the namespace. Valid values:
        # 
        # *   `0`: global configuration
        # *   `1`: default namespace
        # *   `2`: custom namespace
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_count is not None:
            result['ConfigCount'] = self.config_count

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.namespace_desc is not None:
            result['NamespaceDesc'] = self.namespace_desc

        if self.namespace_show_name is not None:
            result['NamespaceShowName'] = self.namespace_show_name

        if self.quota is not None:
            result['Quota'] = self.quota

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigCount') is not None:
            self.config_count = m.get('ConfigCount')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NamespaceDesc') is not None:
            self.namespace_desc = m.get('NamespaceDesc')

        if m.get('NamespaceShowName') is not None:
            self.namespace_show_name = m.get('NamespaceShowName')

        if m.get('Quota') is not None:
            self.quota = m.get('Quota')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

