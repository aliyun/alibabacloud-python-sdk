# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateNacosConfigRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        app_name: str = None,
        beta_ips: str = None,
        content: str = None,
        data_id: str = None,
        desc: str = None,
        group: str = None,
        instance_id: str = None,
        namespace_id: str = None,
        tags: str = None,
        type: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The name of the application.
        self.app_name = app_name
        # The list of IP addresses where the beta release of the configuration is performed.
        self.beta_ips = beta_ips
        self.content = content
        # The ID of the data.
        # 
        # This parameter is required.
        self.data_id = data_id
        # The description of the configuration.
        self.desc = desc
        # The ID of the group.
        # 
        # This parameter is required.
        self.group = group
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the namespace.
        self.namespace_id = namespace_id
        # The tags of the configuration.
        self.tags = tags
        # The format of the configuration. Supported formats include TEXT, JSON, and XML.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.beta_ips is not None:
            result['BetaIps'] = self.beta_ips

        if self.content is not None:
            result['Content'] = self.content

        if self.data_id is not None:
            result['DataId'] = self.data_id

        if self.desc is not None:
            result['Desc'] = self.desc

        if self.group is not None:
            result['Group'] = self.group

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('BetaIps') is not None:
            self.beta_ips = m.get('BetaIps')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')

        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('Group') is not None:
            self.group = m.get('Group')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

