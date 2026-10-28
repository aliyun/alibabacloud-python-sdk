# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_quotas20200510 import models as main_models
from darabonba.model import DaraModel

class GetQuotaTemplateServiceStatusResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        template_service_status: main_models.GetQuotaTemplateServiceStatusResponseBodyTemplateServiceStatus = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The status of the quota template.
        self.template_service_status = template_service_status

    def validate(self):
        if self.template_service_status:
            self.template_service_status.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.template_service_status is not None:
            result['TemplateServiceStatus'] = self.template_service_status.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TemplateServiceStatus') is not None:
            temp_model = main_models.GetQuotaTemplateServiceStatusResponseBodyTemplateServiceStatus()
            self.template_service_status = temp_model.from_map(m.get('TemplateServiceStatus'))

        return self

class GetQuotaTemplateServiceStatusResponseBodyTemplateServiceStatus(DaraModel):
    def __init__(
        self,
        resource_directory_id: str = None,
        service_status: int = None,
    ):
        # The ID of the resource directory.
        self.resource_directory_id = resource_directory_id
        # The status of the quota template. Valid values:
        # 
        # - -1: Disabled.
        # 
        # - 1: Enabled.
        # 
        # - 0: Unset.
        self.service_status = service_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id

        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')

        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')

        return self

