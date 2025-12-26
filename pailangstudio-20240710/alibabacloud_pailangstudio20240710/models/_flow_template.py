# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class FlowTemplate(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        aliyun_document_id: str = None,
        description: str = None,
        description_i18n: Dict[str, str] = None,
        display_name: str = None,
        display_name_i18n: Dict[str, str] = None,
        flow_files: str = None,
        flow_storage_path: str = None,
        flow_template_id: str = None,
        flow_type: str = None,
        locale: str = None,
        reference_count: int = None,
        template_group: str = None,
        template_name: str = None,
        url: str = None,
        version: str = None,
        workspace_id: str = None,
    ):
        self.accessibility = accessibility
        self.aliyun_document_id = aliyun_document_id
        self.description = description
        self.description_i18n = description_i18n
        self.display_name = display_name
        self.display_name_i18n = display_name_i18n
        self.flow_files = flow_files
        self.flow_storage_path = flow_storage_path
        self.flow_template_id = flow_template_id
        self.flow_type = flow_type
        self.locale = locale
        self.reference_count = reference_count
        self.template_group = template_group
        self.template_name = template_name
        self.url = url
        self.version = version
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility

        if self.aliyun_document_id is not None:
            result['AliyunDocumentId'] = self.aliyun_document_id

        if self.description is not None:
            result['Description'] = self.description

        if self.description_i18n is not None:
            result['DescriptionI18N'] = self.description_i18n

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.display_name_i18n is not None:
            result['DisplayNameI18N'] = self.display_name_i18n

        if self.flow_files is not None:
            result['FlowFiles'] = self.flow_files

        if self.flow_storage_path is not None:
            result['FlowStoragePath'] = self.flow_storage_path

        if self.flow_template_id is not None:
            result['FlowTemplateId'] = self.flow_template_id

        if self.flow_type is not None:
            result['FlowType'] = self.flow_type

        if self.locale is not None:
            result['Locale'] = self.locale

        if self.reference_count is not None:
            result['ReferenceCount'] = self.reference_count

        if self.template_group is not None:
            result['TemplateGroup'] = self.template_group

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.url is not None:
            result['Url'] = self.url

        if self.version is not None:
            result['Version'] = self.version

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('AliyunDocumentId') is not None:
            self.aliyun_document_id = m.get('AliyunDocumentId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DescriptionI18N') is not None:
            self.description_i18n = m.get('DescriptionI18N')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('DisplayNameI18N') is not None:
            self.display_name_i18n = m.get('DisplayNameI18N')

        if m.get('FlowFiles') is not None:
            self.flow_files = m.get('FlowFiles')

        if m.get('FlowStoragePath') is not None:
            self.flow_storage_path = m.get('FlowStoragePath')

        if m.get('FlowTemplateId') is not None:
            self.flow_template_id = m.get('FlowTemplateId')

        if m.get('FlowType') is not None:
            self.flow_type = m.get('FlowType')

        if m.get('Locale') is not None:
            self.locale = m.get('Locale')

        if m.get('ReferenceCount') is not None:
            self.reference_count = m.get('ReferenceCount')

        if m.get('TemplateGroup') is not None:
            self.template_group = m.get('TemplateGroup')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

