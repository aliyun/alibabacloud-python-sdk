# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExportNacosConfigRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        app_name: str = None,
        data_id: str = None,
        data_ids: str = None,
        group: str = None,
        ids: str = None,
        instance_id: str = None,
        namespace_id: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The application tag.
        self.app_name = app_name
        # The ID of the data that you want to export.
        # 
        # > 
        # 
        # *   Multiple export methods are supported.
        # 
        # *   If you want to export a single configuration, you must leave the Ids parameter empty and specify the DataID and Group parameters.
        self.data_id = data_id
        # The configuration group name and the ID of the configuration that you want to export. Separate multiple configurations with comma (,).
        self.data_ids = data_ids
        # The name of the configuration group.
        self.group = group
        # The ID of the primary key of a configuration item.
        # 
        # >  - Multiple export methods are supported. You must specify this parameter if you want to export multiple configurations. - You can obtain the value of this parameter by calling the ListNacosConfigs operation. - If you specify this parameter, multiple configurations are exported. The DataId and Group parameters are invalid.
        self.ids = ids
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the namespace.
        self.namespace_id = namespace_id

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

        if self.data_id is not None:
            result['DataId'] = self.data_id

        if self.data_ids is not None:
            result['DataIds'] = self.data_ids

        if self.group is not None:
            result['Group'] = self.group

        if self.ids is not None:
            result['Ids'] = self.ids

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')

        if m.get('DataIds') is not None:
            self.data_ids = m.get('DataIds')

        if m.get('Group') is not None:
            self.group = m.get('Group')

        if m.get('Ids') is not None:
            self.ids = m.get('Ids')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        return self

