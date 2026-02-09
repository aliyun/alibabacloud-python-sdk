# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTemplateRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        content: str = None,
        desc_info: str = None,
        icon_urls: str = None,
        image_urls: str = None,
        jump_action: int = None,
        push_style: int = None,
        show_style: int = None,
        template_name: str = None,
        tenant_id: str = None,
        title: str = None,
        uri: str = None,
        variables: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        self.content = content
        self.desc_info = desc_info
        self.icon_urls = icon_urls
        self.image_urls = image_urls
        self.jump_action = jump_action
        self.push_style = push_style
        self.show_style = show_style
        self.template_name = template_name
        self.tenant_id = tenant_id
        self.title = title
        self.uri = uri
        self.variables = variables
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.content is not None:
            result['Content'] = self.content

        if self.desc_info is not None:
            result['DescInfo'] = self.desc_info

        if self.icon_urls is not None:
            result['IconUrls'] = self.icon_urls

        if self.image_urls is not None:
            result['ImageUrls'] = self.image_urls

        if self.jump_action is not None:
            result['JumpAction'] = self.jump_action

        if self.push_style is not None:
            result['PushStyle'] = self.push_style

        if self.show_style is not None:
            result['ShowStyle'] = self.show_style

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.title is not None:
            result['Title'] = self.title

        if self.uri is not None:
            result['Uri'] = self.uri

        if self.variables is not None:
            result['Variables'] = self.variables

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('DescInfo') is not None:
            self.desc_info = m.get('DescInfo')

        if m.get('IconUrls') is not None:
            self.icon_urls = m.get('IconUrls')

        if m.get('ImageUrls') is not None:
            self.image_urls = m.get('ImageUrls')

        if m.get('JumpAction') is not None:
            self.jump_action = m.get('JumpAction')

        if m.get('PushStyle') is not None:
            self.push_style = m.get('PushStyle')

        if m.get('ShowStyle') is not None:
            self.show_style = m.get('ShowStyle')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        if m.get('Variables') is not None:
            self.variables = m.get('Variables')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

