# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteNacosConfigRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        beta: bool = None,
        data_id: str = None,
        group: str = None,
        instance_id: str = None,
        namespace_id: str = None,
    ):
        # Language type of the returned information:
        # 
        # - zh: Chinese
        # - en: English
        self.accept_language = accept_language
        # Whether it is a Beta release. Default is false.
        # 
        # - `true`: Yes
        # - `false`: No
        self.beta = beta
        # Configuration ID.
        # 
        # This parameter is required.
        self.data_id = data_id
        # Group type.
        # 
        # This parameter is required.
        self.group = group
        # Instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Namespace ID. Default is public.
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

        if self.beta is not None:
            result['Beta'] = self.beta

        if self.data_id is not None:
            result['DataId'] = self.data_id

        if self.group is not None:
            result['Group'] = self.group

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('Beta') is not None:
            self.beta = m.get('Beta')

        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')

        if m.get('Group') is not None:
            self.group = m.get('Group')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        return self

