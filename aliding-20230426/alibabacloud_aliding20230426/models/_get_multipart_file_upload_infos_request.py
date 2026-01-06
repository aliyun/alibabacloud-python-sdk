# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GetMultipartFileUploadInfosRequest(DaraModel):
    def __init__(
        self,
        option: main_models.GetMultipartFileUploadInfosRequestOption = None,
        part_numbers: List[int] = None,
        tenant_context: main_models.GetMultipartFileUploadInfosRequestTenantContext = None,
        upload_key: str = None,
    ):
        self.option = option
        self.part_numbers = part_numbers
        self.tenant_context = tenant_context
        self.upload_key = upload_key

    def validate(self):
        if self.option:
            self.option.validate()
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.option is not None:
            result['Option'] = self.option.to_map()

        if self.part_numbers is not None:
            result['PartNumbers'] = self.part_numbers

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        if self.upload_key is not None:
            result['UploadKey'] = self.upload_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Option') is not None:
            temp_model = main_models.GetMultipartFileUploadInfosRequestOption()
            self.option = temp_model.from_map(m.get('Option'))

        if m.get('PartNumbers') is not None:
            self.part_numbers = m.get('PartNumbers')

        if m.get('TenantContext') is not None:
            temp_model = main_models.GetMultipartFileUploadInfosRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        if m.get('UploadKey') is not None:
            self.upload_key = m.get('UploadKey')

        return self

class GetMultipartFileUploadInfosRequestTenantContext(DaraModel):
    def __init__(
        self,
        tenant_id: str = None,
    ):
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

class GetMultipartFileUploadInfosRequestOption(DaraModel):
    def __init__(
        self,
        prefer_intranet: bool = None,
    ):
        self.prefer_intranet = prefer_intranet

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.prefer_intranet is not None:
            result['PreferIntranet'] = self.prefer_intranet

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PreferIntranet') is not None:
            self.prefer_intranet = m.get('PreferIntranet')

        return self

