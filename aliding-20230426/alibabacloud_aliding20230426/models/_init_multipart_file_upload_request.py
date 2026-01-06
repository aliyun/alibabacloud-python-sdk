# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class InitMultipartFileUploadRequest(DaraModel):
    def __init__(
        self,
        option: main_models.InitMultipartFileUploadRequestOption = None,
        parent_dentry_uuid: str = None,
        tenant_context: main_models.InitMultipartFileUploadRequestTenantContext = None,
    ):
        self.option = option
        self.parent_dentry_uuid = parent_dentry_uuid
        self.tenant_context = tenant_context

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

        if self.parent_dentry_uuid is not None:
            result['ParentDentryUuid'] = self.parent_dentry_uuid

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Option') is not None:
            temp_model = main_models.InitMultipartFileUploadRequestOption()
            self.option = temp_model.from_map(m.get('Option'))

        if m.get('ParentDentryUuid') is not None:
            self.parent_dentry_uuid = m.get('ParentDentryUuid')

        if m.get('TenantContext') is not None:
            temp_model = main_models.InitMultipartFileUploadRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        return self

class InitMultipartFileUploadRequestTenantContext(DaraModel):
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

class InitMultipartFileUploadRequestOption(DaraModel):
    def __init__(
        self,
        pre_check_param: main_models.InitMultipartFileUploadRequestOptionPreCheckParam = None,
        prefer_region: str = None,
        storage_driver: str = None,
    ):
        self.pre_check_param = pre_check_param
        self.prefer_region = prefer_region
        self.storage_driver = storage_driver

    def validate(self):
        if self.pre_check_param:
            self.pre_check_param.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pre_check_param is not None:
            result['PreCheckParam'] = self.pre_check_param.to_map()

        if self.prefer_region is not None:
            result['PreferRegion'] = self.prefer_region

        if self.storage_driver is not None:
            result['StorageDriver'] = self.storage_driver

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PreCheckParam') is not None:
            temp_model = main_models.InitMultipartFileUploadRequestOptionPreCheckParam()
            self.pre_check_param = temp_model.from_map(m.get('PreCheckParam'))

        if m.get('PreferRegion') is not None:
            self.prefer_region = m.get('PreferRegion')

        if m.get('StorageDriver') is not None:
            self.storage_driver = m.get('StorageDriver')

        return self

class InitMultipartFileUploadRequestOptionPreCheckParam(DaraModel):
    def __init__(
        self,
        md_5: str = None,
        name: str = None,
        parent_id: str = None,
        size: int = None,
    ):
        self.md_5 = md_5
        self.name = name
        self.parent_id = parent_id
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.md_5 is not None:
            result['Md5'] = self.md_5

        if self.name is not None:
            result['Name'] = self.name

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

