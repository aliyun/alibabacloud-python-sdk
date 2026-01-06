# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class CommitFileRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        option: main_models.CommitFileRequestOption = None,
        parent_dentry_uuid: str = None,
        tenant_context: main_models.CommitFileRequestTenantContext = None,
        upload_key: str = None,
    ):
        self.name = name
        self.option = option
        self.parent_dentry_uuid = parent_dentry_uuid
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
        if self.name is not None:
            result['Name'] = self.name

        if self.option is not None:
            result['Option'] = self.option.to_map()

        if self.parent_dentry_uuid is not None:
            result['ParentDentryUuid'] = self.parent_dentry_uuid

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        if self.upload_key is not None:
            result['UploadKey'] = self.upload_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Option') is not None:
            temp_model = main_models.CommitFileRequestOption()
            self.option = temp_model.from_map(m.get('Option'))

        if m.get('ParentDentryUuid') is not None:
            self.parent_dentry_uuid = m.get('ParentDentryUuid')

        if m.get('TenantContext') is not None:
            temp_model = main_models.CommitFileRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        if m.get('UploadKey') is not None:
            self.upload_key = m.get('UploadKey')

        return self

class CommitFileRequestTenantContext(DaraModel):
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

class CommitFileRequestOption(DaraModel):
    def __init__(
        self,
        app_properties: List[main_models.CommitFileRequestOptionAppProperties] = None,
        conflict_strategy: str = None,
        convert_to_online_doc: bool = None,
        convert_to_online_doc_target_document_type: str = None,
        size: int = None,
    ):
        self.app_properties = app_properties
        self.conflict_strategy = conflict_strategy
        self.convert_to_online_doc = convert_to_online_doc
        self.convert_to_online_doc_target_document_type = convert_to_online_doc_target_document_type
        self.size = size

    def validate(self):
        if self.app_properties:
            for v1 in self.app_properties:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AppProperties'] = []
        if self.app_properties is not None:
            for k1 in self.app_properties:
                result['AppProperties'].append(k1.to_map() if k1 else None)

        if self.conflict_strategy is not None:
            result['ConflictStrategy'] = self.conflict_strategy

        if self.convert_to_online_doc is not None:
            result['ConvertToOnlineDoc'] = self.convert_to_online_doc

        if self.convert_to_online_doc_target_document_type is not None:
            result['ConvertToOnlineDocTargetDocumentType'] = self.convert_to_online_doc_target_document_type

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_properties = []
        if m.get('AppProperties') is not None:
            for k1 in m.get('AppProperties'):
                temp_model = main_models.CommitFileRequestOptionAppProperties()
                self.app_properties.append(temp_model.from_map(k1))

        if m.get('ConflictStrategy') is not None:
            self.conflict_strategy = m.get('ConflictStrategy')

        if m.get('ConvertToOnlineDoc') is not None:
            self.convert_to_online_doc = m.get('ConvertToOnlineDoc')

        if m.get('ConvertToOnlineDocTargetDocumentType') is not None:
            self.convert_to_online_doc_target_document_type = m.get('ConvertToOnlineDocTargetDocumentType')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

class CommitFileRequestOptionAppProperties(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
        visibility: str = None,
    ):
        self.name = name
        self.value = value
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        if self.visibility is not None:
            result['Visibility'] = self.visibility

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')

        return self

