# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListApplicationSupportedProvisionProtocolTypesResponseBody(DaraModel):
    def __init__(
        self,
        application_supported_provision_protocol_type: main_models.ListApplicationSupportedProvisionProtocolTypesResponseBodyApplicationSupportedProvisionProtocolType = None,
        request_id: str = None,
    ):
        self.application_supported_provision_protocol_type = application_supported_provision_protocol_type
        self.request_id = request_id

    def validate(self):
        if self.application_supported_provision_protocol_type:
            self.application_supported_provision_protocol_type.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_supported_provision_protocol_type is not None:
            result['ApplicationSupportedProvisionProtocolType'] = self.application_supported_provision_protocol_type.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationSupportedProvisionProtocolType') is not None:
            temp_model = main_models.ListApplicationSupportedProvisionProtocolTypesResponseBodyApplicationSupportedProvisionProtocolType()
            self.application_supported_provision_protocol_type = temp_model.from_map(m.get('ApplicationSupportedProvisionProtocolType'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListApplicationSupportedProvisionProtocolTypesResponseBodyApplicationSupportedProvisionProtocolType(DaraModel):
    def __init__(
        self,
        provision_protocol_type: List[str] = None,
    ):
        # 账户同步支持类型
        self.provision_protocol_type = provision_protocol_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.provision_protocol_type is not None:
            result['ProvisionProtocolType'] = self.provision_protocol_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProvisionProtocolType') is not None:
            self.provision_protocol_type = m.get('ProvisionProtocolType')

        return self

